-- Merrimack River Cruises Database Setup
-- This script creates the MRC database and Reservations table with sample data

-- 1) Create database MRC and recreate from scratch each time
DROP DATABASE IF EXISTS MRC;
CREATE DATABASE MRC;
USE MRC;

-- 2) Create Reservations table with attributes matching CSV columns exactly
-- 3) Using appropriate datatypes (VARCHAR(50) where specified)
CREATE TABLE Reservations (
    Date VARCHAR(50),
    Departure_Time VARCHAR(50),
    Length_in_Hours DECIMAL(3,1),
    Vessel VARCHAR(50),
    First_Name VARCHAR(50),
    Last_Name VARCHAR(50),
    Street VARCHAR(50),
    City VARCHAR(50),
    State VARCHAR(50),
    ZIP VARCHAR(50),
    Phone VARCHAR(50),
    Total_Passengers INT,
    Total_Cost VARCHAR(50)
);

-- 4) Insert first six rows from CSV data (with corrected ZIP codes)
INSERT INTO Reservations (Date, Departure_Time, Length_in_Hours, Vessel, First_Name, Last_Name, Street, City, State, ZIP, Phone, Total_Passengers, Total_Cost) VALUES
('3/1/25', '8:00', 2.0, 'Sea Breeze', 'John', 'Smith', '123 Oak St', 'Cityville', 'MA', '01234', '413-555-1234', 5, '$200.00'),
('3/1/25', '9:00', 3.0, 'Ocean Voyager', 'Emily', 'Clark', '456 Pine St', 'Rivertown', 'MA', '23456', '978-555-5678', 3, '$600.00'),
('3/2/25', '8:30', 1.5, 'The Warrior', 'John', 'Smith', '123 Oak St', 'Cityville', 'MA', '01234', '413-555-1234', 5, '$225.00'),
('3/2/25', '10:00', 2.0, 'Ocean Voyager', 'Emily', 'Clark', '456 Pine St', 'Rivertown', 'MA', '23456', '978-555-5678', 3, '$400.00'),
('3/3/25', '11:00', 4.0, 'Ocean Voyager', 'Michael', 'Lee', '789 Maple Ave', 'Beachside', 'MA', '34567', '978-555-8765', 6, '$800.00'),
('3/3/25', '12:30', 2.5, 'Sea Breeze', 'Sarah', 'Johnson', '321 Elm St', 'Townsville', 'MA', '45678', '978-555-4321', 4, '$250.00');

-- 5) Query to show all reservations (for screenshot)
SELECT * FROM Reservations;

-- 6) Three additional SELECT queries with WHERE clauses using specific attributes
-- Query 1: Find all reservations for the Ocean Voyager vessel
SELECT First_Name, Last_Name, Date, Departure_Time FROM Reservations 
WHERE Vessel = 'Ocean Voyager';

-- Query 2: Find all reservations with 4 or more passengers
SELECT First_Name, Last_Name, Vessel, Total_Passengers FROM Reservations 
WHERE Total_Passengers >= 4;

-- Query 3: Find all reservations on March 3rd, 2025
SELECT First_Name, Last_Name, Vessel, Departure_Time FROM Reservations 
WHERE Date = '3/3/25';