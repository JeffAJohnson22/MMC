/* STARTER CODE WEEK 2 */

DROP DATABASE IF EXISTS MRC;
CREATE DATABASE MRC;
USE MRC;

CREATE TABLE Reservations 
	(Date DATE, 
	Departure_Time TIME, 
    Length_in_Hours DeCiMaL(4,2), 
    Vessel VARCHAR(50), 
    First_Name VARCHAR(50), 
    Last_Name VARCHAR(50), 
    Street VARCHAR(50), 
    City VARCHAR(50), 
    State CHAR(2), 
	Zip CHAR(5), 
    Phone CHAR(12), 
    Total_Passengers INT, 
    Total_Cost VARCHAR(50));

INSERT INTO Reservations
	(Date,Departure_Time,Length_in_Hours,Vessel,First_Name,Last_Name,Street,City,State,ZIP,Phone,Total_Passengers,Total_Cost)
	VALUES ('2025-03-01','8:00','2','Sea Breeze','John','Smith','123 Oak St','Cityville','MA','01234','413-555-1234','5',200.00),
('2025-03-01','9:00','3','Ocean Voyager','Emily','Clark','456 Pine St','Rivertown','MA','23456','978-555-5678','3',600.00),
('2025-03-01','8:30','1.5','The Warrior','John','Smith','123 Oak St','Cityville','MA','01234','413-555-1234','5',225.00),
('2025-03-02','8:30','1.5','The Warrior','John','Smith','123 Oak St','Cityville','MA','01234','413-555-1234','5',225.00),
('2025-03-02','10:00','2','Ocean Voyager','Emily','Clark','456 Pine St','Rivertown','MA','23456','978-555-5678','3',400.00),
('2025-03-03','11:00','4','Ocean Voyager','Michael','Lee','789 Maple Ave','Beachside','MA','34567','978-555-8765','6',800.00),
('2025-03-03','12:30','2.5','Sea Breeze','Sarah','Johnson','321 Elm St','Townsville','MA','45678','978-555-4321','4',250.00),
('2025-03-04','7:45','3','Sea Breeze','Sarah','Johnson','321 Elm St','Townsville','MA','45678','978-555-4321','4',300.00),
('2025-03-04','9:30','2','Ocean Voyager','Michael','Lee','789 Maple Ave','Beachside','MA','34567','978-555-8765','6',400.00),
('2025-03-05','8:15','1','Sea Breeze','John','Smith','123 Oak St','Cityville','MA','01234','413-555-1234','5',100.00),
('2025-03-05','11:30','3.5','Ocean Voyager','Emily','Clark','456 Pine St','Rivertown','MA','23456','978-555-5678','3',700.00),
('2025-03-06','7:00','2','Sea Breeze','Jessica','Adams','654 Birch Rd','Seaside','MA','56789','978-555-8760','2',200.00),
('2025-03-06','9:15','3','Ocean Voyager','William','Hall','789 Cedar St','Hilltop','MA','67890','978-555-9999','7',600.00),
('2025-03-06','10:00','1.5','The Warrior','Jessica','Adams','654 Birch Rd','Seaside','MA','56789','978-555-8760','2',225.00),
('2025-03-07','8:45','2','Ocean Voyager','Sarah','Johnson','321 Elm St','Townsville','MA','45678','978-555-4321','4',400.00),
('2025-03-07','11:00','3.5','Sea Breeze','Emily','Clark','456 Pine St','Rivertown','MA','23456','978-555-5678','3',350.00),
('2025-03-08','8:30','4','Ocean Voyager','John','Smith','123 Oak St','Cityville','MA','01234','413-555-1234','5',800.00),
('2025-03-08','9:30','2','Sea Breeze','Michael','Lee','789 Maple Ave','Beachside','MA','34567','978-555-8765','6',200.00),
('2025-03-08','12:00','2.5','The Warrior','William','Hall','789 Cedar St','Hilltop','MA','67890','978-555-9999','7',375.00),
('2025-03-09','7:00','3','Sea Breeze','Sarah','Johnson','321 Elm St','Townsville','MA','45678','978-555-4321','4',300.00),
('2025-03-09','9:30','1.5','Ocean Voyager','Emily','Clark','456 Pine St','Rivertown','MA','23456','978-555-5678','3',300.00),
('2025-03-10','8:00','2','Sea Breeze','Jessica','Adams','654 Birch Rd','Seaside','MA','56789','978-555-8760','2',200.00),
('2025-03-10','10:30','3','Ocean Voyager','Michael','Lee','789 Maple Ave','Beachside','MA','34567','978-555-8765','6',600.00),
('2025-03-10','12:00','2.5','The Warrior','John','Smith','123 Oak St','Cityville','MA','01234','413-555-1234','5',375.00),
('2025-03-11','7:15','1.5','Ocean Voyager','Sarah','Johnson','321 Elm St','Townsville','MA','45678','978-555-4321','4',300.00),
('2025-03-11','9:30','2','Sea Breeze','Jessica','Adams','654 Birch Rd','Seaside','MA','56789','978-555-8760','2',200.00),
('2025-03-12','8:45','3.5','Ocean Voyager','Michael','Lee','789 Maple Ave','Beachside','MA','34567','978-555-8765','6',700.00),
('2025-03-12','10:00','2','Sea Breeze','William','Hall','789 Cedar St','Hilltop','MA','67890','978-555-9999','7',200.00),
('2025-03-13','8:30','2','Sea Breeze','Emily','Clark','456 Pine St','Rivertown','MA','23456','978-555-5678','3',200.00),
('2025-03-13','9:15','3','Ocean Voyager','John','Smith','123 Oak St','Cityville','MA','01234','413-555-1234','5',600.00),
('2025-03-13','12:00','1.5','The Warrior','Sarah','Johnson','321 Elm St','Townsville','MA','45678','978-555-4321','4',225.00),
('2025-03-14','7:00','3','Ocean Voyager','Michael','Lee','789 Maple Ave','Beachside','MA','34567','978-555-8765','6',600.00),
('2025-03-14','9:30','2.5','Sea Breeze','Emily','Clark','456 Pine St','Rivertown','MA','23456','978-555-5678','3',250.00 ),
('2025-03-15','8:15','1','Ocean Voyager','Jessica','Adams','654 Birch Rd','Seaside','MA','56789','978-555-8760','2',200.00 ),
('2025-03-15','11:30','3.5','Sea Breeze','Sarah','Johnson','321 Elm St','Townsville','MA','45678','978-555-4321','4',350.00),
('2025-03-16','8:00','2','Ocean Voyager','William','Hall','789 Cedar St','Hilltop','MA','67890','978-555-9999','7',400.00);

