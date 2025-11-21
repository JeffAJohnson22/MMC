"""
Data Access Layer (DAL) for MRC Database Application
Handles all database connections and CRUD operations for Vessels, Passengers, and Trips
"""

import mysql.connector
from mysql.connector import Error
from typing import List, Tuple, Optional, Dict, Any


class DatabaseConnection:
    """
    Manages database connections, cursors, commits, and closures.
    Provides context manager support for automatic resource cleanup.
    """
    
    def __init__(self, host: str = "localhost", user: str = "root", 
                 password: str = "", database: str = "mrc"):
        """
        Initialize database connection parameters.
        
        Args:
            host: Database host address
            user: Database username
            password: Database password
            database: Database name
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None
    
    def connect(self) -> bool:
        """
        Establish connection to the database.
        
        Returns:
            bool: True if connection successful, False otherwise
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                self.cursor = self.connection.cursor(dictionary=True)
                return True
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return False
    
    def get_cursor(self):
        """
        Get the database cursor.
        
        Returns:
            cursor: MySQL cursor object
        """
        if not self.cursor:
            self.connect()
        return self.cursor
    
    def commit(self):
        """Commit the current transaction."""
        if self.connection:
            self.connection.commit()
    
    def rollback(self):
        """Rollback the current transaction."""
        if self.connection:
            self.connection.rollback()
    
    def close(self):
        """Close cursor and connection."""
        if self.cursor:
            self.cursor.close()
        if self.connection and self.connection.is_connected():
            self.connection.close()
    
    def __enter__(self):
        """Context manager entry - establish connection."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close connection."""
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.close()


