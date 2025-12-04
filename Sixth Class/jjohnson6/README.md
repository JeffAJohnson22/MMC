# Dragon Ball Z Database Management System
**CSC 6302 Final Project**  
*By: Jeff Johnson*

---

## 🐉 Project Overview

This is a comprehensive database management system themed around Dragon Ball Z. The application allows users to manage characters, battles, transformations, and view detailed statistics about the Dragon Ball universe through an intuitive graphical interface.

---

## 📋 Project Requirements Met

### Part 2: Database Creation ✅

1. **Four Tables with Data**:
   - `Characters` (35 rows) - Main character information
   - `Transformations` (15 rows) - Different power-up forms
   - `Battles` (33 rows) - Battle events
   - `Battle_Participants` (Composite key junction table)
   - `Character_Transformations` (Composite key junction table)

2. **Foreign Keys**: Multiple tables include foreign keys with CASCADE constraints
   - `Battle_Participants` references both `Battles` and `Characters`
   - `Character_Transformations` references both `Characters` and `Transformations`

3. **Composite Primary Keys**:
   - `Battle_Participants(Battle_ID, Character_ID)`
   - `Character_Transformations(Character_ID, Transformation_ID)`

4. **Third Normal Form**: All tables are properly normalized

5. **Required Data Types**:
   - **Date/Time/Datetime**: `Birth_Date`, `Battle_Date`, `Start_Time`, `First_Appearance_Date`
   - **Numeric/Decimal**: `Base_Power_Level DECIMAL(15,2)`, `Power_Multiplier DECIMAL(6,2)`
   - **Enum**: `Race`, `Alignment`, `Outcome`
   - **Boolean/TinyInt**: `Is_Alive BOOLEAN`, `Was_Winner BOOLEAN`, `Destroyed_Planet BOOLEAN`

6. **Views and Stored Procedures**:
   - `Battle_Summary_View` - Aggregates battle data with COUNT, AVG, MAX, SUM
   - `Character_Power_Rankings` - Aggregates character statistics
   - 15+ stored procedures for CRUD operations
   - All procedures use aggregate functions where appropriate

7. **CRUD Procedures**:
   - **Create**: `Add_Character`, `Add_Battle`, `Add_Battle_Participant`
   - **Read**: `Get_All_Characters`, `Get_All_Battles`, `Get_Battle_Details`, etc.
   - **Update**: `Update_Character`, `Update_Battle` (with CASCADE)
   - **Delete**: `Delete_Character`, `Delete_Battle` (with CASCADE)

### Part 3: GUI Application ✅

1. **Three-Layer Architecture**:
   - **View Layer** (`View_GUI.py`) - Graphical interface with Tkinter
   - **Business Logic Layer** (`BLL.py`) - Validation and business rules
   - **Data Access Layer** (`DAL.py`) - Database communication only

2. **Connection Management**:
   - Login screen with configurable host and port
   - Password not hard-coded
   - Database name in config file

3. **All CRUD Operations Available**:
   - ✅ Add characters and battles
   - ✅ Update characters and battles
   - ✅ Delete characters and battles (cascades properly)
   - ✅ View all data with formatted displays

4. **User Feedback**: Error messages and success notifications throughout

5. **Advanced Feature**: 
   - **📈 POWER LEVEL VISUALIZATION CHARTS**
   - Interactive matplotlib charts embedded in GUI
   - 4 different chart types:
     1. Top 10 characters by maximum power (horizontal bar chart)
     2. Character distribution by race (pie chart)
     3. Power level distribution by alignment (box plot)
     4. Top characters by transformation count (bar chart)
   - Uses tabbed interface for easy navigation
   - Real-time data visualization from database

---

## 🚀 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- MySQL Server 8.0+
- pip (Python package manager)

### Step 1: Install Required Python Packages

```bash
pip install -r requirements.txt
```

This will install:
- `mysql-connector-python` - MySQL database connector
- `tkcalendar` - Date picker widget for Tkinter
- `matplotlib` - Charting library for advanced feature

### Step 2: Set Up the Database

1. Start your MySQL server

2. Run the SQL script to create the database:
```bash
mysql -u root -p < JohnsonJeff.sql
```

