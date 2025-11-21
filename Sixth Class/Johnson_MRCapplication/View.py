"""
View Layer for MRC Database Application
Provides user interface and demonstrations of all BLL functionality
"""

from datetime import datetime
from typing import Dict, List, Any
from DAL import DatabaseConnection
from BLL import VesselBLL, PassengerBLL, TripBLL


def print_header(title: str):
    """Print a formatted section header."""
    print("\n" + "=" * 80)
    print(f"  {title}")
    print("=" * 80)


def print_subheader(title: str):
    """Print a formatted subsection header."""
    print(f"\n--- {title} ---")


def print_separator():
    """Print a separator line."""
    print("-" * 80)


def format_currency(value: str) -> str:
    """
    Format currency string for display.
    
    Args:
        value: Currency value (may already include $)
    
    Returns:
        Formatted currency string
    """
    if isinstance(value, (int, float)):
        return f"${value:,.2f}"
    
    # If already a string, clean it up
    value_str = str(value).replace('$', '').replace(',', '').strip()
    try:
        amount = float(value_str)
        return f"${amount:,.2f}"
    except ValueError:
        return value


def format_date(date_value: Any) -> str:
    """
    Format date for display.
    
    Args:
        date_value: Date value (string or datetime)
    
    Returns:
        Formatted date string
    """
    if isinstance(date_value, datetime):
        return date_value.strftime('%m/%d/%Y')
    
    try:
        date_str = str(date_value)
        # Try parsing different formats
        for fmt in ['%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y']:
            try:
                dt = datetime.strptime(date_str, fmt)
                return dt.strftime('%m/%d/%Y')
            except ValueError:
                continue
        return date_str
    except:
        return str(date_value)


def format_time(time_value: Any) -> str:
    """
    Format time for display.
    
    Args:
        time_value: Time value (string or time object)
    
    Returns:
        Formatted time string
    """
    time_str = str(time_value)
    
    try:
        # Try parsing as time
        for fmt in ['%H:%M:%S', '%H:%M']:
            try:
                dt = datetime.strptime(time_str, fmt)
                return dt.strftime('%I:%M %p')
            except ValueError:
                continue
        return time_str
    except:
        return time_str


def print_table(headers: List[str], rows: List[List[str]], col_widths: List[int] = None):
    """
    Print data in a formatted table.
    
    Args:
        headers: List of column headers
        rows: List of row data (each row is a list of strings)
        col_widths: Optional list of column widths
    """
    if not rows:
        print("  No data to display.")
        return
    
    # Calculate column widths if not provided
    if col_widths is None:
        col_widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                if i < len(col_widths):
                    col_widths[i] = max(col_widths[i], len(str(cell)))
    
    # Print header
    header_line = "  " + " | ".join(h.ljust(col_widths[i]) for i, h in enumerate(headers))
    print(header_line)
    print("  " + "-" * (len(header_line) - 2))
    
    # Print rows
    for row in rows:
        row_line = "  " + " | ".join(str(cell).ljust(col_widths[i]) for i, cell in enumerate(row))
        print(row_line)


def get_database_credentials():
    """
    Prompt user for database connection parameters.
    
    Returns:
        Dictionary with connection parameters
    """
    print_header("MRC Database Application - Setup")
    print("\nPlease enter your database connection information:")
    
    host = input("  Database Host [localhost]: ").strip() or "localhost"
    user = input("  Database User [root]: ").strip() or "root"
    password = input("  Database Password [press Enter for none]: ").strip()
    database = input("  Database Name [mrc]: ").strip() or "mrc"
    
    return {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }


def display_total_revenue_by_vessel(vessel_bll: VesselBLL):
    """
    Display the Total Revenue by Vessel view in a user-friendly format.
    
    Args:
        vessel_bll: VesselBLL instance
    """
    print_header("6b. Total Revenue by Vessel Report")
    
    revenue_data = vessel_bll.get_total_revenue_by_vessel()
    
    if not revenue_data:
        print("  No revenue data available.")
        return
    
    # Prepare table data
    headers = ["Vessel Name", "Total Revenue"]
    rows = []
    
    for vessel in revenue_data:
        vessel_name = vessel.get('Vessel Name', 'Unknown')
        revenue = vessel.get('Revenue', '$0.00')
        
        rows.append([vessel_name, format_currency(revenue)])
    
    print(f"\n  Total vessels with revenue: {len(rows)}")
    print()
    print_table(headers, rows, [30, 20])


