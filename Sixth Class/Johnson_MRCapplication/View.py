from config import config
from DAL import DatabaseConnection
from BLL import VesselBLL, PassengerBLL, TripBLL
import time

def print_section(title):
    """Helper function to print section headers"""
    print("\n" + "-"*20)
    print(f"{title}")
    print("-"*20)

if __name__ == "__main__":
    print_section("Merrimack River Cruises - Database Demo")
    
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
    
    # ==================== DISPLAY INITIAL DATA ====================
    print_section("INITIAL DATA")
    
    print("\nVessels:")
    vessels = vessel_bll.get_all_vessels()
    if vessels:
        for v in vessels:
            print(f"  {v['ID']}: {v['Vessel']} (${v['Cost_Per_Hour']}/hr)")
    
    print("\nPassengers:")
    passengers = passenger_bll.get_all_passengers()
    if passengers:
        for p in passengers:
            print(f"  {p['ID']}: {p['First_Name']} {p['Last_Name']}")
    
    print("\nTrips:")
    trips = trip_bll.get_all_trips()
    if trips:
        for t in trips:
            print(f"  {t['Date and Time']} - {t['Vessel Name']} - {t['Passenger Name']}")
    
    time.sleep(1) ## this paused the info stream to read it
    
    # -------------------------- DEMO OPERATIONS --------------------------
    print_section("DEMO OPERATIONS")
    
    print("\nAdding vessel: Harbor Queen - $175/hr")
    result = vessel_bll.add_vessel("Harbor Queen", 175.00)
    print(f" Added with ID: {result.get('VesselID')}" if result and 'VesselID' in result else "  Already exists")
    
    print("\nAdding passenger: Alice Johnson")
    result = passenger_bll.add_passenger("Alice", "Johnson", "978-555-9999")
    print(f" Added with ID: {result.get('PassengerID')}" if result and 'PassengerID' in result else "  Already exists")
    
    print("\nLooking up 'Sea Breeze'...")
    result = vessel_bll.get_vessel_id_by_name("Sea Breeze")
    print(f" Vessel ID: {result['VesselID']}" if result and result.get('VesselID', -1) != -1 else "  Not found")
    
    print("\nAdding trip: Sea Breeze with Alice Johnson on 2025-12-15")
    result = trip_bll.add_trip("Sea Breeze", "Alice", "Johnson", "2025-12-15", "14:00:00", 3.5, 4)
    if result and 'error' in result:
        print(f" {result['error']}")
    elif result and 'DuplicateTrip' in result:
        print(" Duplicate trip")
    elif result and 'NotFound' in result:
        print(" Vessel or passenger not found")
    else:
        print(" Trip added")
    time.sleep(1)
    # -------------------------- FINAL STATE --------------------------
    print_section("FINAL DATA")
    
    print(f"\nVessels: {len(vessel_bll.get_all_vessels() or [])}")
    print(f"Passengers: {len(passenger_bll.get_all_passengers() or [])}")
    print(f"Trips: {len(trip_bll.get_all_trips() or [])}")
    time.sleep(1)
    # -------------------------- REVENUE REPORT --------------------------
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
    
    print("\nLooking up vessel: 'Titanic'")
    result = vessel_bll.get_vessel_id_by_name("Titanic")
    if result and result.get('VesselID', -1) != -1:
        print(f"Found - Vessel ID: {result['VesselID']}")
    else:
        print("Not found - This vessel does not exist in the database")
    time.sleep(1)
    # -------------------------- ADD NEW TRIP WITH NEW VESSEL AND PASSENGER --------------------------
    print_section("ADDING COMPLETE NEW TRIP")
    
    print("\nStep 1: Adding new vessel 'A Saiyans Pride")
    vessel_result = vessel_bll.add_vessel("A Saiyans Pride", 300.00)
    if vessel_result and 'VesselID' in vessel_result:
        print(f" Vessel added with ID: {vessel_result['VesselID']}")
    else:
        print(" Vessel already exists")
    
    print("\nStep 2: Adding new passenger 'Goku Son' (413-555-7777)")
    passenger_result = passenger_bll.add_passenger("Goku", "Son", "413-555-7777")
    if passenger_result and 'PassengerID' in passenger_result:
        print(f" Passenger added with ID: {passenger_result['PassengerID']}")
    else:
        print(" Passenger already exists")
    
    print("\nStep 3: Adding trip with new vessel and passenger on 2025-12-20 at 16:00")
    trip_result = trip_bll.add_trip("A Saiyans Pride", "Goku", "Son", "2025-12-20", "16:00:00", 4.0, 6)
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
