"""
Script to set up the MRC database from Starter_Code_Week_4+5.sql
Run this ONCE to create the database and tables

IMPORTANT: This uses subprocess to call mysql command line directly,
which properly handles DELIMITER statements for stored procedures.
"""

import subprocess
import os
from config import config

def setup_database():
    """Execute the SQL starter code to create the mrc database."""
    
    sql_file = 'Starter_Code_Week_4+5.sql'
    
    if not os.path.exists(sql_file):
        print(f"  Error: {sql_file} not found in current directory")
        return False
    
    print("Setting up MRC database...")
    print(f"Using SQL file: {sql_file}")
    print(f"Host: {config['host']}")
    print(f"User: {config['username']}")
    print(f"Database: {config['database']}")
    print()
    
    # Find MySQL executable (common paths)
    mysql_paths = [
        r"C:\Program Files\MySQL\MySQL Server 8.0\bin\mysql.exe",
        r"C:\Program Files\MySQL\MySQL Server 8.4\bin\mysql.exe",
        r"C:\Program Files\MySQL\MySQL Server 9.0\bin\mysql.exe",
        r"C:\xampp\mysql\bin\mysql.exe",
        "mysql"  # If in PATH
    ]
    
    mysql_exe = None
    for path in mysql_paths:
        if os.path.exists(path) or path == "mysql":
            mysql_exe = path
            break
    
    if not mysql_exe:
        print("  MySQL executable not found!")
        print("\nPlease use MySQL Workbench instead:")
        print("  1. Open MySQL Workbench")
        print("  2. File → Open SQL Script")
        print(f"  3. Select: {os.path.abspath(sql_file)}")
        print("  4. Click Execute (⚡) button")
        return False
    
    print(f"Using MySQL at: {mysql_exe}")
    
    # Build command
    cmd = [
        mysql_exe,
        f"--host={config['host']}",
        f"--user={config['username']}",
        f"--password={config['password']}",
        "-e",
        f"source {sql_file}"
    ]
    
    try:
        # Execute MySQL command
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            cwd=os.path.dirname(os.path.abspath(__file__))
        )
        
        if result.returncode == 0:
            print("\n Database 'mrc' created successfully!")
            print(" Tables created: vessels, passengers, trips")
            print(" Views created: 'all trips', 'total revenue by vessel'")
            print(" Functions created: getVesselID(), getPassengerID()")
            print(" Procedures created: getPassengerList, getVesselList, getTripList,")
            print("   addPassenger, addVessel, addTrip, deletePassenger, deleteVessel")
            print("\nYou can now run your application!")
            return True
        else:
            print(f"\n Error executing SQL file:")
            print(result.stderr)
            print("\nPlease use MySQL Workbench instead (see above for instructions)")
            return False
            
    except FileNotFoundError:
        print(" MySQL command line tool not found!")
        print("\nPlease use MySQL Workbench instead:")
        print("  1. Open MySQL Workbench")
        print("  2. File → Open SQL Script")
        print(f"  3. Select: {os.path.abspath(sql_file)}")
        print("  4. Click Execute (⚡) button")
        return False
    except Exception as e:
        print(f"\n Error: {e}")
        return False

if __name__ == "__main__":
    print("="*60)
    print("MRC Database Setup")
    print("="*60)
    print()
    
    success = setup_database()
    
    if not success:
        print("\n" + "="*60)
        print("ALTERNATIVE: Use MySQL Workbench")
        print("="*60)
        print("This is the RECOMMENDED method for running the SQL file.")
        print()
        print("Steps:")
        print("  1. Open MySQL Workbench")
        print("  2. Connect to your MySQL server")
        print("  3. Go to: File → Open SQL Script")
        print("  4. Navigate to and select: Starter_Code_Week_4+5.sql")
        print("  5. Click the Execute button (⚡ lightning bolt icon)")
        print("  6. Wait for execution to complete")
        print()
        print("Then run this script again to verify the setup.")