def demonstrate_get_vessel_id(vessel_bll: VesselBLL):
    """
    Demonstrate the getVesselId function with both matching and non-matching cases.
    
    Args:
        vessel_bll: VesselBLL instance
    """
    print_header("6c. Demonstrate getVesselId Function")
    
    # Get all vessels to find a valid one
    all_vessels = vessel_bll.get_all_vessels()
    
    if all_vessels:
        # Test with a vessel that exists
        existing_vessel_name = all_vessels[0]['Name']
        print_subheader(f"Test 1: Looking up existing vessel '{existing_vessel_name}'")
        
        vessel_id = vessel_bll.get_vessel_id_by_name(existing_vessel_name)
        
        if vessel_id > 0:
            print(f"  ✓ SUCCESS: Vessel '{existing_vessel_name}' found with ID: {vessel_id}")
        else:
            print(f"  ✗ ERROR: Vessel '{existing_vessel_name}' not found (returned {vessel_id})")
    
    # Test with a vessel that doesn't exist
    non_existing_vessel_name = "Nonexistent Boat XYZ123"
    print_subheader(f"Test 2: Looking up non-existent vessel '{non_existing_vessel_name}'")
    
    vessel_id = vessel_bll.get_vessel_id_by_name(non_existing_vessel_name)
    
    if vessel_id == -1:
        print(f"  ✓ SUCCESS: Vessel '{non_existing_vessel_name}' not found (returned -1 as expected)")
    else:
        print(f"  ✗ ERROR: Unexpected result for non-existent vessel (returned {vessel_id})")


def add_new_trip_with_new_entities(vessel_bll: VesselBLL, passenger_bll: PassengerBLL, trip_bll: TripBLL):
    """
    Add a new trip with a brand new vessel and brand new passenger.
    
    Args:
        vessel_bll: VesselBLL instance
        passenger_bll: PassengerBLL instance
        trip_bll: TripBLL instance
    """
    print_header("6d. Add New Trip with New Vessel and New Passenger")
    
    # Generate unique names with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Step 1: Add new vessel
    print_subheader("Step 1: Adding New Vessel")
    new_vessel_name = f"Test Vessel {timestamp}"
    new_vessel_cost = 175.00
    
    print(f"  Vessel Name: {new_vessel_name}")
    print(f"  Cost Per Hour: ${new_vessel_cost:.2f}")
    
    vessel_result = vessel_bll.add_vessel(new_vessel_name, new_vessel_cost)
    
    if vessel_result['success']:
        print(f"  ✓ {vessel_result['message']}")
        print(f"  Vessel ID: {vessel_result['vessel_id']}")
    else:
        print(f"  ✗ {vessel_result['message']}")
        return
    
    # Step 2: Add new passenger
    print_subheader("Step 2: Adding New Passenger")
    new_passenger_first = "TestFirst"
    new_passenger_last = f"TestLast{timestamp}"
    new_passenger_phone = "555-TEST-123"
    
    print(f"  Passenger Name: {new_passenger_first} {new_passenger_last}")
    print(f"  Phone: {new_passenger_phone}")
    
    passenger_result = passenger_bll.add_passenger(
        new_passenger_first, 
        new_passenger_last, 
        new_passenger_phone
    )
    
    if passenger_result['success']:
        print(f"  ✓ {passenger_result['message']}")
        print(f"  Passenger ID: {passenger_result['passenger_id']}")
    else:
        print(f"  ✗ {passenger_result['message']}")
        return
    
    # Step 3: Add new trip
    print_subheader("Step 3: Adding New Trip")
    
    trip_date = datetime.now().strftime('%Y-%m-%d')
    trip_time = "14:30:00"
    trip_length = 3.5
    trip_passengers = 8
    
    print(f"  Vessel: {new_vessel_name}")
    print(f"  Passenger: {new_passenger_first} {new_passenger_last}")
    print(f"  Date: {format_date(trip_date)}")
    print(f"  Departure Time: {format_time(trip_time)}")
    print(f"  Length: {trip_length} hours")
    print(f"  Total Passengers: {trip_passengers}")
    
    # Calculate expected cost
    cost_info = trip_bll.calculate_trip_cost(new_vessel_name, trip_length)
    if cost_info['success']:
        print(f"  Expected Cost: {format_currency(cost_info['cost'])}")
    
    trip_result = trip_bll.add_trip(
        new_vessel_name,
        new_passenger_first,
        new_passenger_last,
        trip_date,
        trip_time,
        trip_length,
        trip_passengers
    )
    
    if trip_result['success']:
        print(f"  ✓ {trip_result['message']}")
        print("\n  ✓ All data committed to database successfully!")
    else:
        print(f"  ✗ {trip_result['message']}")


