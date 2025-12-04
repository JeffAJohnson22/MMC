"""
View Layer (GUI)
Dragon Ball Z Database Management System
Includes advanced feature: Power Level Visualization Charts
"""

import tkinter as tk
from tkinter import messagebox, ttk, scrolledtext
from tkcalendar import DateEntry
from BLL import CharacterBLL, BattleBLL, TransformationBLL
from DAL import DatabaseConnection
from config import config
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib
matplotlib.use('TkAgg')

class DBZApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Dragon Ball Z Database Manager")
        self.root.geometry("1000x700")
        self.root.configure(bg='#FF8C00')
        
        self.db = None
        self.character_bll = None
        self.battle_bll = None
        self.transformation_bll = None
        
        self.show_login_screen()
    
    def show_login_screen(self):
        """Display login interface"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        # Main frame
        main_frame = tk.Frame(self.root, bg='#FF8C00')
        main_frame.pack(expand=True)
        
        # Title
        title = tk.Label(main_frame, text="🐉 DRAGON BALL Z 🐉", 
                        font=("Arial", 28, "bold"), bg='#FF8C00', fg='#FF4500')
        title.pack(pady=20)
        
        subtitle = tk.Label(main_frame, text="Database Management System", 
                           font=("Arial", 14), bg='#FF8C00', fg='white')
        subtitle.pack(pady=5)
        
        # Login form
        form_frame = tk.Frame(main_frame, bg='white', padx=30, pady=30)
        form_frame.pack(pady=30)
        
        tk.Label(form_frame, text="Host:", font=("Arial", 11), bg='white').grid(row=0, column=0, sticky='e', padx=5, pady=10)
        self.host_entry = tk.Entry(form_frame, width=30, font=("Arial", 11))
        self.host_entry.insert(0, config['host'])
        self.host_entry.grid(row=0, column=1, padx=5, pady=10)
        
        tk.Label(form_frame, text="Username:", font=("Arial", 11), bg='white').grid(row=1, column=0, sticky='e', padx=5, pady=10)
        self.username_entry = tk.Entry(form_frame, width=30, font=("Arial", 11))
        self.username_entry.grid(row=1, column=1, padx=5, pady=10)
        
        tk.Label(form_frame, text="Password:", font=("Arial", 11), bg='white').grid(row=2, column=0, sticky='e', padx=5, pady=10)
        self.password_entry = tk.Entry(form_frame, show="*", width=30, font=("Arial", 11))
        self.password_entry.grid(row=2, column=1, padx=5, pady=10)
        
        tk.Label(form_frame, text="Port:", font=("Arial", 11), bg='white').grid(row=3, column=0, sticky='e', padx=5, pady=10)
        self.port_entry = tk.Entry(form_frame, width=30, font=("Arial", 11))
        self.port_entry.insert(0, str(config['port']))
        self.port_entry.grid(row=3, column=1, padx=5, pady=10)
        
        btn_frame = tk.Frame(form_frame, bg='white')
        btn_frame.grid(row=4, column=0, columnspan=2, pady=20)
        
        login_btn = tk.Button(btn_frame, text="CONNECT", command=self.login, 
                             bg='#FF4500', fg='white', font=("Arial", 12, "bold"),
                             width=15, cursor='hand2')
        login_btn.pack()
    
    def login(self):
        """Attempt database connection"""
        host = self.host_entry.get()
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        try:
            port = int(self.port_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Invalid port number")
            return
        
        if not username or not password:
            messagebox.showerror("Error", "Username and password are required")
            return
        
        self.db = DatabaseConnection(host, username, password, config['database'], port)
        
        if self.db.connect():
            self.character_bll = CharacterBLL(self.db)
            self.battle_bll = BattleBLL(self.db)
            self.transformation_bll = TransformationBLL(self.db)
            messagebox.showinfo("Success", "Connected to Dragon Ball Z Database!")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Connection failed. Check credentials and try again.")
    
    def show_main_menu(self):
        """Display main menu"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg='#FF8C00')
        
        # Title
        title_frame = tk.Frame(self.root, bg='#FF8C00')
        title_frame.pack(pady=20)
        
        tk.Label(title_frame, text="🐉 DRAGON BALL Z DATABASE 🐉", 
                font=("Arial", 24, "bold"), bg='#FF8C00', fg='#FF4500').pack()
        
        # Menu buttons frame
        menu_frame = tk.Frame(self.root, bg='#FF8C00')
        menu_frame.pack(expand=True)
        
        button_config = {
            'font': ("Arial", 12, "bold"),
            'width': 30,
            'height': 2,
            'cursor': 'hand2',
            'bg': '#FF4500',
            'fg': 'white',
            'activebackground': '#FF6347'
        }
        
        tk.Button(menu_frame, text="📋 View All Characters", 
                 command=self.view_characters, **button_config).pack(pady=8)
        tk.Button(menu_frame, text="⚔️ View All Battles", 
                 command=self.view_battles, **button_config).pack(pady=8)
        tk.Button(menu_frame, text="⭐ View Transformations", 
                 command=self.view_transformations, **button_config).pack(pady=8)
        tk.Button(menu_frame, text="📊 Saga Statistics", 
                 command=self.view_saga_stats, **button_config).pack(pady=8)
        tk.Button(menu_frame, text="➕ Add Character", 
                 command=self.add_character_screen, **button_config).pack(pady=8)
        tk.Button(menu_frame, text="➕ Add Battle", 
                 command=self.add_battle_screen, **button_config).pack(pady=8)
        tk.Button(menu_frame, text="📈 POWER LEVEL CHARTS (Advanced Feature)", 
                 command=self.show_power_charts, bg='#32CD32', 
                 activebackground='#228B22', **{k:v for k,v in button_config.items() if k not in ['bg', 'activebackground']}).pack(pady=8)
        tk.Button(menu_frame, text="🚪 Logout", 
                 command=self.logout, bg='#696969', 
                 activebackground='#505050', **{k:v for k,v in button_config.items() if k not in ['bg', 'activebackground']}).pack(pady=8)
    
    def view_characters(self):
        """Display all characters"""
        characters = self.character_bll.get_all_characters()
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg='white')
        
        # Header
        header = tk.Frame(self.root, bg='#FF8C00')
        header.pack(fill='x')
        tk.Label(header, text="CHARACTER ROSTER", font=("Arial", 18, "bold"), 
                bg='#FF8C00', fg='white').pack(pady=15)
        
        # Scrollable frame
        container = tk.Frame(self.root)
        container.pack(fill='both', expand=True, padx=10, pady=10)
        
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        if characters:
            for i, char in enumerate(characters):
                char_frame = tk.Frame(scrollable_frame, bg='#f0f0f0', relief='ridge', bd=2)
                char_frame.pack(fill='x', padx=5, pady=5)
                
                info_text = f"🥋 {char['Character_Name']} | Race: {char['Race']} | Alignment: {char['Alignment']}\n"
                info_text += f"   Base Power: {char['Base_Power_Level']} | Max Potential: {char['Max_Power_Potential']}\n"
                info_text += f"   Transformations: {char['Total_Transformations']} | Battles: {char['Battles_Participated']} | Status: {char['Status']}"
                
                tk.Label(char_frame, text=info_text, font=("Arial", 10), 
                        bg='#f0f0f0', justify='left').pack(anchor='w', padx=10, pady=5)
                
                btn_frame = tk.Frame(char_frame, bg='#f0f0f0')
                btn_frame.pack(anchor='e', padx=10, pady=5)
                
                char_id = char['Character_ID']
                tk.Button(btn_frame, text="Edit", command=lambda cid=char_id: self.edit_character_screen(cid),
                         bg='#4CAF50', fg='white', width=8).pack(side='left', padx=3)
                tk.Button(btn_frame, text="Delete", command=lambda cid=char_id: self.delete_character(cid),
                         bg='#f44336', fg='white', width=8).pack(side='left', padx=3)
                tk.Button(btn_frame, text="Battle History", command=lambda cid=char_id: self.view_character_battles(cid),
                         bg='#2196F3', fg='white', width=12).pack(side='left', padx=3)
        else:
            tk.Label(scrollable_frame, text="No characters found", 
                    font=("Arial", 12)).pack(pady=20)
        
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Back button
        tk.Button(self.root, text="← Back to Menu", command=self.show_main_menu,
                 bg='#FF8C00', fg='white', font=("Arial", 11, "bold")).pack(pady=10)
    
    def view_battles(self):
        """Display all battles"""
        battles = self.battle_bll.get_all_battles()
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg='white')
        
        header = tk.Frame(self.root, bg='#FF4500')
        header.pack(fill='x')
        tk.Label(header, text="⚔️ BATTLE HISTORY ⚔️", font=("Arial", 18, "bold"), 
                bg='#FF4500', fg='white').pack(pady=15)
        
        container = tk.Frame(self.root)
        container.pack(fill='both', expand=True, padx=10, pady=10)
        
        canvas = tk.Canvas(container)
        scrollbar = ttk.Scrollbar(container, orient='vertical', command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)
        
        scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        if battles:
            for battle in battles:
                battle_frame = tk.Frame(scrollable_frame, bg='#ffe6e6', relief='ridge', bd=2)
                battle_frame.pack(fill='x', padx=5, pady=5)
                
                info_text = f"⚔️ {battle['Battle_Name']}\n"
                info_text += f"   📍 {battle['Location']} | 📅 {battle['Battle_Date']} | ⏱️ {battle['Duration_Minutes']} min\n"
                info_text += f"   Saga: {battle['Saga']} | Outcome: {battle['Outcome']}\n"
                info_text += f"   Fighters: {battle['Total_Fighters']} | Avg Power: {battle['Avg_Power_Level']} | Max Power: {battle['Max_Power_Level']}\n"
                info_text += f"   Planet Destroyed: {battle['Planet_Destroyed']}"
                
                tk.Label(battle_frame, text=info_text, font=("Arial", 9), 
                        bg='#ffe6e6', justify='left').pack(anchor='w', padx=10, pady=5)
                
                btn_frame = tk.Frame(battle_frame, bg='#ffe6e6')
                btn_frame.pack(anchor='e', padx=10, pady=5)
                
                battle_id = battle['Battle_ID']
                tk.Button(btn_frame, text="Details", command=lambda bid=battle_id: self.view_battle_details(bid),
                         bg='#2196F3', fg='white', width=10).pack(side='left', padx=3)
                tk.Button(btn_frame, text="Edit", command=lambda bid=battle_id: self.edit_battle_screen(bid),
                         bg='#4CAF50', fg='white', width=8).pack(side='left', padx=3)
                tk.Button(btn_frame, text="Delete", command=lambda bid=battle_id: self.delete_battle(bid),
                         bg='#f44336', fg='white', width=8).pack(side='left', padx=3)
        else:
            tk.Label(scrollable_frame, text="No battles found", font=("Arial", 12)).pack(pady=20)
        
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        tk.Button(self.root, text="← Back to Menu", command=self.show_main_menu,
                 bg='#FF8C00', fg='white', font=("Arial", 11, "bold")).pack(pady=10)
    
    def view_transformations(self):
        """Display all transformations"""
        transformations = self.transformation_bll.get_all_transformations()
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg='white')
        
        header = tk.Frame(self.root, bg='#FFD700')
        header.pack(fill='x')
        tk.Label(header, text="⭐ TRANSFORMATIONS ⭐", font=("Arial", 18, "bold"), 
                bg='#FFD700', fg='#8B0000').pack(pady=15)
        
        container = tk.Frame(self.root)
        container.pack(fill='both', expand=True, padx=10, pady=10)
        
        text = scrolledtext.ScrolledText(container, font=("Arial", 10), wrap=tk.WORD)
        text.pack(fill='both', expand=True)
        
        if transformations:
            for trans in transformations:
                trans_info = f"⭐ {trans['Transformation_Name']}\n"
                trans_info += f"   Power Multiplier: {trans['Multiplier']}\n"
                trans_info += f"   Energy Drain: {trans['Energy_Drain_Rate']} | Required Power: {trans.get('Required_Power_Level', 'N/A')}\n"
                trans_info += f"   {trans.get('Description', '')}\n"
                trans_info += "="*80 + "\n\n"
                text.insert('end', trans_info)
        else:
            text.insert('end', "No transformations found")
        
        text.config(state='disabled')
        
        tk.Button(self.root, text="← Back to Menu", command=self.show_main_menu,
                 bg='#FF8C00', fg='white', font=("Arial", 11, "bold")).pack(pady=10)
    
    def view_saga_stats(self):
        """Display saga statistics"""
        stats = self.battle_bll.get_saga_statistics()
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg='white')
        
        header = tk.Frame(self.root, bg='#9370DB')
        header.pack(fill='x')
        tk.Label(header, text="📊 SAGA STATISTICS 📊", font=("Arial", 18, "bold"), 
                bg='#9370DB', fg='white').pack(pady=15)
        
        container = tk.Frame(self.root)
        container.pack(fill='both', expand=True, padx=10, pady=10)
        
        text = scrolledtext.ScrolledText(container, font=("Courier", 11), wrap=tk.WORD)
        text.pack(fill='both', expand=True)
        
        if stats:
            header_line = f"{'SAGA':<30} {'BATTLES':<10} {'AVG MIN':<10} {'PLANETS':<10} {'HERO W':<10} {'VILLAIN W':<10}\n"
            text.insert('end', header_line)
            text.insert('end', "="*90 + "\n")
            
            for saga in stats:
                line = f"{saga['Saga']:<30} {saga['Total_Battles']:<10} "
                line += f"{saga['Avg_Duration']:<10} {saga['Planets_Destroyed']:<10} "
                line += f"{saga['Hero_Victories']:<10} {saga['Villain_Victories']:<10}\n"
                text.insert('end', line)
        else:
            text.insert('end', "No saga statistics available")
        
        text.config(state='disabled')
        
        tk.Button(self.root, text="← Back to Menu", command=self.show_main_menu,
                 bg='#FF8C00', fg='white', font=("Arial", 11, "bold")).pack(pady=10)
    
    def add_character_screen(self):
        """Screen to add new character"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg='#FF8C00')
        
        tk.Label(self.root, text="ADD NEW CHARACTER", font=("Arial", 18, "bold"), 
                bg='#FF8C00', fg='white').pack(pady=20)
        
        form_frame = tk.Frame(self.root, bg='white', padx=20, pady=20)
        form_frame.pack(padx=20, pady=10)
        
        fields = {}
        
        tk.Label(form_frame, text="Name:", bg='white').grid(row=0, column=0, sticky='e', padx=5, pady=5)
        fields['name'] = tk.Entry(form_frame, width=35)
        fields['name'].grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Race:", bg='white').grid(row=1, column=0, sticky='e', padx=5, pady=5)
        fields['race'] = ttk.Combobox(form_frame, width=33, state='readonly',
                                      values=['Saiyan', 'Namekian', 'Human', 'Android', 'Majin', 'Kai', 'Demon', 'Fusion', 'Other'])
        fields['race'].grid(row=1, column=1, padx=5, pady=5)
        fields['race'].current(0)
        
        tk.Label(form_frame, text="Alignment:", bg='white').grid(row=2, column=0, sticky='e', padx=5, pady=5)
        fields['alignment'] = ttk.Combobox(form_frame, width=33, state='readonly',
                                          values=['Hero', 'Villain', 'Neutral'])
        fields['alignment'].grid(row=2, column=1, padx=5, pady=5)
        fields['alignment'].current(0)
        
        tk.Label(form_frame, text="Birth Date:", bg='white').grid(row=3, column=0, sticky='e', padx=5, pady=5)
        fields['birth_date'] = DateEntry(form_frame, width=33)
        fields['birth_date'].grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Base Power Level:", bg='white').grid(row=4, column=0, sticky='e', padx=5, pady=5)
        fields['power'] = tk.Entry(form_frame, width=35)
        fields['power'].insert(0, "1000")
        fields['power'].grid(row=4, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Is Alive:", bg='white').grid(row=5, column=0, sticky='e', padx=5, pady=5)
        fields['alive'] = ttk.Combobox(form_frame, width=33, state='readonly', values=['True', 'False'])
        fields['alive'].grid(row=5, column=1, padx=5, pady=5)
        fields['alive'].current(0)
        
        tk.Label(form_frame, text="Planet Origin:", bg='white').grid(row=6, column=0, sticky='e', padx=5, pady=5)
        fields['planet'] = tk.Entry(form_frame, width=35)
        fields['planet'].insert(0, "Earth")
        fields['planet'].grid(row=6, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="First Appearance:", bg='white').grid(row=7, column=0, sticky='e', padx=5, pady=5)
        fields['appearance'] = DateEntry(form_frame, width=33)
        fields['appearance'].grid(row=7, column=1, padx=5, pady=5)
        
        def submit():
            result = self.character_bll.add_character(
                fields['name'].get(),
                fields['race'].get(),
                fields['alignment'].get(),
                fields['birth_date'].get_date().strftime('%Y-%m-%d'),
                fields['power'].get(),
                fields['alive'].get(),
                fields['planet'].get(),
                fields['appearance'].get_date().strftime('%Y-%m-%d')
            )
            
            if result and 'error' in result:
                messagebox.showerror("Error", result['error'])
            else:
                messagebox.showinfo("Success", "Character added successfully!")
                self.view_characters()
        
        btn_frame = tk.Frame(self.root, bg='#FF8C00')
        btn_frame.pack(pady=15)
        
        tk.Button(btn_frame, text="Add Character", command=submit, 
                 bg='#4CAF50', fg='white', font=("Arial", 11, "bold"), width=15).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.show_main_menu,
                 bg='#f44336', fg='white', font=("Arial", 11, "bold"), width=15).pack(side='left', padx=5)
    
    def add_battle_screen(self):
        """Screen to add new battle"""
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg='#FF8C00')
        
        tk.Label(self.root, text="ADD NEW BATTLE", font=("Arial", 18, "bold"), 
                bg='#FF8C00', fg='white').pack(pady=20)
        
        form_frame = tk.Frame(self.root, bg='white', padx=20, pady=20)
        form_frame.pack(padx=20, pady=10)
        
        fields = {}
        
        tk.Label(form_frame, text="Battle Name:", bg='white').grid(row=0, column=0, sticky='e', padx=5, pady=5)
        fields['name'] = tk.Entry(form_frame, width=35)
        fields['name'].grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Location:", bg='white').grid(row=1, column=0, sticky='e', padx=5, pady=5)
        fields['location'] = tk.Entry(form_frame, width=35)
        fields['location'].grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Battle Date:", bg='white').grid(row=2, column=0, sticky='e', padx=5, pady=5)
        fields['date'] = DateEntry(form_frame, width=33)
        fields['date'].grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Start Time (HH:MM:SS):", bg='white').grid(row=3, column=0, sticky='e', padx=5, pady=5)
        fields['time'] = tk.Entry(form_frame, width=35)
        fields['time'].insert(0, "12:00:00")
        fields['time'].grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Duration (minutes):", bg='white').grid(row=4, column=0, sticky='e', padx=5, pady=5)
        fields['duration'] = tk.Entry(form_frame, width=35)
        fields['duration'].insert(0, "60")
        fields['duration'].grid(row=4, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Outcome:", bg='white').grid(row=5, column=0, sticky='e', padx=5, pady=5)
        fields['outcome'] = ttk.Combobox(form_frame, width=33, state='readonly',
                                        values=['Hero Victory', 'Villain Victory', 'Draw', 'Interrupted'])
        fields['outcome'].grid(row=5, column=1, padx=5, pady=5)
        fields['outcome'].current(0)
        
        tk.Label(form_frame, text="Saga:", bg='white').grid(row=6, column=0, sticky='e', padx=5, pady=5)
        fields['saga'] = tk.Entry(form_frame, width=35)
        fields['saga'].grid(row=6, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Destroyed Planet:", bg='white').grid(row=7, column=0, sticky='e', padx=5, pady=5)
        fields['destroyed'] = ttk.Combobox(form_frame, width=33, state='readonly', values=['False', 'True'])
        fields['destroyed'].grid(row=7, column=1, padx=5, pady=5)
        fields['destroyed'].current(0)
        
        def submit():
            result = self.battle_bll.add_battle(
                fields['name'].get(),
                fields['location'].get(),
                fields['date'].get_date().strftime('%Y-%m-%d'),
                fields['time'].get(),
                fields['duration'].get(),
                fields['outcome'].get(),
                fields['saga'].get(),
                fields['destroyed'].get()
            )
            
            if result and 'error' in result:
                messagebox.showerror("Error", result['error'])
            else:
                messagebox.showinfo("Success", "Battle added successfully!")
                self.view_battles()
        
        btn_frame = tk.Frame(self.root, bg='#FF8C00')
        btn_frame.pack(pady=15)
        
        tk.Button(btn_frame, text="Add Battle", command=submit, 
                 bg='#4CAF50', fg='white', font=("Arial", 11, "bold"), width=15).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.show_main_menu,
                 bg='#f44336', fg='white', font=("Arial", 11, "bold"), width=15).pack(side='left', padx=5)
    
    def edit_character_screen(self, char_id):
        """Edit existing character"""
        char_data = self.character_bll.get_character_details(char_id)
        if not char_data:
            messagebox.showerror("Error", "Character not found")
            return
        
        char = char_data[0]
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg='#FF8C00')
        
        tk.Label(self.root, text=f"EDIT CHARACTER: {char['Character_Name']}", 
                font=("Arial", 18, "bold"), bg='#FF8C00', fg='white').pack(pady=20)
        
        form_frame = tk.Frame(self.root, bg='white', padx=20, pady=20)
        form_frame.pack(padx=20, pady=10)
        
        fields = {}
        
        tk.Label(form_frame, text="Name:", bg='white').grid(row=0, column=0, sticky='e', padx=5, pady=5)
        fields['name'] = tk.Entry(form_frame, width=35)
        fields['name'].insert(0, char['Character_Name'])
        fields['name'].grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Race:", bg='white').grid(row=1, column=0, sticky='e', padx=5, pady=5)
        fields['race'] = ttk.Combobox(form_frame, width=33, state='readonly',
                                      values=['Saiyan', 'Namekian', 'Human', 'Android', 'Majin', 'Kai', 'Demon', 'Fusion', 'Other'])
        fields['race'].grid(row=1, column=1, padx=5, pady=5)
        fields['race'].set(char['Race'])
        
        tk.Label(form_frame, text="Alignment:", bg='white').grid(row=2, column=0, sticky='e', padx=5, pady=5)
        fields['alignment'] = ttk.Combobox(form_frame, width=33, state='readonly',
                                          values=['Hero', 'Villain', 'Neutral'])
        fields['alignment'].grid(row=2, column=1, padx=5, pady=5)
        fields['alignment'].set(char['Alignment'])
        
        tk.Label(form_frame, text="Birth Date:", bg='white').grid(row=3, column=0, sticky='e', padx=5, pady=5)
        fields['birth_date'] = DateEntry(form_frame, width=33)
        if char['Birth_Date']:
            fields['birth_date'].set_date(char['Birth_Date'])
        fields['birth_date'].grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Base Power Level:", bg='white').grid(row=4, column=0, sticky='e', padx=5, pady=5)
        fields['power'] = tk.Entry(form_frame, width=35)
        fields['power'].insert(0, str(char['Base_Power_Level']))
        fields['power'].grid(row=4, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Is Alive:", bg='white').grid(row=5, column=0, sticky='e', padx=5, pady=5)
        fields['alive'] = ttk.Combobox(form_frame, width=33, state='readonly', values=['True', 'False'])
        fields['alive'].grid(row=5, column=1, padx=5, pady=5)
        fields['alive'].set('True' if char['Is_Alive'] else 'False')
        
        tk.Label(form_frame, text="Planet Origin:", bg='white').grid(row=6, column=0, sticky='e', padx=5, pady=5)
        fields['planet'] = tk.Entry(form_frame, width=35)
        fields['planet'].insert(0, char['Planet_Origin'] or '')
        fields['planet'].grid(row=6, column=1, padx=5, pady=5)
        
        def submit():
            result = self.character_bll.update_character(
                char_id,
                fields['name'].get(),
                fields['race'].get(),
                fields['alignment'].get(),
                fields['birth_date'].get_date().strftime('%Y-%m-%d'),
                fields['power'].get(),
                fields['alive'].get(),
                fields['planet'].get()
            )
            
            if result and 'error' in result:
                messagebox.showerror("Error", result['error'])
            else:
                messagebox.showinfo("Success", "Character updated successfully!")
                self.view_characters()
        
        btn_frame = tk.Frame(self.root, bg='#FF8C00')
        btn_frame.pack(pady=15)
        
        tk.Button(btn_frame, text="Save Changes", command=submit, 
                 bg='#4CAF50', fg='white', font=("Arial", 11, "bold"), width=15).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.view_characters,
                 bg='#f44336', fg='white', font=("Arial", 11, "bold"), width=15).pack(side='left', padx=5)
    
    def edit_battle_screen(self, battle_id):
        """Edit existing battle"""
        battle_details = self.battle_bll.get_battle_details(battle_id)
        if not battle_details:
            messagebox.showerror("Error", "Battle not found")
            return
        
        battle = battle_details[0]
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg='#FF8C00')
        
        tk.Label(self.root, text=f"EDIT BATTLE: {battle['Battle_Name']}", 
                font=("Arial", 18, "bold"), bg='#FF8C00', fg='white').pack(pady=20)
        
        form_frame = tk.Frame(self.root, bg='white', padx=20, pady=20)
        form_frame.pack(padx=20, pady=10)
        
        fields = {}
        
        tk.Label(form_frame, text="Battle Name:", bg='white').grid(row=0, column=0, sticky='e', padx=5, pady=5)
        fields['name'] = tk.Entry(form_frame, width=35)
        fields['name'].insert(0, battle['Battle_Name'])
        fields['name'].grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Location:", bg='white').grid(row=1, column=0, sticky='e', padx=5, pady=5)
        fields['location'] = tk.Entry(form_frame, width=35)
        fields['location'].insert(0, battle['Location'])
        fields['location'].grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Battle Date:", bg='white').grid(row=2, column=0, sticky='e', padx=5, pady=5)
        fields['date'] = DateEntry(form_frame, width=33)
        if battle['Battle_Date']:
            fields['date'].set_date(battle['Battle_Date'])
        fields['date'].grid(row=2, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Start Time (HH:MM:SS):", bg='white').grid(row=3, column=0, sticky='e', padx=5, pady=5)
        fields['time'] = tk.Entry(form_frame, width=35)
        fields['time'].insert(0, str(battle['Start_Time']) if battle['Start_Time'] else '12:00:00')
        fields['time'].grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Duration (minutes):", bg='white').grid(row=4, column=0, sticky='e', padx=5, pady=5)
        fields['duration'] = tk.Entry(form_frame, width=35)
        fields['duration'].insert(0, str(battle['Duration_Minutes']))
        fields['duration'].grid(row=4, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Outcome:", bg='white').grid(row=5, column=0, sticky='e', padx=5, pady=5)
        fields['outcome'] = ttk.Combobox(form_frame, width=33, state='readonly',
                                        values=['Hero Victory', 'Villain Victory', 'Draw', 'Interrupted'])
        fields['outcome'].grid(row=5, column=1, padx=5, pady=5)
        fields['outcome'].set(battle['Outcome'])
        
        tk.Label(form_frame, text="Saga:", bg='white').grid(row=6, column=0, sticky='e', padx=5, pady=5)
        fields['saga'] = tk.Entry(form_frame, width=35)
        fields['saga'].insert(0, battle['Saga'] or '')
        fields['saga'].grid(row=6, column=1, padx=5, pady=5)
        
        tk.Label(form_frame, text="Destroyed Planet:", bg='white').grid(row=7, column=0, sticky='e', padx=5, pady=5)
        fields['destroyed'] = ttk.Combobox(form_frame, width=33, state='readonly', values=['False', 'True'])
        fields['destroyed'].grid(row=7, column=1, padx=5, pady=5)
        fields['destroyed'].set('True' if battle['Destroyed_Planet'] else 'False')
        
        def submit():
            result = self.battle_bll.update_battle(
                battle_id,
                fields['name'].get(),
                fields['location'].get(),
                fields['date'].get_date().strftime('%Y-%m-%d'),
                fields['time'].get(),
                fields['duration'].get(),
                fields['outcome'].get(),
                fields['saga'].get(),
                fields['destroyed'].get()
            )
            
            if result and 'error' in result:
                messagebox.showerror("Error", result['error'])
            else:
                messagebox.showinfo("Success", "Battle updated successfully!")
                self.view_battles()
        
        btn_frame = tk.Frame(self.root, bg='#FF8C00')
        btn_frame.pack(pady=15)
        
        tk.Button(btn_frame, text="Save Changes", command=submit, 
                 bg='#4CAF50', fg='white', font=("Arial", 11, "bold"), width=15).pack(side='left', padx=5)
        tk.Button(btn_frame, text="Cancel", command=self.view_battles,
                 bg='#f44336', fg='white', font=("Arial", 11, "bold"), width=15).pack(side='left', padx=5)
    
    def delete_character(self, char_id):
        """Delete a character"""
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this character?\nThis will cascade to all related records."):
            result = self.character_bll.delete_character(char_id)
            if result:
                messagebox.showinfo("Success", "Character deleted successfully!")
                self.view_characters()
            else:
                messagebox.showerror("Error", "Failed to delete character")
    
    def delete_battle(self, battle_id):
        """Delete a battle"""
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this battle?\nThis will cascade to all participants."):
            result = self.battle_bll.delete_battle(battle_id)
            if result:
                messagebox.showinfo("Success", "Battle deleted successfully!")
                self.view_battles()
            else:
                messagebox.showerror("Error", "Failed to delete battle")
    
    def view_character_battles(self, char_id):
        """View character's battle history"""
        history = self.character_bll.get_character_battle_history(char_id)
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg='white')
        
        if history:
            char_name = history[0].get('Battle_Name', 'Character')
        
        header = tk.Frame(self.root, bg='#4169E1')
        header.pack(fill='x')
        tk.Label(header, text="BATTLE HISTORY", font=("Arial", 18, "bold"), 
                bg='#4169E1', fg='white').pack(pady=15)
        
        text = scrolledtext.ScrolledText(self.root, font=("Courier", 10), wrap=tk.WORD)
        text.pack(fill='both', expand=True, padx=10, pady=10)
        
        if history:
            total_battles = history[0].get('Total_Battles', 0)
            total_wins = history[0].get('Total_Wins', 0)
            
            text.insert('end', f"Total Battles: {total_battles} | Total Wins: {total_wins}\n")
            text.insert('end', "="*100 + "\n\n")
            
            for battle in history:
                battle_info = f"⚔️ {battle['Battle_Name']}\n"
                battle_info += f"   Date: {battle['Battle_Date']} | Location: {battle['Location']}\n"
                battle_info += f"   Saga: {battle['Saga']} | Outcome: {battle['Outcome']}\n"
                battle_info += f"   Power Level: {battle['Power_Level_In_Battle']}\n"
                if battle.get('Transformation_Name'):
                    battle_info += f"   Transformation: {battle['Transformation_Name']}\n"
                battle_info += f"   Damage Dealt: {battle['Damage_Dealt']} | Damage Taken: {battle['Damage_Taken']}\n"
                battle_info += f"   Result: {battle['Result']}\n"
                battle_info += "-"*100 + "\n\n"
                text.insert('end', battle_info)
        else:
            text.insert('end', "No battle history found for this character")
        
        text.config(state='disabled')
        
        tk.Button(self.root, text="← Back", command=self.view_characters,
                 bg='#FF8C00', fg='white', font=("Arial", 11, "bold")).pack(pady=10)
    
    def view_battle_details(self, battle_id):
        """View detailed battle information"""
        details = self.battle_bll.get_battle_details(battle_id)
        
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg='white')
        
        header = tk.Frame(self.root, bg='#DC143C')
        header.pack(fill='x')
        
        if details:
            tk.Label(header, text=f"⚔️ {details[0]['Battle_Name']} ⚔️", 
                    font=("Arial", 18, "bold"), bg='#DC143C', fg='white').pack(pady=15)
        
        text = scrolledtext.ScrolledText(self.root, font=("Courier", 10), wrap=tk.WORD)
        text.pack(fill='both', expand=True, padx=10, pady=10)
        
        if details:
            battle = details[0]
            text.insert('end', f"Location: {battle['Location']}\n")
            text.insert('end', f"Date: {battle['Battle_Date']} | Start Time: {battle['Start_Time']}\n")
            text.insert('end', f"Duration: {battle['Duration_Minutes']} minutes\n")
            text.insert('end', f"Saga: {battle['Saga']} | Outcome: {battle['Outcome']}\n")
            text.insert('end', f"Planet Destroyed: {'Yes' if battle['Destroyed_Planet'] else 'No'}\n\n")
            text.insert('end', "="*100 + "\n")
            text.insert('end', "PARTICIPANTS:\n")
            text.insert('end', "="*100 + "\n\n")
            
            for participant in details:
                part_info = f"🥋 {participant['Character_Name']} ({participant['Race']})\n"
                part_info += f"   Power Level: {participant['Power_Level_In_Battle']}\n"
                if participant.get('Transformation_Name'):
                    part_info += f"   Transformation: {participant['Transformation_Name']}\n"
                part_info += f"   Damage Dealt: {participant['Damage_Dealt']}\n"
                part_info += f"   Damage Taken: {participant['Damage_Taken']}\n"
                part_info += f"   Winner: {'Yes' if participant['Was_Winner'] else 'No'}\n"
                part_info += "-"*100 + "\n\n"
                text.insert('end', part_info)
        else:
            text.insert('end', "Battle details not found")
        
        text.config(state='disabled')
        
        tk.Button(self.root, text="← Back", command=self.view_battles,
                 bg='#FF8C00', fg='white', font=("Arial", 11, "bold")).pack(pady=10)
    
    def show_power_charts(self):
        """
        ADVANCED FEATURE: Power Level Visualization Charts
        Displays interactive charts showing character power levels and battle statistics
        """
        for widget in self.root.winfo_children():
            widget.destroy()
        
        self.root.configure(bg='white')
        
        header = tk.Frame(self.root, bg='#32CD32')
        header.pack(fill='x')
        tk.Label(header, text="📈 POWER LEVEL ANALYSIS 📈", 
                font=("Arial", 18, "bold"), bg='#32CD32', fg='white').pack(pady=15)
        
        # Get data
        characters = self.character_bll.get_all_characters()
        
        if not characters or len(characters) == 0:
            tk.Label(self.root, text="No character data available for charts", 
                    font=("Arial", 14)).pack(pady=50)
            tk.Button(self.root, text="← Back to Menu", command=self.show_main_menu,
                     bg='#FF8C00', fg='white', font=("Arial", 11, "bold")).pack(pady=10)
            return
        
        # Create notebook for multiple charts
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Chart 1: Top 10 Characters by Max Power
        frame1 = tk.Frame(notebook, bg='white')
        notebook.add(frame1, text='Top Power Levels')
        
        # Sort and get top 10
        top_chars = sorted(characters, 
                          key=lambda x: float(x['Max_Power_Potential'].replace(',', '')), 
                          reverse=True)[:10]
        
        names = [c['Character_Name'] for c in top_chars]
        powers = [float(c['Max_Power_Potential'].replace(',', '')) for c in top_chars]
        
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        colors = ['#FFD700', '#FF4500', '#FF8C00', '#FFA500', '#FFB84D', 
                 '#FFC966', '#FFD580', '#FFE199', '#FFEDB3', '#FFF9CC']
        bars = ax1.barh(names, powers, color=colors)
        ax1.set_xlabel('Max Power Level', fontsize=12, fontweight='bold')
        ax1.set_title('Top 10 Characters by Maximum Power', fontsize=14, fontweight='bold')
        ax1.invert_yaxis()
        
        # Add value labels on bars
        for bar in bars:
            width = bar.get_width()
            ax1.text(width, bar.get_y() + bar.get_height()/2, 
                    f'{width:,.0f}', ha='left', va='center', fontsize=9)
        
        canvas1 = FigureCanvasTkAgg(fig1, frame1)
        canvas1.draw()
        canvas1.get_tk_widget().pack(fill='both', expand=True)
        
        # Chart 2: Character Distribution by Race
        frame2 = tk.Frame(notebook, bg='white')
        notebook.add(frame2, text='Race Distribution')
        
        race_counts = {}
        for char in characters:
            race = char['Race']
            race_counts[race] = race_counts.get(race, 0) + 1
        
        fig2, ax2 = plt.subplots(figsize=(10, 6))
        colors2 = plt.cm.Set3(range(len(race_counts)))
        wedges, texts, autotexts = ax2.pie(race_counts.values(), labels=race_counts.keys(), 
                                            autopct='%1.1f%%', colors=colors2, startangle=90)
        ax2.set_title('Character Distribution by Race', fontsize=14, fontweight='bold')
        
        # Make percentage text bold
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
        
        canvas2 = FigureCanvasTkAgg(fig2, frame2)
        canvas2.draw()
        canvas2.get_tk_widget().pack(fill='both', expand=True)
        
        # Chart 3: Hero vs Villain Power Comparison
        frame3 = tk.Frame(notebook, bg='white')
        notebook.add(frame3, text='Alignment Comparison')
        
        alignment_data = {'Hero': [], 'Villain': [], 'Neutral': []}
        for char in characters:
            alignment = char['Alignment']
            power = float(char['Max_Power_Potential'].replace(',', ''))
            if alignment in alignment_data:
                alignment_data[alignment].append(power)
        
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        
        box_data = [alignment_data[align] for align in alignment_data if alignment_data[align]]
        box_labels = [align for align in alignment_data if alignment_data[align]]
        
        bp = ax3.boxplot(box_data, labels=box_labels, patch_artist=True)
        
        colors3 = ['#4169E1', '#DC143C', '#FFD700']
        for patch, color in zip(bp['boxes'], colors3[:len(bp['boxes'])]):
            patch.set_facecolor(color)
        
        ax3.set_ylabel('Maximum Power Level', fontsize=12, fontweight='bold')
        ax3.set_title('Power Level Distribution by Alignment', fontsize=14, fontweight='bold')
        ax3.grid(True, alpha=0.3)
        
        canvas3 = FigureCanvasTkAgg(fig3, frame3)
        canvas3.draw()
        canvas3.get_tk_widget().pack(fill='both', expand=True)
        
        # Chart 4: Transformations per Character
        frame4 = tk.Frame(notebook, bg='white')
        notebook.add(frame4, text='Transformations')
        
        top_transform_chars = sorted([c for c in characters if c['Total_Transformations'] > 0],
                                     key=lambda x: x['Total_Transformations'], reverse=True)[:10]
        
        if top_transform_chars:
            trans_names = [c['Character_Name'] for c in top_transform_chars]
            trans_counts = [c['Total_Transformations'] for c in top_transform_chars]
            
            fig4, ax4 = plt.subplots(figsize=(10, 6))
            bars4 = ax4.bar(range(len(trans_names)), trans_counts, 
                           color=['#FFD700', '#C0C0C0', '#CD7F32'] + ['#4169E1']*(len(trans_names)-3))
            ax4.set_xticks(range(len(trans_names)))
            ax4.set_xticklabels(trans_names, rotation=45, ha='right')
            ax4.set_ylabel('Number of Transformations', fontsize=12, fontweight='bold')
            ax4.set_title('Top Characters by Transformation Count', fontsize=14, fontweight='bold')
            ax4.grid(True, alpha=0.3, axis='y')
            
            # Add value labels
            for bar in bars4:
                height = bar.get_height()
                ax4.text(bar.get_x() + bar.get_width()/2., height,
                        f'{int(height)}', ha='center', va='bottom', fontsize=10, fontweight='bold')
            
            plt.tight_layout()
            
            canvas4 = FigureCanvasTkAgg(fig4, frame4)
            canvas4.draw()
            canvas4.get_tk_widget().pack(fill='both', expand=True)
        else:
            tk.Label(frame4, text="No transformation data available", 
                    font=("Arial", 14)).pack(pady=50)
        
        # Back button
        tk.Button(self.root, text="← Back to Menu", command=self.show_main_menu,
                 bg='#FF8C00', fg='white', font=("Arial", 11, "bold")).pack(pady=10)
    
    def logout(self):
        """Logout and return to login screen"""
        if self.db:
            self.db.close()
        self.db = None
        self.character_bll = None
        self.battle_bll = None
        self.transformation_bll = None
        messagebox.showinfo("Logged Out", "You have been logged out successfully")
        self.show_login_screen()


def main():
    root = tk.Tk()
    app = DBZApplication(root)
    root.mainloop()


if __name__ == "__main__":
    main()
