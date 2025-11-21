"""
Business Logic Layer (BLL) for MRC Database Application
Manages flow between View and DAL, handles business logic and validation
"""

from typing import List, Dict, Any, Optional, Tuple
from datetime import datetime
import re
from DAL import DatabaseConnection, VesselDAL, PassengerDAL, TripDAL


class VesselBLL:
    """
    Business Logic Layer for Vessel operations.
    Handles validation and business rules for vessel management.
    """
    
    def __init__(self, db_connection: DatabaseConnection):
        """
        Initialize VesselBLL with a database connection.
        
        Args:
            db_connection: DatabaseConnection instance
        """
        self.vessel_dal = VesselDAL(db_connection)
    
    def get_all_vessels(self) -> List[Dict[str, Any]]:
        """
        Retrieve all vessels from the database.
        
        Returns:
            List of dictionaries containing vessel data
        """
        return self.vessel_dal.get_all_vessels()
    
    def add_vessel(self, vessel_name: str, cost_per_hour: float) -> Dict[str, Any]:
        """
        Add a new vessel with validation.
        
        Args:
            vessel_name: Name of the vessel
            cost_per_hour: Hourly rental cost
        
        Returns:
            Dictionary with success status, message, and vessel_id if successful
        """
        # Validate vessel name
        if not vessel_name or not vessel_name.strip():
            return {
                'success': False,
                'message': 'Vessel name cannot be empty',
                'vessel_id': -1
            }
        
        vessel_name = vessel_name.strip()
        
        if len(vessel_name) > 100:
            return {
                'success': False,
                'message': 'Vessel name must be 100 characters or less',
                'vessel_id': -1
            }
        
        # Validate cost per hour
        try:
            cost = float(cost_per_hour)
            if cost <= 0:
                return {
                    'success': False,
                    'message': 'Cost per hour must be greater than zero',
                    'vessel_id': -1
                }
            if cost > 10000:
                return {
                    'success': False,
                    'message': 'Cost per hour seems unreasonably high (max: $10,000)',
                    'vessel_id': -1
                }
        except (ValueError, TypeError):
            return {
                'success': False,
                'message': 'Cost per hour must be a valid number',
                'vessel_id': -1
            }
        
        # Check for duplicate vessel name
        existing_vessels = self.vessel_dal.get_all_vessels()
        for vessel in existing_vessels:
            if vessel['Name'].lower() == vessel_name.lower():
                return {
                    'success': False,
                    'message': f'Vessel "{vessel_name}" already exists',
                    'vessel_id': -1
                }
        
        # Add vessel via DAL
        vessel_id = self.vessel_dal.add_vessel(vessel_name, cost)
        
        if vessel_id > 0:
            return {
                'success': True,
                'message': f'Vessel "{vessel_name}" added successfully',
                'vessel_id': vessel_id
            }
        else:
            return {
                'success': False,
                'message': 'Failed to add vessel to database',
                'vessel_id': -1
            }
    
    def get_vessel_by_id(self, vessel_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific vessel by ID.
        
        Args:
            vessel_id: ID of the vessel
        
        Returns:
            Dictionary containing vessel data or None if not found
        """
        try:
            vessel_id = int(vessel_id)
            return self.vessel_dal.get_vessel_by_id(vessel_id)
        except (ValueError, TypeError):
            return None
    
    def delete_vessel(self, vessel_id: int) -> Dict[str, Any]:
        """
        Delete a vessel with validation.
        
        Args:
            vessel_id: ID of the vessel to delete
        
        Returns:
            Dictionary with success status and message
        """
        try:
            vessel_id = int(vessel_id)
        except (ValueError, TypeError):
            return {
                'success': False,
                'message': 'Invalid vessel ID'
            }
        
        # Check if vessel exists
        vessel = self.vessel_dal.get_vessel_by_id(vessel_id)
        if not vessel:
            return {
                'success': False,
                'message': 'Vessel not found'
            }
        
        vessel_name = vessel['Name']
        
        # Attempt to delete
        success = self.vessel_dal.delete_vessel(vessel_id)
        
        if success:
            return {
                'success': True,
                'message': f'Vessel "{vessel_name}" deleted successfully'
            }
        else:
            return {
                'success': False,
                'message': f'Failed to delete vessel "{vessel_name}". It may have associated trips.'
            }
    
    def get_vessel_count(self) -> int:
        """
        Get the total number of vessels.
        
        Returns:
            int: Number of vessels
        """
        vessels = self.vessel_dal.get_all_vessels()
        return len(vessels)
    
    def get_vessel_id_by_name(self, vessel_name: str) -> int:
        """
        Get vessel ID by name.
        
        Args:
            vessel_name: Name of the vessel
        
        Returns:
            int: Vessel ID if found, -1 if not found
        """
        if not vessel_name or not vessel_name.strip():
            return -1
        
        return self.vessel_dal.get_vessel_id_by_name(vessel_name.strip())
    
    def get_total_revenue_by_vessel(self) -> List[Dict[str, Any]]:
        """
        Get total revenue by vessel from the database view.
        
        Returns:
            List of dictionaries containing vessel revenue data
        """
        return self.vessel_dal.get_total_revenue_by_vessel()


class PassengerBLL:
    """
    Business Logic Layer for Passenger operations.
    Handles validation and business rules for passenger management.
    """
    
    def __init__(self, db_connection: DatabaseConnection):
        """
        Initialize PassengerBLL with a database connection.
        
        Args:
            db_connection: DatabaseConnection instance
        """
        self.passenger_dal = PassengerDAL(db_connection)
    
    def get_all_passengers(self) -> List[Dict[str, Any]]:
        """
        Retrieve all passengers from the database.
        
        Returns:
            List of dictionaries containing passenger data
        """
        return self.passenger_dal.get_all_passengers()
    
    def add_passenger(self, first_name: str, last_name: str, phone: str) -> Dict[str, Any]:
        """
        Add a new passenger with validation.
        
        Args:
            first_name: Passenger's first name
            last_name: Passenger's last name
            phone: Passenger's phone number
        
        Returns:
            Dictionary with success status, message, and passenger_id if successful
        """
        # Validate first name
        if not first_name or not first_name.strip():
            return {
                'success': False,
                'message': 'First name cannot be empty',
                'passenger_id': -1
            }
        
        first_name = first_name.strip()
        
        if len(first_name) > 50:
            return {
                'success': False,
                'message': 'First name must be 50 characters or less',
                'passenger_id': -1
            }
        
        # Validate last name
        if not last_name or not last_name.strip():
            return {
                'success': False,
                'message': 'Last name cannot be empty',
                'passenger_id': -1
            }
        
        last_name = last_name.strip()
        
        if len(last_name) > 50:
            return {
                'success': False,
                'message': 'Last name must be 50 characters or less',
                'passenger_id': -1
            }
        
        # Validate phone number
        if not phone or not phone.strip():
            return {
                'success': False,
                'message': 'Phone number cannot be empty',
                'passenger_id': -1
            }
        
        phone = phone.strip()
        
        # Basic phone validation - allow various formats
        phone_pattern = re.compile(r'^[\d\s\-\(\)\+\.]+$')
        if not phone_pattern.match(phone):
            return {
                'success': False,
                'message': 'Phone number contains invalid characters',
                'passenger_id': -1
            }
        
        if len(phone) < 7 or len(phone) > 20:
            return {
                'success': False,
                'message': 'Phone number must be between 7 and 20 characters',
                'passenger_id': -1
            }
        
        # Check for duplicate passenger
        existing_passengers = self.passenger_dal.get_all_passengers()
        for passenger in existing_passengers:
            if (passenger['FirstName'].lower() == first_name.lower() and 
                passenger['LastName'].lower() == last_name.lower() and
                passenger['Phone'] == phone):
                return {
                    'success': False,
                    'message': f'Passenger "{first_name} {last_name}" with this phone number already exists',
                    'passenger_id': -1
                }
        
        # Add passenger via DAL
        passenger_id = self.passenger_dal.add_passenger(first_name, last_name, phone)
        
        if passenger_id > 0:
            return {
                'success': True,
                'message': f'Passenger "{first_name} {last_name}" added successfully',
                'passenger_id': passenger_id
            }
        else:
            return {
                'success': False,
                'message': 'Failed to add passenger to database',
                'passenger_id': -1
            }
    
    def get_passenger_by_id(self, passenger_id: int) -> Optional[Dict[str, Any]]:
        """
        Retrieve a specific passenger by ID.
        
        Args:
            passenger_id: ID of the passenger
        
        Returns:
            Dictionary containing passenger data or None if not found
        """
        try:
            passenger_id = int(passenger_id)
            return self.passenger_dal.get_passenger_by_id(passenger_id)
        except (ValueError, TypeError):
            return None
    
    def delete_passenger(self, passenger_id: int) -> Dict[str, Any]:
        """
        Delete a passenger with validation.
        
        Args:
            passenger_id: ID of the passenger to delete
        
        Returns:
            Dictionary with success status and message
        """
        try:
            passenger_id = int(passenger_id)
        except (ValueError, TypeError):
            return {
                'success': False,
                'message': 'Invalid passenger ID'
            }
        
        # Check if passenger exists
        passenger = self.passenger_dal.get_passenger_by_id(passenger_id)
        if not passenger:
            return {
                'success': False,
                'message': 'Passenger not found'
            }
        
        passenger_name = f"{passenger['FirstName']} {passenger['LastName']}"
        
        # Attempt to delete
        success = self.passenger_dal.delete_passenger(passenger_id)
        
        if success:
            return {
                'success': True,
                'message': f'Passenger "{passenger_name}" deleted successfully'
            }
        else:
            return {
                'success': False,
                'message': f'Failed to delete passenger "{passenger_name}". They may have associated trips.'
            }
    
    def get_passenger_count(self) -> int:
        """
        Get the total number of passengers.
        
        Returns:
            int: Number of passengers
        """
        passengers = self.passenger_dal.get_all_passengers()
        return len(passengers)
    
    def search_passengers(self, search_term: str) -> List[Dict[str, Any]]:
        """
        Search passengers by name or phone number.
        
        Args:
            search_term: Term to search for
        
        Returns:
            List of matching passengers
        """
        if not search_term or not search_term.strip():
            return self.get_all_passengers()
        
        search_term = search_term.strip().lower()
        all_passengers = self.get_all_passengers()
        
        matching_passengers = []
        for passenger in all_passengers:
            # Search in first name, last name, or phone
            if (search_term in passenger['FirstName'].lower() or
                search_term in passenger['LastName'].lower() or
                search_term in passenger['Phone']):
                matching_passengers.append(passenger)
        
        return matching_passengers


class TripBLL:
    """
    Business Logic Layer for Trip operations.
    Handles validation and business rules for trip management.
    """
    
    def __init__(self, db_connection: DatabaseConnection):
        """
        Initialize TripBLL with a database connection.
        
        Args:
            db_connection: DatabaseConnection instance
        """
        self.trip_dal = TripDAL(db_connection)
        self.vessel_dal = VesselDAL(db_connection)
        self.passenger_dal = PassengerDAL(db_connection)
    
    def get_all_trips(self) -> List[Dict[str, Any]]:
        """
        Retrieve all trips from the database.
        
        Returns:
            List of dictionaries containing trip data
        """
        return self.trip_dal.get_all_trips()
    
    def add_trip(self, vessel_name: str, passenger_first_name: str, 
                 passenger_last_name: str, trip_date: str, departure_time: str,
                 length_in_hours: float, total_passengers: int) -> Dict[str, Any]:
        """
        Add a new trip with validation.
        
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
        # Validate vessel name
        if not vessel_name or not vessel_name.strip():
            return {
                'success': False,
                'message': 'Vessel name cannot be empty'
            }
        
        vessel_name = vessel_name.strip()
        
        # Validate passenger name
        if not passenger_first_name or not passenger_first_name.strip():
            return {
                'success': False,
                'message': 'Passenger first name cannot be empty'
            }
        
        if not passenger_last_name or not passenger_last_name.strip():
            return {
                'success': False,
                'message': 'Passenger last name cannot be empty'
            }
        
        passenger_first_name = passenger_first_name.strip()
        passenger_last_name = passenger_last_name.strip()
        
        # Validate date
        try:
            date_obj = datetime.strptime(trip_date, '%Y-%m-%d')
            
            # Don't allow trips more than 1 year in the past or 2 years in the future
            today = datetime.now()
            min_date = datetime(today.year - 1, today.month, today.day)
            max_date = datetime(today.year + 2, today.month, today.day)
            
            if date_obj < min_date:
                return {
                    'success': False,
                    'message': 'Trip date cannot be more than 1 year in the past'
                }
            
            if date_obj > max_date:
                return {
                    'success': False,
                    'message': 'Trip date cannot be more than 2 years in the future'
                }
        except ValueError:
            return {
                'success': False,
                'message': 'Invalid date format. Use YYYY-MM-DD'
            }
        
        # Validate time
        try:
            datetime.strptime(departure_time, '%H:%M:%S')
        except ValueError:
            # Try HH:MM format
            try:
                time_obj = datetime.strptime(departure_time, '%H:%M')
                departure_time = time_obj.strftime('%H:%M:%S')
            except ValueError:
                return {
                    'success': False,
                    'message': 'Invalid time format. Use HH:MM:SS or HH:MM'
                }
        
        # Validate length in hours
        try:
            hours = float(length_in_hours)
            if hours <= 0:
                return {
                    'success': False,
                    'message': 'Trip length must be greater than zero hours'
                }
            if hours > 24:
                return {
                    'success': False,
                    'message': 'Trip length cannot exceed 24 hours'
                }
        except (ValueError, TypeError):
            return {
                'success': False,
                'message': 'Trip length must be a valid number'
            }
        
        # Validate total passengers
        try:
            passengers = int(total_passengers)
            if passengers <= 0:
                return {
                    'success': False,
                    'message': 'Total passengers must be at least 1'
                }
            if passengers > 500:
                return {
                    'success': False,
                    'message': 'Total passengers cannot exceed 500'
                }
        except (ValueError, TypeError):
            return {
                'success': False,
                'message': 'Total passengers must be a valid whole number'
            }
        
        # Add trip via DAL
        result = self.trip_dal.add_trip(
            vessel_name,
            passenger_first_name,
            passenger_last_name,
            trip_date,
            departure_time,
            hours,
            passengers
        )
        
        return result
    
    def get_trips_by_vessel(self, vessel_id: int) -> List[Dict[str, Any]]:
        """
        Retrieve all trips for a specific vessel.
        
        Args:
            vessel_id: ID of the vessel
        
        Returns:
            List of dictionaries containing trip data
        """
        try:
            vessel_id = int(vessel_id)
            return self.trip_dal.get_trips_by_vessel(vessel_id)
        except (ValueError, TypeError):
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
            passenger_id = int(passenger_id)
            return self.trip_dal.get_trips_by_passenger(passenger_id)
        except (ValueError, TypeError):
            return []
    
    def get_trip_count(self) -> int:
        """
        Get the total number of trips.
        
        Returns:
            int: Number of trips
        """
        trips = self.trip_dal.get_all_trips()
        return len(trips)
    
    def calculate_trip_cost(self, vessel_name: str, length_in_hours: float) -> Dict[str, Any]:
        """
        Calculate the cost of a trip based on vessel and duration.
        
        Args:
            vessel_name: Name of the vessel
            length_in_hours: Duration of trip in hours
        
        Returns:
            Dictionary with success status, cost, and message
        """
        if not vessel_name or not vessel_name.strip():
            return {
                'success': False,
                'cost': 0.0,
                'message': 'Vessel name cannot be empty'
            }
        
        try:
            hours = float(length_in_hours)
            if hours <= 0:
                return {
                    'success': False,
                    'cost': 0.0,
                    'message': 'Trip length must be greater than zero'
                }
        except (ValueError, TypeError):
            return {
                'success': False,
                'cost': 0.0,
                'message': 'Invalid trip length'
            }
        
        # Find vessel by name
        vessels = self.vessel_dal.get_all_vessels()
        vessel = None
        for v in vessels:
            if v['Name'].lower() == vessel_name.strip().lower():
                vessel = v
                break
        
        if not vessel:
            return {
                'success': False,
                'cost': 0.0,
                'message': f'Vessel "{vessel_name}" not found'
            }
        
        cost = vessel['CostPerHour'] * hours
        
        return {
            'success': True,
            'cost': round(cost, 2),
            'message': f'Trip cost: ${cost:.2f} ({hours} hours @ ${vessel["CostPerHour"]:.2f}/hour)'
        }
    
    def get_trip_statistics(self) -> Dict[str, Any]:
        """
        Get statistics about all trips.
        
        Returns:
            Dictionary with various statistics
        """
        trips = self.get_all_trips()
        
        if not trips:
            return {
                'total_trips': 0,
                'total_passengers': 0,
                'average_trip_length': 0.0,
                'most_popular_vessel': None
            }
        
        total_passengers = 0
        total_hours = 0.0
        vessel_usage = {}
        
        for trip in trips:
            total_passengers += trip.get('TotalPassengers', 0)
            total_hours += trip.get('LengthInHours', 0.0)
            
            vessel_name = trip.get('VesselName', 'Unknown')
            vessel_usage[vessel_name] = vessel_usage.get(vessel_name, 0) + 1
        
        most_popular_vessel = max(vessel_usage, key=vessel_usage.get) if vessel_usage else None
        average_trip_length = total_hours / len(trips) if trips else 0.0
        
        return {
            'total_trips': len(trips),
            'total_passengers': total_passengers,
            'average_trip_length': round(average_trip_length, 2),
            'most_popular_vessel': most_popular_vessel,
            'vessel_usage': vessel_usage
        }


# Example usage and testing
if __name__ == "__main__":
    print("=== Testing BLL Classes ===\n")
    
    # Update these connection parameters as needed
    db_config = {
        'host': 'localhost',
        'user': 'root',
        'password': '',  # Add your password here
        'database': 'mrc'
    }
    
    with DatabaseConnection(**db_config) as db:
        # Test VesselBLL
        print("--- Testing Vessel BLL ---")
        vessel_bll = VesselBLL(db)
        
        print(f"Total vessels: {vessel_bll.get_vessel_count()}")
        
        # Test adding a vessel with validation
        result = vessel_bll.add_vessel("Test Vessel", 150.00)
        print(f"Add vessel result: {result}")
        
        # Test PassengerBLL
        print("\n--- Testing Passenger BLL ---")
        passenger_bll = PassengerBLL(db)
        
        print(f"Total passengers: {passenger_bll.get_passenger_count()}")
        
        # Test adding a passenger with validation
        result = passenger_bll.add_passenger("John", "Doe", "555-1234")
        print(f"Add passenger result: {result}")
        
        # Test TripBLL
        print("\n--- Testing Trip BLL ---")
        trip_bll = TripBLL(db)
        
        print(f"Total trips: {trip_bll.get_trip_count()}")
        
        # Test trip statistics
        stats = trip_bll.get_trip_statistics()
        print(f"Trip statistics: {stats}")
        
        # Test cost calculation
        cost_result = trip_bll.calculate_trip_cost("Test Vessel", 3.5)
        print(f"Cost calculation: {cost_result}")
