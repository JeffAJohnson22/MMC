from config import config
from DAL import DatabaseConnection
from BLL import VesselBLL, PassengerBLL, TripBLL
import time

def print_section(title):
    print("\n" + "-"*20)
    print(f"{title}")
    print("-"*20)

if __name__ == "__main__":
    print_section("Welcome to the Program for One Piece Industries")
    
    print("\nEnter database connection information (press Enter for defaults):")
    host = input(f"Host [{config['host']}]: ").strip() or config['host']
    username = input(f"Username [{config['username']}]: ").strip() or config['username']
    password = input(f"Password: ").strip() or config['password']
    database = input(f"Database [{config['database']}]: ").strip() or config['database']
    
    # Connect to database
    print("\nConnecting to database")
    db = DatabaseConnection(host, username, password, database)
    
    if not db.connect():
        print(" Connection didnt work!")
        exit(1)
    
    print("Connected worked")
    
    # Create BLL instances
    vessel_bll = VesselBLL(db)
    passenger_bll = PassengerBLL(db)
    trip_bll = TripBLL(db)
    
    # -------------------------- TOTAL REVENUE REPORT --------------------------
    print_section("TOTAL REVENUE BY VESSEL")
    
    revenue_data = trip_bll.get_revenue_by_vessel()
    if revenue_data:
        for row in revenue_data:
            print(f"\n{row['Vessel Name']}: {row['Revenue']}")
    time.sleep(1)
    
    # -------------------------- VESSEL LOOKUP TEST --------------------------
    print_section("VESSEL ID LOOKUP TEST")
    
    print("\nLooking up vessel: 'Ocean Voyager'")
    result = vessel_bll.get_vessel_id_by_name("Ocean Voyager")
    if result and result.get('VesselID', -1) != -1:
        print(f"Found - Vessel ID: {result['VesselID']}")
    else:
        print("Not found")
    
    print("\nLooking up vessel: 'Going Merry'")
    result = vessel_bll.get_vessel_id_by_name("Going Merry")
    if result and result.get('VesselID', -1) != -1:
        print(f"Found - Vessel ID: {result['VesselID']}")
    else:
        print("Not found - This vessel does not exist in the database")
    time.sleep(1)
    
    # -------------------------- ADD NEW TRIP WITH NEW VESSEL AND PASSENGER --------------------------
    print_section("ADDING COMPLETE NEW TRIP")
    
    print("\nStep 1: Adding new vessel 'Thousand Sunny'")
    vessel_result = vessel_bll.add_vessel("Thousand Sunny", 300.00)
    if vessel_result and 'VesselID' in vessel_result:
        print(f" Vessel added with ID: {vessel_result['VesselID']}")
    else:
        print(" Vessel already exists")
    
    print("\nStep 2: Adding new passenger 'Monkey D. Luffy' (413-555-7777)")
    passenger_result = passenger_bll.add_passenger("Monkey", "D. Luffy", "413-555-7777")
    if passenger_result and 'PassengerID' in passenger_result:
        print(f" Passenger added with ID: {passenger_result['PassengerID']}")
    else:
        print(" Passenger already exists")
    
    print("\nStep 3: Adding trip with new vessel and passenger on 2025-12-20 at 16:00")
    trip_result = trip_bll.add_trip("Thousand Sunny", "Monkey", "D. Luffy", "2025-12-20", "16:00:00", 4.0, 6)
    if trip_result and 'error' in trip_result:
        print(f" Error: {trip_result['error']}")
    elif trip_result and 'DuplicateTrip' in trip_result:
        print(" Duplicate trip detected")
    elif trip_result and 'NotFound' in trip_result:
        print(" Error: Vessel or passenger not found")
    else:
        print(" Trip successfully added and committed to database!")
    time.sleep(1)
    
    # -------------------------- ALL TRIPS VIEW --------------------------
    print_section("ALL TRIPS (Including New Trip)")
    
    all_trips = trip_bll.get_all_trips()
    if all_trips:
        print(f"\nTotal trips in database: {len(all_trips)}\n")
        for trip in all_trips:
            print(f"Date/Time: {trip['Date and Time']}")
            print(f"  Vessel: {trip['Vessel Name']}")
            print(f"  Passenger: {trip['Passenger Name']}")
            print(f"  Address: {trip['Passenger Address']}")
            print(f"  Phone: {trip['Passenger Phone']}")
            print(f"  Duration: {trip['Trip Duration']} hours")
            print(f"  Cost: {trip['Total Cost']}")
            print()
    else:
        print("\nNo trips found.")
    time.sleep(1)
    db.close()
    print("\n Finished and db closed.")
