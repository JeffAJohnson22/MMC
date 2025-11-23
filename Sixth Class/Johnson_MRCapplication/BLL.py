from DAL import Vessel, Passenger, Trip

class VesselBLL:    
    def __init__(self, db):
        self.vessel_dal = Vessel(db)
    
    def add_vessel(self, vessel_name, cost_per_hour):
        """Add a vessel with validation"""
        if not vessel_name or not isinstance(vessel_name, str):
            return {"error": "Invalid vessel name"}
        if cost_per_hour is None or cost_per_hour < 0:
            return {"error": "Invalid cost per hour"}
        
        result = self.vessel_dal.add_vessel(vessel_name, cost_per_hour)
        return result
    
    def get_all_vessels(self):
        """Get all vessels"""
        return self.vessel_dal.get_vessels()
    
    def get_vessel_id_by_name(self, vessel_name):
        """Get vessel ID by name"""
        if not vessel_name:
            return {"error": "Vessel name required"}
        
        result = self.vessel_dal.get_vessel_id(vessel_name)
        return result


class PassengerBLL:    
    def __init__(self, db):
        self.passenger_dal = Passenger(db)
    
    def add_passenger(self, first_name, last_name, phone):
        """Add a passenger with validation"""
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
    
    def get_passenger_id_by_name(self, first_name, last_name):
        """Get passenger ID by name"""
        if not first_name or not last_name:
            return {"error": "First and last name required"}
        
        result = self.passenger_dal.get_passenger_id(first_name, last_name)
        return result

class TripBLL:
    def __init__(self, db):
        self.trip_dal = Trip(db)
    
    def add_trip(self, vessel_name, passenger_first_name, passenger_last_name, 
                 date, departure_time, length_in_hours, total_passengers):
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
    
    def get_revenue_by_vessel(self):
        """Get revenue by vessel"""
        return self.trip_dal.get_revenue_by_vessel()