class VesselDAL:
    """
    Data Access Layer for Vessels table.
    Handles all database operations related to vessels.
    """
    
    def __init__(self, db_connection: DatabaseConnection):
        """
        Initialize VesselDAL with a database connection.
        
        Args:
            db_connection: DatabaseConnection instance
        """
        self.db = db_connection
    
    def get_all_vessels(self) -> List[Dict[str, Any]]:
        """
        Retrieve all vessels from the database using getVesselList procedure.
        
        Returns:
            List of dictionaries containing vessel data
        """
        try:
            cursor = self.db.get_cursor()
            cursor.callproc('getVesselList')
            
            # Fetch results from the stored procedure
            results = []
            for result in cursor.stored_results():
                results = result.fetchall()
            
            return results
        except Error as e:
            print(f"Error retrieving vessels: {e}")
            return []
    
    def add_vessel(self, vessel_name: str, cost_per_hour: float) -> int:
        """
        Add a new vessel to the database using addVessel procedure.
        
        Args:
            vessel_name: Name of the vessel
            cost_per_hour: Hourly rental cost
        
        Returns:
            int: Vessel ID if successful, -1 if failed
        """
        try:
            cursor = self.db.get_cursor()
            cursor.callproc('addVessel', [vessel_name, cost_per_hour])
            
            # Get the vessel ID from the procedure result
            vessel_id = -1
            for result in cursor.stored_results():
                row = result.fetchone()
                if row and 'VesselID' in row:
                    vessel_id = row['VesselID']
            
            self.db.commit()
            return vessel_id
        except Error as e:
            print(f"Error adding vessel: {e}")
            self.db.rollback()
            return -1
    
    def get_vessel_by_id(self, vessel_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific vessel by ID.
        
        Args:
            vessel_id: ID of the vessel
        
        Returns:
            Dictionary containing vessel data or None if not found
        """
        try:
            cursor = self.db.get_cursor()
            query = "SELECT * FROM vessels WHERE ID = %s"
            cursor.execute(query, (vessel_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error retrieving vessel by ID: {e}")
            return None
    
    def delete_vessel(self, vessel_id: int) -> bool:
        """
        Delete a vessel from the database using deleteVessel procedure.
        
        Args:
            vessel_id: ID of the vessel to delete
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            cursor = self.db.get_cursor()
            cursor.callproc('deleteVessel', [vessel_id])
            
            # Check if deletion was successful
            for result in cursor.stored_results():
                row = result.fetchone()
                if row and 'NotFound' in row:
                    return False
            
            self.db.commit()
            return True
        except Error as e:
            print(f"Error deleting vessel: {e}")
            self.db.rollback()
            return False
    
    def get_vessel_id_by_name(self, vessel_name: str) -> int:
        """
        Get vessel ID by name using getVesselId function.
        
        Args:
            vessel_name: Name of the vessel
        
        Returns:
            int: Vessel ID if found, -1 if not found
        """
        try:
            cursor = self.db.get_cursor()
            query = "SELECT getVesselId(%s) AS vessel_id"
            cursor.execute(query, (vessel_name,))
            result = cursor.fetchone()
            
            if result and 'vessel_id' in result:
                return result['vessel_id']
            return -1
        except Error as e:
            print(f"Error getting vessel ID by name: {e}")
            return -1
    
    def get_total_revenue_by_vessel(self) -> List[Dict[str, Any]]:
        """
        Retrieve total revenue by vessel from the 'Total Revenue by Vessel' view.
        
        Returns:
            List of dictionaries containing vessel revenue data
        """
        try:
            cursor = self.db.get_cursor()
            query = "SELECT * FROM `Total Revenue by Vessel`"
            cursor.execute(query)
            return cursor.fetchall()
        except Error as e:
            print(f"Error retrieving total revenue by vessel: {e}")
            return []


class PassengerDAL:
    """
    Data Access Layer for Passengers table.
    Handles all database operations related to passengers.
    """
    
    def __init__(self, db_connection: DatabaseConnection):
        """
        Initialize PassengerDAL with a database connection.
        
        Args:
            db_connection: DatabaseConnection instance
        """
        self.db = db_connection
    
    def get_all_passengers(self) -> List[Dict[str, Any]]:
        """
        Retrieve all passengers from the database using getPassengerList procedure.
        
        Returns:
            List of dictionaries containing passenger data
        """
        try:
            cursor = self.db.get_cursor()
            cursor.callproc('getPassengerList')
            
            # Fetch results from the stored procedure
            results = []
            for result in cursor.stored_results():
                results = result.fetchall()
            
            return results
        except Error as e:
            print(f"Error retrieving passengers: {e}")
            return []
    
    def add_passenger(self, first_name: str, last_name: str, phone: str) -> int:
        """
        Add a new passenger to the database using addPassenger procedure.
        
        Args:
            first_name: Passenger's first name
            last_name: Passenger's last name
            phone: Passenger's phone number
        
        Returns:
            int: Passenger ID if successful, -1 if failed
        """
        try:
            cursor = self.db.get_cursor()
            cursor.callproc('addPassenger', [first_name, last_name, phone])
            
            # Get the passenger ID from the procedure result
            passenger_id = -1
            for result in cursor.stored_results():
                row = result.fetchone()
                if row and 'PassengerID' in row:
                    passenger_id = row['PassengerID']
            
            self.db.commit()
            return passenger_id
        except Error as e:
            print(f"Error adding passenger: {e}")
            self.db.rollback()
            return -1
    
    def get_passenger_by_id(self, passenger_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific passenger by ID.
        
        Args:
            passenger_id: ID of the passenger
        
        Returns:
            Dictionary containing passenger data or None if not found
        """
        try:
            cursor = self.db.get_cursor()
            query = "SELECT * FROM passengers WHERE ID = %s"
            cursor.execute(query, (passenger_id,))
            return cursor.fetchone()
        except Error as e:
            print(f"Error retrieving passenger by ID: {e}")
            return None
    
    def delete_passenger(self, passenger_id: int) -> bool:
        """
        Delete a passenger from the database using deletePassenger procedure.
        
        Args:
            passenger_id: ID of the passenger to delete
        
        Returns:
            bool: True if successful, False otherwise
        """
        try:
            cursor = self.db.get_cursor()
            cursor.callproc('deletePassenger', [passenger_id])
            
            # Check if deletion was successful
            for result in cursor.stored_results():
                row = result.fetchone()
                if row and 'NotFound' in row:
                    return False
            
            self.db.commit()
            return True
        except Error as e:
            print(f"Error deleting passenger: {e}")
            self.db.rollback()
            return False


class TripDAL:
    """
    Data Access Layer for Trips table.
    Handles all database operations related to trips.
    """
    
    def __init__(self, db_connection: DatabaseConnection):
        """
        Initialize TripDAL with a database connection.
        
        Args:
            db_connection: DatabaseConnection instance
        """
        self.db = db_connection
    
    def get_all_trips(self) -> List[Dict[str, Any]]:
        """
        Retrieve all trips from the database using getTripList procedure.
        Returns formatted trip data from the 'All Trips' view.
        
        Returns:
            List of dictionaries containing trip data
        """
        try:
            cursor = self.db.get_cursor()
            cursor.callproc('getTripList')
            
            # Fetch results from the stored procedure
            results = []
            for result in cursor.stored_results():
                results = result.fetchall()
            
            return results
        except Error as e:
            print(f"Error retrieving trips: {e}")
            return []
    
    def add_trip(self, vessel_name: str, passenger_first_name: str, 
                 passenger_last_name: str, trip_date: str, departure_time: str,
                 length_in_hours: float, total_passengers: int) -> Dict[str, Any]:
        """
        Add a new trip to the database using addTrip procedure.
        
        Args:
            vessel_name: Name of the vessel
            passenger_first_name: Passenger's first name
            passenger_last_name: Passenger's last name
            trip_date: Trip date (YYYY-MM-DD format)
            departure_time: Departure time (HH:MM:SS format)
            length_in_hours: Duration of trip in hours
            total_passengers: Total number of passengers on trip
        
        Returns:
            Dictionary with success status and message
        """
        try:
            cursor = self.db.get_cursor()
            cursor.callproc('addTrip', [
                vessel_name, 
                passenger_first_name, 
                passenger_last_name,
                trip_date, 
                departure_time, 
                length_in_hours, 
                total_passengers
            ])
            
            # Check the result from the procedure
            result_data = {'success': True, 'message': 'Trip added successfully'}
            
            for result in cursor.stored_results():
                row = result.fetchone()
                if row:
                    if 'DuplicateTrip' in row and row['DuplicateTrip'] == 0:
                        result_data = {'success': False, 'message': 'Duplicate trip - this trip already exists'}
                    elif 'NotFound' in row:
                        not_found_code = row['NotFound']
                        if not_found_code == -1:
                            result_data = {'success': False, 'message': 'Vessel not found'}
                        elif not_found_code == -2:
                            result_data = {'success': False, 'message': 'Passenger not found'}
                        elif not_found_code == -3:
                            result_data = {'success': False, 'message': 'Both vessel and passenger not found'}
            
            if result_data['success']:
                self.db.commit()
            else:
                self.db.rollback()
            
            return result_data
        except Error as e:
            print(f"Error adding trip: {e}")
            self.db.rollback()
            return {'success': False, 'message': f'Database error: {str(e)}'}
    
    def get_trips_by_vessel(self, vessel_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve all trips for a specific vessel.
        
        Args:
            vessel_id: ID of the vessel
        
        Returns:
            List of dictionaries containing trip data
        """
        try:
            cursor = self.db.get_cursor()
            query = "SELECT * FROM trips WHERE Vessel_ID = %s ORDER BY Date DESC, Departure_Time DESC"
            cursor.execute(query, (vessel_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error retrieving trips by vessel: {e}")
            return []
    
    def get_trips_by_passenger(self, passenger_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve all trips for a specific passenger.
        
        Args:
            passenger_id: ID of the passenger
        
        Returns:
            List of dictionaries containing trip data
        """
        try:
            cursor = self.db.get_cursor()
            query = "SELECT * FROM trips WHERE Passenger_ID = %s ORDER BY Date DESC, Departure_Time DESC"
            cursor.execute(query, (passenger_id,))
            return cursor.fetchall()
        except Error as e:
            print(f"Error retrieving trips by passenger: {e}")
            return []


# Example usage and testing
if __name__ == "__main__":
    # Example: Using context manager for automatic connection handling
    print("=== Testing DAL Classes ===\n")
    
    # Update these connection parameters as needed
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',  # Add your password here
        'database': 'mrc'
    }
    
    with DatabaseConnection(**db_config) as db:
        # Test VesselDAL
        print("--- Testing Vessels ---")
        vessel_dal = VesselDAL(db)
        vessels = vessel_dal.get_all_vessels()
        print(f"Found {len(vessels)} vessels:")
        for vessel in vessels:
            print(f"  - {vessel}")
        
        # Test PassengerDAL
        print("\n--- Testing Passengers ---")
        passenger_dal = PassengerDAL(db)
        passengers = passenger_dal.get_all_passengers()
        print(f"Found {len(passengers)} passengers:")
        for passenger in passengers[:3]:  # Show first 3
            print(f"  - {passenger}")
        
        # Test TripDAL
        print("\n--- Testing Trips ---")
        trip_dal = TripDAL(db)
        trips = trip_dal.get_all_trips()
        print(f"Found {len(trips)} trips:")
        for trip in trips[:3]:  # Show first 3
            print(f"  - {trip}")
