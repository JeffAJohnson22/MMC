# A way to connect to the database, establish and manage a cursor, and if needed, commit data and/or close the connection. Many people use a custom connection class, but this is not strictly necessary.
import mysql.connector
from mysql.connector import Error

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

class Vessel:
    def __init__(self, db):
        self.db = db

    def add_vessel(self, vessel_name, cost_per_hour):
        """Add a vessel using the addVessel stored procedure"""
        cursor = self.db.get_cursor()
        cursor.callproc('addVessel', (vessel_name, cost_per_hour))
        self.db.commit()
        # Fetch the result to get the VesselID
        for result in cursor.stored_results():
            return result.fetchone()

    def get_vessels(self):
        """Get all vessels using the getVesselList stored procedure"""
        cursor = self.db.get_cursor()
        cursor.callproc('getVesselList')
        # Fetch results from the stored procedure
        for result in cursor.stored_results():
            return result.fetchall()
    
    def delete_vessel(self, vessel_id):
        """Delete a vessel using the deleteVessel stored procedure"""
        cursor = self.db.get_cursor()
        cursor.callproc('deleteVessel', (vessel_id,))
        self.db.commit()
        # Fetch the result to check if vessel was found
        for result in cursor.stored_results():
            return result.fetchone()
    
    def get_vessel_id(self, vessel_name):
        """Get vessel ID by name using the getVesselID function"""
        cursor = self.db.get_cursor()
        query = "SELECT getVesselID(%s) as VesselID"
        cursor.execute(query, (vessel_name,))
        return cursor.fetchone()

class Passenger:
    def __init__(self, db):
        self.db = db

    def add_passenger(self, first_name, last_name, phone):
        """Add a passenger using the addPassenger stored procedure"""
        cursor = self.db.get_cursor()
        cursor.callproc('addPassenger', (first_name, last_name, phone))
        self.db.commit()
        # Fetch the result to get the PassengerID
        for result in cursor.stored_results():
            return result.fetchone()

    def get_passengers(self):
        """Get all passengers using the getPassengerList stored procedure"""
        cursor = self.db.get_cursor()
        cursor.callproc('getPassengerList')
        # Fetch results from the stored procedure
        for result in cursor.stored_results():
            return result.fetchall()
    
    def delete_passenger(self, passenger_id):
        """Delete a passenger using the deletePassenger stored procedure"""
        cursor = self.db.get_cursor()
        cursor.callproc('deletePassenger', (passenger_id,))
        self.db.commit()
        # Fetch the result to check if passenger was found
        for result in cursor.stored_results():
            return result.fetchone()
    
    def get_passenger_id(self, first_name, last_name):
        """Get passenger ID by name using the getPassengerID function"""
        cursor = self.db.get_cursor()
        query = "SELECT getPassengerID(%s, %s) as PassengerID"
        cursor.execute(query, (first_name, last_name))
        return cursor.fetchone()
    
class Trip:
    def __init__(self, db):
        self.db = db

    def add_trip(self, vessel_name, passenger_first_name, passenger_last_name, date, departure_time, length_in_hours, total_passengers):
        """Add a trip using the addTrip stored procedure"""
        cursor = self.db.get_cursor()
        cursor.callproc('addTrip', (vessel_name, passenger_first_name, passenger_last_name, 
                                    date, departure_time, length_in_hours, total_passengers))
        self.db.commit()
        # Fetch the result to check for errors (returns -1, -2, -3 for not found, 0 for duplicate)
        for result in cursor.stored_results():
            return result.fetchone()

    def get_trips(self):
        """Get all trips using the getTripList stored procedure (returns formatted view)"""
        cursor = self.db.get_cursor()
        cursor.callproc('getTripList')
        # Fetch results from the stored procedure
        for result in cursor.stored_results():
            return result.fetchall()