def display_all_trips(trip_bll: TripBLL):
    """
    Display all trips from the 'All Trips' view in a user-friendly format.
    
    Args:
        trip_bll: TripBLL instance
    """
    print_header("6e. All Trips Report")
    
    trips = trip_bll.get_all_trips()
    
    if not trips:
        print("  No trips available.")
        return
    
    print(f"\n  Total trips in database: {len(trips)}")
    print()
    
    # Prepare table data - showing most recent trips first
    headers = ["Date", "Time", "Vessel", "Passenger", "Hours", "Total Pass.", "Amount"]
    rows = []
    
    # Sort by date descending (most recent first)
    sorted_trips = sorted(trips, key=lambda x: (x.get('Date', ''), x.get('Departure Time', '')), reverse=True)
    
    for trip in sorted_trips:
        date = format_date(trip.get('Date', ''))
        time = format_time(trip.get('Departure Time', ''))
        vessel = trip.get('Vessel Name', 'Unknown')
        passenger = f"{trip.get('Passenger First Name', '')} {trip.get('Passenger Last Name', '')}"
        hours = str(trip.get('Length in Hours', '0'))
        total_pass = str(trip.get('Total Passengers', '0'))
        amount = format_currency(trip.get('Amount Paid', '0'))
        
        rows.append([date, time, vessel, passenger, hours, total_pass, amount])
    
    # Show first 15 trips to keep output manageable
    display_count = min(15, len(rows))
    print(f"  Displaying {display_count} most recent trips:\n")
    
    print_table(headers, rows[:display_count], [12, 10, 20, 20, 6, 11, 12])
    
    if len(rows) > display_count:
        print(f"\n  ... and {len(rows) - display_count} more trips")
    
    # Highlight the most recent trip (likely the one just added)
    print_subheader("Most Recent Trip Details")
    recent_trip = sorted_trips[0]
    print(f"  Date: {format_date(recent_trip.get('Date', ''))}")
    print(f"  Departure Time: {format_time(recent_trip.get('Departure Time', ''))}")
    print(f"  Vessel: {recent_trip.get('Vessel Name', 'Unknown')}")
    print(f"  Passenger: {recent_trip.get('Passenger First Name', '')} {recent_trip.get('Passenger Last Name', '')}")
    print(f"  Duration: {recent_trip.get('Length in Hours', '0')} hours")
    print(f"  Total Passengers: {recent_trip.get('Total Passengers', '0')}")
    print(f"  Amount Paid: {format_currency(recent_trip.get('Amount Paid', '0'))}")


def display_statistics(vessel_bll: VesselBLL, passenger_bll: PassengerBLL, trip_bll: TripBLL):
    """
    Display overall database statistics.
    
    Args:
        vessel_bll: VesselBLL instance
        passenger_bll: PassengerBLL instance
        trip_bll: TripBLL instance
    """
    print_header("Database Statistics Summary")
    
    # Get statistics
    stats = trip_bll.get_trip_statistics()
    vessel_count = vessel_bll.get_vessel_count()
    passenger_count = passenger_bll.get_passenger_count()
    
    print(f"\n  Total Vessels: {vessel_count}")
    print(f"  Total Passengers: {passenger_count}")
    print(f"  Total Trips: {stats['total_trips']}")
    print(f"  Total Passengers Served: {stats['total_passengers']:,}")
    print(f"  Average Trip Length: {stats['average_trip_length']} hours")
    
    if stats['most_popular_vessel']:
        print(f"  Most Popular Vessel: {stats['most_popular_vessel']}")


def main():
    """Main function to run the MRC Database Application demonstration."""
    
    # Get database credentials from user
    db_config = get_database_credentials()
    
    print("\n  Connecting to database...")
    
    try:
        # Establish database connection using context manager
        with DatabaseConnection(**db_config) as db:
            print("  ✓ Connected successfully!\n")
            
            # Initialize BLL objects
            vessel_bll = VesselBLL(db)
            passenger_bll = PassengerBLL(db)
            trip_bll = TripBLL(db)
            
            # Display initial statistics
            display_statistics(vessel_bll, passenger_bll, trip_bll)
            
            # 6b. Display Total Revenue by Vessel
            display_total_revenue_by_vessel(vessel_bll)
            
            # 6c. Demonstrate getVesselId function
            demonstrate_get_vessel_id(vessel_bll)
            
            # 6d. Add new trip with new vessel and passenger
            add_new_trip_with_new_entities(vessel_bll, passenger_bll, trip_bll)
            
            # 6e. Display all trips (including newly added)
            display_all_trips(trip_bll)
            
            # Final statistics
            print_header("Final Database Statistics")
            display_statistics(vessel_bll, passenger_bll, trip_bll)
            
            print_header("Application Demonstration Complete")
            print("\n  All operations completed successfully!")
            print("  Database changes have been committed.\n")
    
    except Exception as e:
        print(f"\n  ✗ Error: {str(e)}")
        print("  Please check your database connection and try again.\n")


if __name__ == "__main__":
    main()
