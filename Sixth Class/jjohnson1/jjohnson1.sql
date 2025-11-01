-- syntax that will re-create the database from scratch each time.
--  drop statement
DROP DATABASE IF EXISTS MRC;
-- Created a database called "MRC.
-- Database named correctly and has the correct create 
CREATE DATABASE MRC;
-- use statements
USE MRC;

-- Create a table called "Reservations" with an attribute for each column in the .csv. Match the column headings exactly from the .csv'
-- Give them data types
-- Table created with the required attributes
-- Attributes created with appropriate datatypes
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
    -- This fixes the leading zeros
    ZIP CHAR(5),
    Phone VARCHAR(50),
    Total_Passengers INT,
	-- I thought to make this a decimal but the $ is the issue if i didnt need it they type would be a decimal
    Total_Cost VARCHAR(50)
);

INSERT INTO Reservations (Date, Departure_Time, Length_in_Hours, Vessel, First_Name, Last_Name, Street, City, State, ZIP, Phone, Total_Passengers, Total_Cost) VALUES
-- First six rows from csv inserted
('3/1/25', '8:00', 2.0, 'Sea Breeze', 'John', 'Smith', '123 Oak St', 'Cityville', 'MA', '01234', '413-555-1234', 5, '$200.00'),
('3/1/25', '9:00', 3.0, 'Ocean Voyager', 'Emily', 'Clark', '456 Pine St', 'Rivertown', 'MA', '02345', '978-555-5678', 3, '$600.00'),
('3/2/25', '8:30', 1.5, 'The Warrior', 'John', 'Smith', '123 Oak St', 'Cityville', 'MA', '01234', '413-555-1234', 5, '$225.00'),
('3/2/25', '10:00', 2.0, 'Ocean Voyager', 'Emily', 'Clark', '456 Pine St', 'Rivertown', 'MA', '02345', '978-555-5678', 3, '$400.00'),
('3/3/25', '11:00', 4.0, 'Ocean Voyager', 'Michael', 'Lee', '789 Maple Ave', 'Beachside', 'MA', '03456', '978-555-8765', 6, '$800.00'),
('3/3/25', '12:30', 2.5, 'Sea Breeze', 'Sarah', 'Johnson', '321 Elm St', 'Townsville', 'MA', '04567', '978-555-4321', 4, '$250.00');

-- a query "SELECT * FROM Reservations
-- SELECT * From Reservations query
SELECT * FROM Reservations;

-- three other SELECT queries with WHERE clauses
-- Three additional queries
-- 1 
SELECT First_Name, Last_Name, Total_Passengers, Total_Cost FROM Reservations 
WHERE Vessel = 'Sea Breeze';

-- 2
SELECT First_Name, Last_Name, Vessel, Total_Passengers FROM Reservations 
WHERE Total_Passengers >= 4;

-- 3
SELECT First_Name, Last_Name, Vessel, Departure_Time FROM Reservations 
WHERE Date = '3/3/25';