import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import DateEntry
from BLL import TripBLL, VesselBLL, PassengerBLL
from DAL import DatabaseConnection
from config import config
from datetime import datetime

class MRCApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("MRC Application")
        self.root.geometry("800x800")
        self.db = None
        self.trip_bll = None
        self.vessel_bll = None
        self.passenger_bll = None
        self.show_login_screen()
    
    def show_login_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Login", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        
        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        
        tk.Button(self.root, text="Login", command=self.login).pack(pady=20)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        self.db = DatabaseConnection(config['host'], username, password, config['database'])
        
        if self.db.connect():
            self.trip_bll = TripBLL(self.db)
            self.vessel_bll = VesselBLL(self.db)
            self.passenger_bll = PassengerBLL(self.db)
            messagebox.showinfo("","Logged in")
            self.show_main_menu()
        else:
            messagebox.showerror("","Login failed")
    
    def show_main_menu(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Main Menu", font=("Helvetica", 16)).pack(pady=20)
        
        tk.Button(self.root, text="View All Trips", command=self.view_trips, width=20).pack(pady=10)
        tk.Button(self.root, text="Add A Trip", command=self.add_trip, width=20).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.logout, width=20).pack(pady=10)
    
    def view_trips(self):
        trips = self.trip_bll.get_all_trips()
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="All Trips", font=("Helvetica", 16)).pack(pady=10)
        
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        
        text = tk.Text(frame, font=("Helvetica", 12), yscrollcommand=scrollbar.set)
        text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text.yview)
        
        if trips:
            for trip in trips:
                trip_info = f"Date/Time: {trip['Date and Time']} | "
                trip_info += f"Vessel: {trip['Vessel Name']} | "
                trip_info += f"Passenger: {trip['Passenger Name']} | "
                trip_info += f"Address: {trip['Passenger Address']} | "
                trip_info += f"Phone: {trip['Passenger Phone']} | "
                trip_info += f"Duration: {trip['Trip Duration']}hrs | "
                trip_info += f"Cost: {trip['Total Cost']}\n\n"
                text.insert("end", trip_info)
        else:
            text.insert("end", "No trips found")
        
        tk.Button(self.root, text="Back", command=self.show_main_menu).pack(pady=10)
    
    def add_trip(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Add New Trip", font=("Helvetica", 16)).pack(pady=10)
        
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=20)
        
        vessels = self.vessel_bll.get_all_vessels()
        passengers = self.passenger_bll.get_all_passengers()
        
        tk.Label(form_frame, text="Vessel:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        vessel_var = tk.StringVar()
        vessel_names = [v['Vessel'] for v in vessels]
        vessel_dropdown = ttk.Combobox(form_frame, textvariable=vessel_var, values=vessel_names, state="readonly", width=30)
        vessel_dropdown.grid(row=0, column=1, padx=5, pady=5)
        if vessel_names:
            vessel_dropdown.current(0)
        
        tk.Label(form_frame, text="Passenger:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        passenger_var = tk.StringVar()
        passenger_names = [f"{p['First_Name']} {p['Last_Name']}" for p in passengers]
        passenger_dropdown = ttk.Combobox(form_frame, textvariable=passenger_var, values=passenger_names, state="readonly", width=30)
        passenger_dropdown.grid(row=1, column=1, padx=5, pady=5)
        if passenger_names:
            passenger_dropdown.current(0)
        
        tk.Label(form_frame, text="Date:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        date_entry = DateEntry(form_frame, width=28, background='darkblue', foreground='white', borderwidth=2)
        date_entry.grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Departure Time:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        time_frame = tk.Frame(form_frame)
        time_frame.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        
        hour_var = tk.StringVar(value="09")
        minute_var = tk.StringVar(value="00")
        
        hour_spinner = ttk.Spinbox(time_frame, from_=0, to=23, textvariable=hour_var, width=5, format="%02.0f")
        hour_spinner.pack(side="left")
        tk.Label(time_frame, text=":").pack(side="left")
        minute_spinner = ttk.Spinbox(time_frame, from_=0, to=59, textvariable=minute_var, width=5, format="%02.0f")
        minute_spinner.pack(side="left")
        
        tk.Label(form_frame, text="Length (hours):").grid(row=4, column=0, sticky="e", padx=5, pady=5)
        length_entry = tk.Entry(form_frame, width=32)
        length_entry.grid(row=4, column=1, padx=5, pady=5)
        length_entry.insert(0, "2.0")
        
        tk.Label(form_frame, text="Total Passengers:").grid(row=5, column=0, sticky="e", padx=5, pady=5)
        passengers_entry = tk.Entry(form_frame, width=32)
        passengers_entry.grid(row=5, column=1, padx=5, pady=5)
        passengers_entry.insert(0, "1")
        
        def submit_trip():
            try:
                vessel_name = vessel_var.get()
                
                passenger_full = passenger_var.get()
                passenger_parts = passenger_full.split(" ", 1)
                passenger_first = passenger_parts[0]
                passenger_last = passenger_parts[1] if len(passenger_parts) > 1 else ""
                
                trip_date = date_entry.get_date().strftime('%Y-%m-%d')
                
                departure_time = f"{hour_var.get()}:{minute_var.get()}:00"
                
                length = float(length_entry.get())
                total_pass = int(passengers_entry.get())
                
                result = self.trip_bll.add_trip(
                    vessel_name, 
                    passenger_first, 
                    passenger_last,
                    trip_date,
                    departure_time,
                    length,
                    total_pass
                )
                
                if result and 'error' in result:
                    messagebox.showerror("Error", result['error'])
                else:
                    messagebox.showinfo("Success", "Trip added successfully!")
                    self.show_main_menu()
                    
            except ValueError as e:
                messagebox.showerror("Error", "Please enter valid numbers for length and passengers")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add trip: {str(e)}")
        
        tk.Button(self.root, text="Add Trip", command=submit_trip, width=15).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.show_main_menu, width=15).pack(pady=5)
    
    def logout(self):
        if self.db:
            self.db.close()
        self.db = None
        self.trip_bll = None
        self.vessel_bll = None
        self.passenger_bll = None
        messagebox.showinfo("", "Logged out")
        self.show_login_screen()

def main():
    root = tk.Tk()
    app = MRCApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