Or manually:
- Open MySQL Workbench or command line
- Copy and paste the contents of `JohnsonJeff.sql`
- Execute the script

This will:
- Create the `DragonBallZ` database
- Create all tables with proper constraints
- Insert 35+ character records and 30+ battle records
- Create all stored procedures, views, and functions

### Step 3: Verify Database

```sql
USE DragonBallZ;
SHOW TABLES;
```

You should see:
- `Characters`
- `Transformations`
- `Battles`
- `Battle_Participants`
- `Character_Transformations`

---

## 🎮 Running the Application

### Launch the GUI

```bash
python View_GUI.py
```

### Login

1. **Host**: `localhost` (or your MySQL server address)
2. **Username**: Your MySQL username (e.g., `root`)
3. **Password**: Your MySQL password
4. **Port**: `3306` (default MySQL port)

Click **CONNECT** to access the application.

---

## 📖 Application Features

### Main Menu Options

1. **📋 View All Characters**
   - Browse all Dragon Ball Z characters
   - See power levels, transformations, and battle counts
   - Edit, delete, or view battle history for each character

2. **⚔️ View All Battles**
   - Complete battle history
   - View details, edit, or delete battles
   - See aggregate statistics (fighters, power levels, damage)

3. **⭐ View Transformations**
   - List of all transformation forms
   - Power multipliers and energy drain rates
   - Descriptions of each transformation

4. **📊 Saga Statistics**
   - Aggregate data by saga
   - Battle counts, average durations
   - Win/loss records for heroes and villains
   - Planets destroyed count

5. **➕ Add Character**
   - Add new characters to the database
   - Specify race, alignment, power level, etc.
   - Validation ensures data integrity

6. **➕ Add Battle**
   - Create new battle records
   - Set location, date, duration, and outcome
   - Track whether planets were destroyed

7. **📈 POWER LEVEL CHARTS (Advanced Feature)**
   - **Visual analytics with 4 interactive charts**:
     - Top 10 characters by maximum power
     - Character distribution by race
     - Power comparison by alignment
     - Transformation count leaders
   - Tabbed interface for easy navigation
   - Real-time data from database

8. **🚪 Logout**
   - Safely disconnect from database
   - Return to login screen

### Character Management

- **Edit**: Update character information (cascades to related records)
- **Delete**: Remove characters (automatically removes from battles)
- **Battle History**: View complete fight record with statistics

### Battle Management

- **Details**: See all participants, transformations, and damage stats
- **Edit**: Modify battle information (cascades to participants)
- **Delete**: Remove battles (automatically removes all participants)

---

## 🔧 Advanced Feature Details

### Power Level Visualization Charts

This feature provides comprehensive visual analytics of the Dragon Ball Z universe using matplotlib embedded in the Tkinter GUI.

**What Makes It Advanced:**
1. **Integration**: Matplotlib figures embedded directly in Tkinter (not trivial)
2. **Multiple Visualizations**: 4 different chart types with different analysis purposes
3. **Dynamic Data**: Charts generated in real-time from database queries
4. **Interactive Navigation**: Tabbed interface to switch between chart types
5. **Professional Styling**: Custom colors, labels, and formatting

**Chart Types:**

1. **Top Power Levels** (Horizontal Bar Chart)
   - Shows the 10 most powerful characters
   - Gradient color scheme from gold to light yellow
   - Power values displayed on bars
   - Sorted by maximum potential power

2. **Race Distribution** (Pie Chart)
   - Percentage breakdown of character races
   - Color-coded segments
   - Shows diversity of the Dragon Ball universe

3. **Alignment Comparison** (Box Plot)
   - Statistical distribution of power by alignment
   - Shows median, quartiles, and outliers
   - Compares heroes, villains, and neutral characters

4. **Transformation Leaders** (Bar Chart)
   - Top 10 characters by transformation count
   - Gold/Silver/Bronze for top 3
   - Shows who has mastered the most forms

**Why This Feature:**
- Provides insights that aren't obvious from raw data
- Makes the database interactive and engaging
- Demonstrates data analysis skills beyond basic CRUD
- Uses professional data visualization library
- Enhances user experience significantly

---

## 📁 File Structure

