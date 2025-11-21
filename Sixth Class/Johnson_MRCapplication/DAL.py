# A way to connect to the database, establish and manage a cursor, and if needed, commit data and/or close the connection. Many people use a custom connection class, but this is not strictly necessary.
import mysql.connector
from mysql.connector import Error
from config import config

class DatabaseConnection:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        """Establish a database connection."""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                return True
        except Error as e:
            print(f"Error: {e}")
            return False

    def get_cursor(self):
        """Get a cursor from the connection."""
        if self.connection and self.connection.is_connected():
            return self.connection.cursor(dictionary=True)
        else:
            raise Exception("Database not connected")

    def commit(self):
        """Commit the current transaction."""
        if self.connection and self.connection.is_connected():
            self.connection.commit()
        else:
            raise Exception("Database not connected")

    def close(self):
        """Close the database connection."""
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None



db = DatabaseConnection(config['host'], config['username'], config['password'], config['database'])
if db.connect():  
    print("✅ Connected to mrc database!")
    cursor = db.get_cursor()

    # switch case to demonstrate commit and close
    choice = input("Enter 'commit' to commit changes or 'close' to close the connection: ").strip().lower()
    if choice == 'commit':
        db.commit()
    elif choice == 'close':
        db.close()
    else:
        print("Invalid choice. No action taken.")
else:
    print("❌ Connection failed!")