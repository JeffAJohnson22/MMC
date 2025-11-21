#!/usr/bin/env python3
"""
Quick Test Script for MRC Application
Tests that all modules can be imported and basic structure is correct
"""

import sys

def test_imports():
    """Test that all modules can be imported."""
    print("Testing module imports...")
    
    try:
        import DAL
        print("✓ DAL module imported successfully")
    except Exception as e:
        print(f"✗ Error importing DAL: {e}")
        return False
    
    try:
        import BLL
        print("✓ BLL module imported successfully")
    except Exception as e:
        print(f"✗ Error importing BLL: {e}")
        return False
    
    try:
        import View
        print("✓ View module imported successfully")
    except Exception as e:
        print(f"✗ Error importing View: {e}")
        return False
    
    return True

def test_classes():
    """Test that all classes are defined."""
    print("\nTesting class definitions...")
    
    try:
        from DAL import DatabaseConnection, VesselDAL, PassengerDAL, TripDAL
        print("✓ All DAL classes found")
    except Exception as e:
        print(f"✗ Error with DAL classes: {e}")
        return False
    
    try:
        from BLL import VesselBLL, PassengerBLL, TripBLL
        print("✓ All BLL classes found")
    except Exception as e:
        print(f"✗ Error with BLL classes: {e}")
        return False
    
    return True

def test_methods():
    """Test that required methods exist."""
    print("\nTesting method definitions...")
    
    from BLL import VesselBLL, PassengerBLL, TripBLL
    
    # Check VesselBLL methods
    vessel_methods = [
        'get_all_vessels', 'add_vessel', 'get_vessel_by_id', 
        'delete_vessel', 'get_vessel_count', 'get_vessel_id_by_name',
        'get_total_revenue_by_vessel'
    ]
    
    for method in vessel_methods:
        if not hasattr(VesselBLL, method):
            print(f"✗ VesselBLL missing method: {method}")
            return False
    print("✓ All VesselBLL methods found")
    
    # Check PassengerBLL methods
    passenger_methods = [
        'get_all_passengers', 'add_passenger', 'get_passenger_by_id',
        'delete_passenger', 'get_passenger_count', 'search_passengers'
    ]
    
    for method in passenger_methods:
        if not hasattr(PassengerBLL, method):
            print(f"✗ PassengerBLL missing method: {method}")
            return False
    print("✓ All PassengerBLL methods found")
    
    # Check TripBLL methods
    trip_methods = [
        'get_all_trips', 'add_trip', 'get_trips_by_vessel',
        'get_trips_by_passenger', 'get_trip_count', 'calculate_trip_cost',
        'get_trip_statistics'
    ]
    
    for method in trip_methods:
        if not hasattr(TripBLL, method):
            print(f"✗ TripBLL missing method: {method}")
            return False
    print("✓ All TripBLL methods found")
    
    return True

def main():
    """Run all tests."""
    print("=" * 60)
    print("MRC Application Structure Test")
    print("=" * 60)
    
    if not test_imports():
        print("\n✗ Import tests failed!")
        sys.exit(1)
    
    if not test_classes():
        print("\n✗ Class tests failed!")
        sys.exit(1)
    
    if not test_methods():
        print("\n✗ Method tests failed!")
        sys.exit(1)
    
    print("\n" + "=" * 60)
    print("✓ All structure tests passed!")
    print("=" * 60)
    print("\nThe application is ready to run.")
    print("\nTo run the full application:")
    print("  python View.py")
    print("\nMake sure you have:")
    print("  1. MySQL server running")
    print("  2. MRC database created with all tables, views, and procedures")
    print("  3. mysql-connector-python installed (pip install -r requirements.txt)")
    print()

if __name__ == "__main__":
    main()