SELECT * FROM Reservations ORDER BY Date, Departure_Time ASC;
/* YOUR CODE BELOW HERE */

-- A) One .sql file submitted unzipped
-- B) Starter code .sql file used, no changes made to reservations, only built-in SQL used

-- C) Tables created with appropriate datatypes
--  Create three new tables to hold the decomposed data: Vessels, Passengers, Trips. 
-- Each new table should have a primary key where needed
-- 1) Create Vessels table
CREATE TABLE Vessels (
    Vessel_ID INT PRIMARY KEY AUTO_INCREMENT,
    Vessel_Name VARCHAR(50) NOT NULL UNIQUE,
    Cost_Per_Hour DECIMAL(8,2) NOT NULL
);

-- D) Tables have appropriate primary and foreign keys
-- 2) Create Passengers table  
-- Each new table should have a primary key where needed
CREATE TABLE Passengers (
    Passenger_ID INT PRIMARY KEY AUTO_INCREMENT,
    First_Name VARCHAR(50) NOT NULL,
    Last_Name VARCHAR(50) NOT NULL,
    Street VARCHAR(50),
    City VARCHAR(50),
    State CHAR(2),
    Zip CHAR(5),
    Phone CHAR(12),
    UNIQUE KEY unique_passenger (First_Name, Last_Name, Phone)
);

