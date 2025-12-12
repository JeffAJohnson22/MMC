"""
Simplified View Layer (GUI)
Dragon Ball Z Database Management System
"""

import tkinter as tk
from tkinter import messagebox, ttk
from tkcalendar import DateEntry
from BLL import CharacterBLL, BattleBLL, TransformationBLL
from DAL import DatabaseConnection
from config import config
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class DBZApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Dragon Ball Z Database Manager")
        self.root.geometry("900x600")
        self.root.configure(bg='#FF8C00')
        
        self.db = None
        self.character_bll = None
        self.battle_bll = None
        self.transformation_bll = None
        
        self.show_login()
    
    def show_login(self):
        """Display login screen"""
        self.clear_window()
        
        frame = tk.Frame(self.root, bg='#FF8C00')
        frame.place(relx=0.5, rely=0.5, anchor='center')
        
        tk.Label(frame, text="Dragon Ball Z Database", font=('Arial', 24, 'bold'), 
                bg='#FF8C00', fg='white').pack(pady=20)
        
        tk.Label(frame, text="Username:", bg='#FF8C00', fg='white', font=('Arial', 12)).pack()
        self.username_entry = tk.Entry(frame, font=('Arial', 12), width=25)
        self.username_entry.pack(pady=5)
        self.username_entry.insert(0, config.get('username', 'root'))
        
        tk.Label(frame, text="Password:", bg='#FF8C00', fg='white', font=('Arial', 12)).pack()
        self.password_entry = tk.Entry(frame, show='*', font=('Arial', 12), width=25)
        self.password_entry.pack(pady=5)
        self.password_entry.insert(0, config.get('password', ''))
        
        tk.Button(frame, text="Login", command=self.login, bg='#4CAF50', fg='white',
                 font=('Arial', 12, 'bold'), width=20).pack(pady=20)
    
    def login(self):
        """Attempt database connection"""
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        self.db = DatabaseConnection(
            host=config.get('host', 'localhost'),
            username=username,
            password=password,
            database=config.get('database', 'DragonBallZ'),
            port=config.get('port', 3306)
        )
        
        if self.db.connect():
            self.character_bll = CharacterBLL(self.db)
            self.battle_bll = BattleBLL(self.db)
            self.transformation_bll = TransformationBLL(self.db)
            messagebox.showinfo("Success", "Connected to Database!")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Failed to connect to database")
    
    def show_main_menu(self):
        """Display main menu"""
        self.clear_window()
        
        tk.Label(self.root, text="Main Menu", font=('Arial', 20, 'bold'),
                bg='#FF8C00', fg='white').pack(pady=30)
        
        button_frame = tk.Frame(self.root, bg='#FF8C00')
        button_frame.pack(pady=20)
        
        buttons = [
            ("View All Battles", self.view_battles),
            ("View All Characters", self.view_characters),
            ("Add Character", self.add_character_form),
            ("Power Level Chart", self.show_power_chart),
            ("Logout", self.logout)
        ]
        
        for text, command in buttons:
            tk.Button(button_frame, text=text, command=command,
                     bg='#4CAF50', fg='white', font=('Arial', 14),
                     width=20, height=2).pack(pady=10)
    
    def view_battles(self):
        """Display all battles with aggregate statistics"""
        self.clear_window()
        
        tk.Label(self.root, text="All Battles (with Statistics)", font=('Arial', 18, 'bold'),
                bg='#FF8C00', fg='white').pack(pady=10)
        
        # Create treeview
        frame = tk.Frame(self.root)
        frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        columns = ('Battle', 'Date', 'Location', 'Outcome', 'Fighters', 'Avg Power', 'Max Power')
        tree = ttk.Treeview(frame, columns=columns, show='headings', height=15)
        
        # Configure columns
        tree.heading('Battle', text='Battle Name')
        tree.heading('Date', text='Date')
        tree.heading('Location', text='Location')
        tree.heading('Outcome', text='Outcome')
        tree.heading('Fighters', text='Total Fighters')
        tree.heading('Avg Power', text='Avg Power Level')
        tree.heading('Max Power', text='Max Power Level')
        
        tree.column('Battle', width=250)
        tree.column('Date', width=100)
        tree.column('Location', width=120)
        tree.column('Outcome', width=120)
        tree.column('Fighters', width=100)
        tree.column('Avg Power', width=120)
        tree.column('Max Power', width=120)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Get data
        battles = self.battle_bll.get_all_battles()
        if battles:
            for battle in battles:
                tree.insert('', 'end', values=(
                    battle.get('Battle_Name', ''),
                    battle.get('Battle_Date', ''),
                    battle.get('Location', ''),
                    battle.get('Outcome', ''),
                    battle.get('Total_Fighters', 0),
                    battle.get('Avg_Power_Display', 'N/A'),
                    battle.get('Max_Power_Display', 'N/A')
                ))
        
        tk.Button(self.root, text="Back to Menu", command=self.show_main_menu,
                 bg='#f44336', fg='white', font=('Arial', 12), width=15).pack(pady=10)
    
    def view_characters(self):
        """Display all characters"""
        self.clear_window()
        
        tk.Label(self.root, text="All Characters", font=('Arial', 18, 'bold'),
                bg='#FF8C00', fg='white').pack(pady=10)
        
        # Create treeview
        frame = tk.Frame(self.root)
        frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        columns = ('ID', 'Name', 'Race', 'Alignment', 'Power Level', 'Status', 'Planet')
        tree = ttk.Treeview(frame, columns=columns, show='headings', height=15)
        
        # Configure columns
        for col in columns:
            tree.heading(col, text=col)
        
        tree.column('ID', width=50)
        tree.column('Name', width=150)
        tree.column('Race', width=100)
        tree.column('Alignment', width=100)
        tree.column('Power Level', width=120)
        tree.column('Status', width=80)
        tree.column('Planet', width=120)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
        tree.configure(yscrollcommand=scrollbar.set)
        
        tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Get data
        characters = self.character_bll.get_all_characters()
        if characters:
            for char in characters:
                tree.insert('', 'end', values=(
                    char.get('Character_ID', ''),
                    char.get('Character_Name', ''),
                    char.get('Race', ''),
                    char.get('Alignment', ''),
                    char.get('Base_Power_Level_Display', ''),
                    char.get('Status', ''),
                    char.get('Planet_Origin', '')
                ))
        
        tk.Button(self.root, text="Back to Menu", command=self.show_main_menu,
                 bg='#f44336', fg='white', font=('Arial', 12), width=15).pack(pady=10)
    
    def add_character_form(self):
        """Display add character form"""
        self.clear_window()
        
        tk.Label(self.root, text="Add New Character", font=('Arial', 18, 'bold'),
                bg='#FF8C00', fg='white').pack(pady=20)
        
        form_frame = tk.Frame(self.root, bg='#FF8C00')
        form_frame.pack(pady=20)
        
        # Name
        tk.Label(form_frame, text="Name:", bg='#FF8C00', fg='white', font=('Arial', 12)).grid(row=0, column=0, sticky='e', padx=10, pady=5)
        name_entry = tk.Entry(form_frame, font=('Arial', 12), width=30)
        name_entry.grid(row=0, column=1, pady=5)
        
        # Race
        tk.Label(form_frame, text="Race:", bg='#FF8C00', fg='white', font=('Arial', 12)).grid(row=1, column=0, sticky='e', padx=10, pady=5)
        race_var = tk.StringVar(value='Saiyan')
        race_combo = ttk.Combobox(form_frame, textvariable=race_var, font=('Arial', 12), width=28,
                                  values=['Saiyan', 'Namekian', 'Human', 'Android', 'Majin', 'Other'])
        race_combo.grid(row=1, column=1, pady=5)
        
        # Alignment
        tk.Label(form_frame, text="Alignment:", bg='#FF8C00', fg='white', font=('Arial', 12)).grid(row=2, column=0, sticky='e', padx=10, pady=5)
        alignment_var = tk.StringVar(value='Hero')
        alignment_combo = ttk.Combobox(form_frame, textvariable=alignment_var, font=('Arial', 12), width=28,
                                      values=['Hero', 'Villain', 'Neutral'])
        alignment_combo.grid(row=2, column=1, pady=5)
        
        # Birth Date
        tk.Label(form_frame, text="Birth Date:", bg='#FF8C00', fg='white', font=('Arial', 12)).grid(row=3, column=0, sticky='e', padx=10, pady=5)
        date_entry = DateEntry(form_frame, width=28, font=('Arial', 12))
        date_entry.grid(row=3, column=1, pady=5)
        
        # Power Level
        tk.Label(form_frame, text="Base Power Level:", bg='#FF8C00', fg='white', font=('Arial', 12)).grid(row=4, column=0, sticky='e', padx=10, pady=5)
        power_entry = tk.Entry(form_frame, font=('Arial', 12), width=30)
        power_entry.grid(row=4, column=1, pady=5)
        power_entry.insert(0, '1000')
        
        # Is Alive
        tk.Label(form_frame, text="Is Alive:", bg='#FF8C00', fg='white', font=('Arial', 12)).grid(row=5, column=0, sticky='e', padx=10, pady=5)
        alive_var = tk.BooleanVar(value=True)
        tk.Checkbutton(form_frame, variable=alive_var, bg='#FF8C00', font=('Arial', 12)).grid(row=5, column=1, sticky='w', pady=5)
        
        # Planet
        tk.Label(form_frame, text="Planet Origin:", bg='#FF8C00', fg='white', font=('Arial', 12)).grid(row=6, column=0, sticky='e', padx=10, pady=5)
        planet_entry = tk.Entry(form_frame, font=('Arial', 12), width=30)
        planet_entry.grid(row=6, column=1, pady=5)
        planet_entry.insert(0, 'Earth')
        
        def submit():
            try:
                name = name_entry.get()
                race = race_var.get()
                alignment = alignment_var.get()
                birth_date = date_entry.get_date().strftime('%Y-%m-%d')
                power_level = float(power_entry.get())
                is_alive = alive_var.get()
                planet = planet_entry.get()
                
                result = self.character_bll.add_character(name, race, alignment, birth_date,
                                                         power_level, is_alive, planet)
                
                if result and 'error' in str(result):
                    messagebox.showerror("Error", str(result))
                else:
                    messagebox.showinfo("Success", f"Character '{name}' added successfully!")
                    self.show_main_menu()
            except ValueError:
                messagebox.showerror("Error", "Please enter a valid power level number")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to add character: {str(e)}")
        
        button_frame = tk.Frame(self.root, bg='#FF8C00')
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="Add Character", command=submit,
                 bg='#4CAF50', fg='white', font=('Arial', 12), width=15).pack(side='left', padx=10)
        tk.Button(button_frame, text="Cancel", command=self.show_main_menu,
                 bg='#f44336', fg='white', font=('Arial', 12), width=15).pack(side='left', padx=10)
    def show_power_chart(self):
        """Display power level chart for top characters"""
        self.clear_window()
        
        tk.Label(self.root, text="Character Power Levels", font=('Arial', 18, 'bold'),
                bg='#FF8C00', fg='white').pack(pady=10)
        
        # Get characters data
        characters = self.character_bll.get_all_characters()
        
        if not characters:
            messagebox.showinfo("No Data", "No characters found in database")
            self.show_main_menu()
            return
        
        # Get top 15 characters by power level
        top_characters = sorted(characters, key=lambda x: float(x.get('Base_Power_Level', 0)), reverse=True)[:15]
        
        # Create figure
        fig = Figure(figsize=(10, 6), facecolor='#FF8C00')
        ax = fig.add_subplot(111)
        
        # Extract data
        names = [char['Character_Name'] for char in top_characters]
        powers = [float(char['Base_Power_Level']) for char in top_characters]
        
        # Create bar chart
        colors = ['#FF6B6B' if char['Alignment'] == 'Villain' else '#4ECDC4' if char['Alignment'] == 'Hero' else '#95E1D3' 
                  for char in top_characters]
        
        bars = ax.barh(names, powers, color=colors)
        
        # Customize chart
        ax.set_xlabel('Base Power Level', fontsize=12, fontweight='bold')
        ax.set_title('Top 15 Characters by Power Level', fontsize=14, fontweight='bold')
        ax.set_facecolor('#FFF5E6')
        ax.grid(axis='x', alpha=0.3)
        
        # Format x-axis with commas
        ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'{int(x):,}'))
        
        # Add legend
        from matplotlib.patches import Patch
        legend_elements = [
            Patch(facecolor='#4ECDC4', label='Hero'),
            Patch(facecolor='#FF6B6B', label='Villain'),
            Patch(facecolor='#95E1D3', label='Neutral')
        ]
        ax.legend(handles=legend_elements, loc='lower right')
        
        fig.tight_layout()
        
        # Embed chart in tkinter
        chart_frame = tk.Frame(self.root)
        chart_frame.pack(fill='both', expand=True, padx=20, pady=10)
        
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
        
        tk.Button(self.root, text="Back to Menu", command=self.show_main_menu,
                 bg='#f44336', fg='white', font=('Arial', 12), width=15).pack(pady=10)
    
    def logout(self):
        """Close connection and return to login"""
        if self.db:
            self.db.close()
        self.db = None
        self.character_bll = None
        self.battle_bll = None
        self.transformation_bll = None
        messagebox.showinfo("Logged Out", "Successfully logged out")
        self.show_login()
    
    def clear_window(self):
        """Clear all widgets from window"""
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = DBZApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()