```
jjohnson6/
├── JohnsonJeff.sql          # Complete database schema and data
├── config.py                # Database configuration
├── DAL.py                   # Data Access Layer
├── BLL.py                   # Business Logic Layer
├── View_GUI.py              # GUI View Layer (run this)
├── requirements.txt         # Python dependencies
└── README.md               # This file
```

---

## 🗄️ Database Schema

### Characters Table
- Primary Key: `Character_ID`
- Stores: Name, race, alignment, power level, status, origin
- Data types: INT, VARCHAR, ENUM, DATE, DECIMAL, BOOLEAN

### Transformations Table
- Primary Key: `Transformation_ID`
- Stores: Name, multiplier, drain rate, requirements
- Data types: INT, VARCHAR, DECIMAL, TEXT

### Battles Table
- Primary Key: `Battle_ID`
- Stores: Name, location, date, time, duration, outcome, saga
- Data types: INT, VARCHAR, DATE, TIME, ENUM, BOOLEAN

### Battle_Participants Table (Junction)
- **Composite Primary Key**: `(Battle_ID, Character_ID)`
- Foreign Keys: References Battles and Characters (CASCADE)
- Stores: Power level in battle, damage dealt/taken, winner status

### Character_Transformations Table (Junction)
- **Composite Primary Key**: `(Character_ID, Transformation_ID)`
- Foreign Keys: References Characters and Transformations (CASCADE)
- Stores: Date unlocked, mastery level

---

## 🎯 Usage Examples

### Adding a Character
1. Click "➕ Add Character"
2. Fill in all fields:
   - Name: "Trunks"
   - Race: Select "Saiyan"
   - Alignment: Select "Hero"
   - Birth Date: Choose date
   - Base Power Level: 7000
   - Is Alive: True
   - Planet Origin: "Earth"
   - First Appearance: Choose date
3. Click "Add Character"

### Viewing Battle Statistics
1. Click "⚔️ View All Battles"
2. Find a battle and click "Details"
3. See all participants, transformations used, and damage statistics

### Creating Power Charts
1. Click "📈 POWER LEVEL CHARTS"
2. Navigate between tabs to see different visualizations
3. Charts update automatically with current database data

---

## 🔒 Security Notes

- Passwords are not stored or hard-coded
- Database credentials entered at login
- All SQL uses parameterized stored procedures (prevents SQL injection)
- User input validated in Business Logic Layer

---

## 🐛 Troubleshooting

### Connection Failed
- Verify MySQL server is running
- Check username and password
- Confirm database "DragonBallZ" exists
- Try port 3306 (default MySQL port)

### Module Not Found
```bash
pip install -r requirements.txt
```

### Charts Not Displaying
- Ensure matplotlib is installed
- Check Python version (3.8+)
- Try: `pip install --upgrade matplotlib`

### Database Errors
- Re-run `JohnsonJeff.sql` to reset database
- Verify all stored procedures exist:
  ```sql
  SHOW PROCEDURE STATUS WHERE Db = 'DragonBallZ';
  ```

---

## 📊 Project Statistics

- **Total Database Tables**: 5
- **Total Stored Procedures**: 15
- **Total Views**: 2
- **Character Records**: 35
- **Battle Records**: 33
- **Lines of Python Code**: ~1000+
- **Lines of SQL**: ~700+

---

## 🎓 Learning Outcomes

This project demonstrates:
- 3-tier architecture design
- Database normalization (3NF)
- Complex SQL with aggregates and joins
- Stored procedure development
- CASCADE operations
- GUI development with Tkinter
- Data visualization with matplotlib
- Business logic separation
- Input validation
- Error handling
- User experience design

---

## 👨‍💻 Author

**Jeff Johnson**  
CSC 6302 - Database Management Systems  
Final Project - Fall 2025

---

## 📝 Notes

- The database contains 35 Dragon Ball Z characters with authentic information
- Battle data includes major fights from various sagas
- Power levels and transformations reflect the anime/manga
- All CASCADE operations work properly for updates and deletes
- The advanced feature (charts) was independently researched and implemented

---

## 🚀 Future Enhancements

Possible additions (not implemented):
- Export battle reports to PDF
- Import characters from CSV
- User authentication system
- More advanced analytics
- Search and filter functionality
- Custom SQL query interface

---

**Enjoy managing the Dragon Ball Z universe!** 🐉⚡

