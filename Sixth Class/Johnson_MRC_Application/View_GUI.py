import tkinter as tk
from tkinter import messagebox
from BLL import TripBLL
from DAL import DatabaseConnection
from config import config

class MRCApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("MRC Management System")
        self.root.geometry("600x400")
        self.db = None
        self.trip_bll = None
        self.show_login_screen()
    
    def show_login_screen(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        tk.Label(self.root, text="Login", font=("Arial", 16)).pack(pady=20)
        
        # Username
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        
        # Password
        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        
        # Login button
        tk.Button(self.root, text="Login", command=self.login).pack(pady=20)
    
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        # Connect to database
        self.db = DatabaseConnection(config['host'], username, password, config['database'])
        
        if self.db.connect():
            self.trip_bll = TripBLL(self.db)
            messagebox.showinfo("Success", "Logged in!")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Login failed")
    
    def show_main_menu(self):
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        tk.Label(self.root, text="Main Menu", font=("Arial", 16)).pack(pady=20)
        
        # Buttons
        tk.Button(self.root, text="View All Trips", command=self.view_trips).pack(pady=10)
        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=10)
    
    def view_trips(self):
        # Get trips from BLL
        trips = self.trip_bll.get_all_trips()
        
        # Clear window
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Title
        tk.Label(self.root, text="All Trips", font=("Arial", 16)).pack(pady=10)
        
        # Create text area with scrollbar
        frame = tk.Frame(self.root)
        frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")
        
        text = tk.Text(frame, yscrollcommand=scrollbar.set)
        text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=text.yview)
        
        # Display trips
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
        
        # Back button
        tk.Button(self.root, text="Back", command=self.show_main_menu).pack(pady=10)
    
    def logout(self):
        if self.db:
            self.db.close()
        self.db = None
        self.trip_bll = None
        messagebox.showinfo("Logout", "Logged out")
        self.show_login_screen()

def main():
    root = tk.Tk()
    app = MRCApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
