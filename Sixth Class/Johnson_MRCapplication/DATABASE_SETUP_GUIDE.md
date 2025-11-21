# How to Connect to Your Database

## The Problem
The `Starter_Code_Week_4+5.sql` file **creates the database** - it's not a database you connect to, it's a script that builds one.

---

## Solution: Run the SQL File ONCE

### Option 1: MySQL Workbench (Recommended)
1. Open **MySQL Workbench**
2. Connect to your MySQL server
3. Go to **File → Open SQL Script**
4. Select `Starter_Code_Week_4+5.sql`
5. Click the **⚡ Execute** button (or press Ctrl+Shift+Enter)
6. Wait for it to finish - you'll see "mrc" database created

### Option 2: MySQL Command Line
```bash
mysql -u root -p < "Starter_Code_Week_4+5.sql"
```
Enter your password when prompted.

### Option 3: MySQL Command Line (Windows)
```powershell
& "C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe" -u root -p < "c:\Users\jeffa\Desktop\MMC\Sixth Class\Johnson_MRCapplication\Starter_Code_Week_4+5.sql"
```

---

## What Gets Created

After running the SQL file, you'll have:

**Database:** `mrc`

**Tables:**
- `vessels` (with 3 sample vessels)
- `passengers` (with 5 sample passengers)
- `trips` (with 18 sample trips)

**Views:**
- `all trips` - formatted trip display
- `total revenue by vessel` - revenue summary

**Functions:**
- `getVesselID(vesselName)` - returns vessel ID or -1
- `getPassengerID(firstName, lastName)` - returns passenger ID or -1

**Stored Procedures:**
- `getPassengerList()` - list all passengers
- `getVesselList()` - list all vessels
- `getTripList()` - list all trips
- `addPassenger(fname, lname, phone)` - add new passenger
- `addVessel(name, costPerHour)` - add new vessel
- `addTrip(...)` - add new trip
- `deletePassenger(id)` - delete passenger
- `deleteVessel(id)` - delete vessel

---

## Now Connect From Python

Your `config.py` is already set up correctly:
```python
config = {
    'username': 'root',
    'password': 'password',     # ← Change to YOUR MySQL password
    'database': 'mrc',           # ← This is the database created by SQL file
    'host': 'localhost',
    'port': 3306
}
```

Your `DAL.py` test code will work:
```python
from config import config
from DAL import DatabaseConnection

db = DatabaseConnection(
    config['host'], 
    config['username'], 
    config['password'], 
    config['database']
)

if db.connect():  
    print("✅ Connected to mrc database!")
    cursor = db.get_cursor()
    
    # Test: Get all vessels
    cursor.callproc('getVesselList')
    for result in cursor.stored_results():
        vessels = result.fetchall()
        for vessel in vessels:
            print(f"  {vessel['Vessel']} - ${vessel['Cost_Per_Hour']}/hr")
    
    db.close()
else:
    print("❌ Connection failed!")
```

---

## Checklist

- [ ] MySQL is running
- [ ] Run `Starter_Code_Week_4+5.sql` in MySQL Workbench (do this ONCE)
- [ ] Update `config.py` with your MySQL password
- [ ] Database name is set to `'mrc'` in config.py ✅ (already done)
- [ ] Run your Python application

---

## Verify Database Exists

In MySQL Workbench, run:
```sql
SHOW DATABASES;
```
You should see `mrc` in the list.

```sql
USE mrc;
SHOW TABLES;
```
You should see: `passengers`, `trips`, `vessels`
