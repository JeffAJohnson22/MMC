# MRC Database Application

A three-tier database application for Merrimack River Cruises using Python and MySQL.

## Architecture

The application follows a three-tier architecture:

1. **DAL (Data Access Layer)** - `DAL.py`
   - Handles all database connections and CRUD operations
   - Uses stored procedures and views from the database
   - Classes: `DatabaseConnection`, `VesselDAL`, `PassengerDAL`, `TripDAL`

2. **BLL (Business Logic Layer)** - `BLL.py`
   - Manages flow between View and DAL
   - Handles validation and business rules
   - Classes: `VesselBLL`, `PassengerBLL`, `TripBLL`

3. **View Layer** - `View.py`
   - User interface and data presentation
   - Formats data in user-friendly tables
   - Demonstrates all functionality

## Features

### 6a. Database Connection
- Prompts user for database credentials (host, user, password, database name)
- Establishes secure connection using context manager

### 6b. Total Revenue by Vessel Report
- Displays data from the "Total Revenue by Vessel" view
- Formats currency with proper $ and comma separators
- Shows vessels sorted by revenue (highest to lowest)

### 6c. getVesselId Function Demonstration
- Tests the function with an existing vessel (returns vessel ID)
- Tests the function with a non-existent vessel (returns -1)
- Displays results in a clear, user-friendly format

### 6d. Add New Trip with New Entities
- Creates a new vessel with unique name and cost per hour
- Creates a new passenger with unique name and phone number
- Creates a new trip using the newly added vessel and passenger
- All data is committed to the database
- Shows step-by-step progress and calculated trip cost

### 6e. All Trips Report
- Displays data from the "All Trips" view
- Formats dates (MM/DD/YYYY), times (12-hour format with AM/PM), and currency
- Shows trips in a formatted table
- Highlights the most recent trip (the one just added)
- Removes all technical formatting (quotes, apostrophes, tuples)

## Data Formatting

The View layer provides user-friendly formatting:
- **Currency**: `$1,234.56` format
- **Dates**: `MM/DD/YYYY` format
- **Times**: `12-hour` format with AM/PM
- **Tables**: Clean columnar display with headers and separators
- **No technical artifacts**: Removes quotes, apostrophes, tuple notation

## Running the Application

```bash
python View.py
```

The application will:
1. Prompt for database credentials
2. Run through all demonstrations automatically
3. Display statistics, reports, and test results
4. Commit all new data to the database

## BLL Methods

### VesselBLL
- `get_all_vessels()` - Get all vessels
- `add_vessel(name, cost)` - Add vessel with validation
- `get_vessel_by_id(id)` - Get specific vessel
- `delete_vessel(id)` - Delete vessel with validation
- `get_vessel_count()` - Get total count
- `get_vessel_id_by_name(name)` - Get ID by name (uses getVesselId function)
- `get_total_revenue_by_vessel()` - Get revenue report

### PassengerBLL
- `get_all_passengers()` - Get all passengers
- `add_passenger(first, last, phone)` - Add passenger with validation
- `get_passenger_by_id(id)` - Get specific passenger
- `delete_passenger(id)` - Delete passenger with validation
- `get_passenger_count()` - Get total count
- `search_passengers(term)` - Search by name or phone

### TripBLL
- `get_all_trips()` - Get all trips
- `add_trip(...)` - Add trip with comprehensive validation
- `get_trips_by_vessel(id)` - Get trips for vessel
- `get_trips_by_passenger(id)` - Get trips for passenger
- `get_trip_count()` - Get total count
- `calculate_trip_cost(vessel, hours)` - Calculate trip cost
- `get_trip_statistics()` - Get comprehensive statistics

## Validation

The BLL layer provides extensive validation:
- Empty field checks
- String length limits
- Numeric range validation
- Date/time format validation
- Duplicate prevention
- Phone number format validation
- Foreign key existence verification

## Requirements

- Python 3.x
- mysql-connector-python
- MySQL database with MRC schema

## Installation

```bash
pip install mysql-connector-python
```

## Database Setup

Ensure your MySQL database has:
- The MRC database created
- All tables (vessels, passengers, trips)
- Required stored procedures (addVessel, addPassenger, addTrip, etc.)
- Required views (All Trips, Total Revenue by Vessel)
- Required functions (getVesselId, getPassengerId)

## Author

Jeff Johnson
