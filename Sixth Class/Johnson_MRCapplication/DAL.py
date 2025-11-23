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
        if self.connection and self.connection.is_connected():
            return self.connection.cursor(dictionary=True)
        else:
            raise Exception("Database not connected")

    def commit(self):
        if self.connection and self.connection.is_connected():
            self.connection.commit()
        else:
            raise Exception("Not connected")

    def close(self):
        if self.connection and self.connection.is_connected():
            self.connection.close()
            self.connection = None 

class Vessel:
    def __init__(self, db):
        self.db = db

    def add_vessel(self, vessel_name, cost_per_hour):
        cursor = self.db.get_cursor()
        cursor.callproc('addVessel', (vessel_name, cost_per_hour))
        self.db.commit()
        for result in cursor.stored_results():
            return result.fetchone()

    def get_vessels(self):
        cursor = self.db.get_cursor()
        cursor.callproc('getVesselList')
        for result in cursor.stored_results():
            return result.fetchall()
    
    def delete_vessel(self, vessel_id):
        cursor = self.db.get_cursor()
        cursor.callproc('deleteVessel', (vessel_id,))
        self.db.commit()
        for result in cursor.stored_results():
            return result.fetchone()
    
    def get_vessel_id(self, vessel_name):
        cursor = self.db.get_cursor()
        query = "SELECT getVesselID(%s) as VesselID"
        cursor.execute(query, (vessel_name,))
        return cursor.fetchone()

class Passenger:
    def __init__(self, db):
        self.db = db

    def add_passenger(self, first_name, last_name, phone):
        cursor = self.db.get_cursor()
        cursor.callproc('addPassenger', (first_name, last_name, phone))
        self.db.commit()
        for result in cursor.stored_results():
            return result.fetchone()

    def get_passengers(self):
        cursor = self.db.get_cursor()
        cursor.callproc('getPassengerList')
        for result in cursor.stored_results():
            return result.fetchall()
    
    def delete_passenger(self, passenger_id):
        cursor = self.db.get_cursor()
        cursor.callproc('deletePassenger', (passenger_id,))
        self.db.commit()
        for result in cursor.stored_results():
            return result.fetchone()
    
    def get_passenger_id(self, first_name, last_name):
        cursor = self.db.get_cursor()
        query = "SELECT getPassengerID(%s, %s) as PassengerID"
        cursor.execute(query, (first_name, last_name))
        return cursor.fetchone()
    
class Trip:
    def __init__(self, db):
        self.db = db

    def add_trip(self, vessel_name, passenger_first_name, passenger_last_name, date, departure_time, length_in_hours, total_passengers):
        cursor = self.db.get_cursor()
        cursor.callproc('addTrip', (vessel_name, passenger_first_name, passenger_last_name, 
                                    date, departure_time, length_in_hours, total_passengers))
        self.db.commit()
        for result in cursor.stored_results():
            return result.fetchone()

    def get_trips(self):
        cursor = self.db.get_cursor()
        cursor.callproc('getTripList')
        for result in cursor.stored_results():
            return result.fetchall()
    
    def get_revenue_by_vessel(self):
        cursor = self.db.get_cursor()
        query = "SELECT * FROM `total revenue by vessel`"
        cursor.execute(query)
        return cursor.fetchall()
