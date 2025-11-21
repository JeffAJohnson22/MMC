# Create a scaffold that gives the user information about what is happening and displays the data. 

from config import config
from DAL import DatabaseConnection
from BLL import VesselBLL, PassengerBLL, TripBLL

def print_section(title):
    """Helper function to print section headers"""
    print("\n" + "="*50)
    print(f"{title}")
    print("="*50)

if __name__ == "__main__":
    print_section("Merrimack River Cruises - Database Demo")
    
    # Prompt user for database connection parameters
    print("\nEnter database connection information (press Enter for defaults):")
    host = input(f"Host [{config['host']}]: ").strip() or config['host']
    username = input(f"Username [{config['username']}]: ").strip() or config['username']
    password = input(f"Password: ").strip() or config['password']
    database = input(f"Database [{config['database']}]: ").strip() or config['database']
    
    # Connect to database
    print("\nConnecting to database...")
    db = DatabaseConnection(host, username, password, database)
    
    if not db.connect():
        print("❌ Connection failed!")
        exit(1)
    
    print("✅ Connected successfully!")
    
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
    
    # ==================== DEMO OPERATIONS ====================
    print_section("DEMO OPERATIONS")
    
    print("\nAdding vessel: Harbor Queen ($175/hr)")
    result = vessel_bll.add_vessel("Harbor Queen", 175.00)
    print(f"✅ Added with ID: {result.get('VesselID')}" if result and 'VesselID' in result else "⚠️ Already exists")
    
    print("\nAdding passenger: Alice Johnson")
    result = passenger_bll.add_passenger("Alice", "Johnson", "978-555-9999")
    print(f"✅ Added with ID: {result.get('PassengerID')}" if result and 'PassengerID' in result else "⚠️ Already exists")
    
    print("\nLooking up 'Sea Breeze'...")
    result = vessel_bll.get_vessel_id_by_name("Sea Breeze")
    print(f"✅ Vessel ID: {result['VesselID']}" if result and result.get('VesselID', -1) != -1 else "❌ Not found")
    
    print("\nAdding trip: Sea Breeze with Alice Johnson on 2025-12-15...")
    result = trip_bll.add_trip("Sea Breeze", "Alice", "Johnson", "2025-12-15", "14:00:00", 3.5, 4)
    if result and 'error' in result:
        print(f"⚠️ {result['error']}")
    elif result and 'DuplicateTrip' in result:
        print("⚠️ Duplicate trip")
    elif result and 'NotFound' in result:
        print("❌ Vessel or passenger not found")
    else:
        print("✅ Trip added")
    
    # ==================== FINAL STATE ====================
    print_section("FINAL DATA")
    
    print(f"\nVessels: {len(vessel_bll.get_all_vessels() or [])}")
    print(f"Passengers: {len(passenger_bll.get_all_passengers() or [])}")
    print(f"Trips: {len(trip_bll.get_all_trips() or [])}")
    
    # ==================== REVENUE REPORT ====================
    print_section("TOTAL REVENUE BY VESSEL")
    
    revenue_data = trip_bll.get_revenue_by_vessel()
    if revenue_data:
        for row in revenue_data:
            print(f"\n{row['Vessel Name']}: {row['Revenue']}")
    
    db.close()
    print("\n✅ Demo complete!")
