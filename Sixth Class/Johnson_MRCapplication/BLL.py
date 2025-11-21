# Business Logic Layer - Handles business logic and calls DAL methods
from DAL import DatabaseConnection, Vessel, Passenger, Trip
from config import config

class VesselBLL:
    """Business Logic Layer for Vessel operations"""
    
    def __init__(self, db):
        self.vessel_dal = Vessel(db)
    
    def add_vessel(self, vessel_name, cost_per_hour):
        """Add a new vessel with validation"""
        if not vessel_name or not isinstance(vessel_name, str):
            return {"error": "Invalid vessel name"}
        if cost_per_hour is None or cost_per_hour < 0:
            return {"error": "Invalid cost per hour"}
        
        result = self.vessel_dal.add_vessel(vessel_name, cost_per_hour)
        return result
    
    def get_all_vessels(self):
        """Get all vessels"""
        return self.vessel_dal.get_vessels()
    
    def delete_vessel(self, vessel_id):
        """Delete a vessel by ID"""
        if not isinstance(vessel_id, int) or vessel_id <= 0:
            return {"error": "Invalid vessel ID"}
        
        result = self.vessel_dal.delete_vessel(vessel_id)
        return result
    
    def get_vessel_id_by_name(self, vessel_name):
        """Get vessel ID by name"""
        if not vessel_name:
            return {"error": "Vessel name required"}
        
        result = self.vessel_dal.get_vessel_id(vessel_name)
        return result


class PassengerBLL:
    """Business Logic Layer for Passenger operations"""
    
    def __init__(self, db):
        self.passenger_dal = Passenger(db)
    
    def add_passenger(self, first_name, last_name, phone):
        """Add a new passenger with validation"""
        if not first_name or not isinstance(first_name, str):
            return {"error": "Invalid first name"}
        if not last_name or not isinstance(last_name, str):
            return {"error": "Invalid last name"}
        if not phone or not isinstance(phone, str):
            return {"error": "Invalid phone number"}
        
        result = self.passenger_dal.add_passenger(first_name, last_name, phone)
        return result
    
    def get_all_passengers(self):
        """Get all passengers"""
        return self.passenger_dal.get_passengers()
    
    def delete_passenger(self, passenger_id):
        """Delete a passenger by ID"""
        if not isinstance(passenger_id, int) or passenger_id <= 0:
            return {"error": "Invalid passenger ID"}
        
        result = self.passenger_dal.delete_passenger(passenger_id)
        return result
    
    def get_passenger_id_by_name(self, first_name, last_name):
        """Get passenger ID by name"""
        if not first_name or not last_name:
            return {"error": "First and last name required"}
        
        result = self.passenger_dal.get_passenger_id(first_name, last_name)
        return result


class TripBLL:
    """Business Logic Layer for Trip operations"""
    
    def __init__(self, db):
        self.trip_dal = Trip(db)
    
    def add_trip(self, vessel_name, passenger_first_name, passenger_last_name, 
                 date, departure_time, length_in_hours, total_passengers):
        """Add a new trip with validation"""
        if not vessel_name or not isinstance(vessel_name, str):
            return {"error": "Invalid vessel name"}
        if not passenger_first_name or not isinstance(passenger_first_name, str):
            return {"error": "Invalid passenger first name"}
        if not passenger_last_name or not isinstance(passenger_last_name, str):
            return {"error": "Invalid passenger last name"}
        if not date:
            return {"error": "Date required"}
        if not departure_time:
            return {"error": "Departure time required"}
        if length_in_hours is None or length_in_hours <= 0:
            return {"error": "Invalid trip length"}
        if not isinstance(total_passengers, int) or total_passengers <= 0:
            return {"error": "Invalid total passengers"}
        
        result = self.trip_dal.add_trip(vessel_name, passenger_first_name, passenger_last_name,
                                       date, departure_time, length_in_hours, total_passengers)
        
        # Handle stored procedure return codes
        if result:
            if 'NotFound' in result:
                error_code = result['NotFound']
                if error_code == -1:
                    return {"error": "Vessel not found"}
                elif error_code == -2:
                    return {"error": "Passenger not found"}
                elif error_code == -3:
                    return {"error": "Both vessel and passenger not found"}
            elif 'DuplicateTrip' in result:
                return {"error": "Duplicate trip - this trip already exists"}
        
        return result
    
    def get_all_trips(self):
        """Get all trips"""
        return self.trip_dal.get_trips()


# Example usage (for testing)
if __name__ == "__main__":
    # Connect to database
    db = DatabaseConnection(config['host'], config['username'], config['password'], config['database'])
    
    if db.connect():
        print("Connected to mrc database!")
        
        # Create BLL instances
        vessel_bll = VesselBLL(db)
        passenger_bll = PassengerBLL(db)
        trip_bll = TripBLL(db)
        
        # Main loop
        while True:
            choice = input("\nEnter 'vessels' to get all vessels, 'passengers' to get all passengers, 'trips' to get all trips, or 'exit' to quit: ").strip().lower()
            
            if choice == 'vessels':
                print("\n--- All Vessels ---")
                vessels = vessel_bll.get_all_vessels()
                if vessels:
                    for vessel in vessels:
                        print(vessel)
            elif choice == 'passengers':
                print("\n--- All Passengers ---")
                passengers = passenger_bll.get_all_passengers()
                if passengers:
                    for passenger in passengers:
                        print(passenger)
            elif choice == 'trips':
                print("\n--- All Trips ---")
                trips = trip_bll.get_all_trips()
                if trips:
                    for trip in trips:
                        print(trip)
            elif choice == 'exit':
                break
            else:
                print("Invalid choice. Please try again.")
        
        # Close connection
        db.close()
        print("Database connection closed!")
    else:
        print("Connection failed!")
