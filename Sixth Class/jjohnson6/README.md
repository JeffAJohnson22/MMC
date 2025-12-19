# Dragon Ball Z Database Management System

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- MySQL Server 8.0 or higher
- MySQL Workbench (recommended for database setup)

### Step 1: Install Python Dependencies

```powershell
# Navigate to the project directory
# Install required packages
pip install -r requirements.txt
```

**Required packages:**

- `mysql-connector-python==8.3.0`
- `matplotlib==3.8.2`
- `tkcalendar==1.6.1`

### Step 2: Set Up the Database

1. Open MySQL Workbench
2. Connect to your MySQL server
3. Open the `DBZ.sql` file
4. Execute the entire script to create the `DragonBallZ` database

### Step 3: Configuration

The `config.py` file contains default connection settings:

```python
config = {
    'host': 'localhost',
    'database': 'DragonBallZ',
    'port': 3306
}
```

### Step 4: Run the GUI

```powershell
python View_GUI.py
```

### Step 5: Login

When the application starts, you'll see the login screen:

1. **Username**: Enter your MySQL username (default: `root`)
2. **Password**: Enter your MySQL password
3. Click **Login**

**Technologies Used**:

- Python 3.11
- MySQL 8.0
- tkinter (GUI)
- matplotlib (Data Visualization)
- mysql-connector-python (Database Connectivity)