-- 3) Create Trips table
-- Each new table should have a primary key, and foreign keys where needed
-- Do not give the Trips table a unique integer id 
CREATE TABLE Trips (
    Date DATE NOT NULL,
    Departure_Time TIME NOT NULL,
    Vessel_ID INT NOT NULL,
    Passenger_ID INT NOT NULL,
    Length_in_Hours DECIMAL(4,2) NOT NULL,
    Total_Passengers INT NOT NULL,
    --  This table should use a composite key made up of multiple attributes instead of a single integer primary key
    PRIMARY KEY (Date, Departure_Time, Vessel_ID, Passenger_ID),
    FOREIGN KEY (Vessel_ID) REFERENCES Vessels(Vessel_ID),
    FOREIGN KEY (Passenger_ID) REFERENCES Passengers(Passenger_ID)
);

-- E) Complete and correct response to superkey, candidate key, and primary key for Trips table
-- a) the total number of superkeys for this table: 4
-- b) the combinations of at least two candidate keys for this table:
--    1. (Date, Departure_Time, Vessel_ID, Passenger_ID) 
--    2. (Date, Departure_Time, Vessel_ID)
-- c) the combination chosen for your primary key and why this was chosen: 
--    (Date, Departure_Time, Vessel_ID, Passenger_ID)

-- F) Cost per hour calculated and inserted using SQL
-- Calculate and insert vessels with their cost per hour
-- create a Cost_Per_Hour attribute attached to each vessel
INSERT INTO Vessels (Vessel_Name, Cost_Per_Hour)
SELECT 
    Vessel,
    -- Calculate this using only SQL built-in functions and commands. 
    AVG(CAST(REPLACE(Total_Cost, '$', '') AS DECIMAL(8,2)) / Length_in_Hours) AS Cost_Per_Hour
FROM Reservations
GROUP BY Vessel;

-- G) Data transferred from the Reservations table to the new tables
-- Insert unique passengers from reservations
INSERT INTO Passengers (First_Name, Last_Name, Street, City, State, Zip, Phone)
SELECT DISTINCT 
    First_Name, 
    Last_Name, 
    Street, 
    City, 
    State, 
    Zip, 
    Phone
FROM Reservations
WHERE First_Name IS NOT NULL 
  AND Last_Name IS NOT NULL 
  AND Phone IS NOT NULL
ORDER BY Last_Name, First_Name;

-- Insert trips data linking to vessels and passengers
INSERT INTO Trips (Date, Departure_Time, Vessel_ID, Passenger_ID, Length_in_Hours, Total_Passengers)
SELECT 
    r.Date,
    r.Departure_Time,
    v.Vessel_ID,
    p.Passenger_ID,
    r.Length_in_Hours,
    r.Total_Passengers
FROM Reservations r
INNER JOIN Vessels v ON r.Vessel = v.Vessel_Name
INNER JOIN Passengers p ON r.First_Name = p.First_Name 
                        AND r.Last_Name = p.Last_Name 
                        AND r.Phone = p.Phone
WHERE r.Date IS NOT NULL 
  AND r.Departure_Time IS NOT NULL 
  AND v.Vessel_ID IS NOT NULL 
  AND p.Passenger_ID IS NOT NULL;

-- H) Three select * queries included
-- Display all data from the new normalized tables
-- Include the following three queries: select * from passengers; select * from vessels; select * from trips;

SELECT * FROM Passengers WHERE Passenger_ID IS NOT NULL;

SELECT * FROM Vessels WHERE Vessel_ID IS NOT NULL;

SELECT * FROM Trips WHERE Date IS NOT NULL;

-- I) Query joining tables matches SELECT * FROM Reservations query
SELECT 
    t.Date,
    t.Departure_Time,
    t.Length_in_Hours,
    v.Vessel_Name AS Vessel,
    p.First_Name,
    p.Last_Name,
    p.Street,
    p.City,
    p.State,
    p.Zip,
    p.Phone,
    t.Total_Passengers,
    CONCAT('$', FORMAT(v.Cost_Per_Hour * t.Length_in_Hours, 2)) AS Total_Cost
FROM Trips t
JOIN Vessels v ON t.Vessel_ID = v.Vessel_ID
JOIN Passengers p ON t.Passenger_ID = p.Passenger_ID
ORDER BY t.Date, t.Departure_Time ASC;

-- J) .sql file runs without error the first time