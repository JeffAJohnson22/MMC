/* WEEK 3 STARTER CODE */

DROP DATABASE IF EXISTS `mrc`;
CREATE DATABASE IF NOT EXISTS `mrc`; 
USE `mrc`;

DROP TABLE IF EXISTS `vessels`;

CREATE TABLE `vessels` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Vessel` varchar(50) NOT NULL,
  `Cost_Per_Hour` decimal(6,2) DEFAULT NULL,
  PRIMARY KEY (`ID`)
);

INSERT INTO `vessels` VALUES 
	(1,'Ocean Voyager',200.00),
	(2,'Sea Breeze',100.00),
    (3,'The Warrior',150.00);


DROP TABLE IF EXISTS `passengers`;

CREATE TABLE `passengers` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `First_Name` varchar(50) NOT NULL,
  `Last_Name` varchar(50) NOT NULL,
  `Street` varchar(50) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `State` CHAR(2) DEFAULT NULL,
  ZIP CHAR(5) DEFAULT NULL,
  `phone` CHAR(12) DEFAULT NULL,
  `getsSeasick` tinyint DEFAULT NULL,
  PRIMARY KEY (`ID`)
);

INSERT INTO `passengers` VALUES 
	(1,'Emily', 'Clark','456 Pine St', 'Rivertown', 'MA', '23456','978-555-5678',NULL),
	(2,'Michael', 'Lee','789 Maple Ave', 'Beachside', 'MA', '34567','978-555-8765',NULL),
    (3,'Jessica', 'Adams','654 Birch Rd', 'Seaside', 'MA', '56789','978-555-8760',NULL),
    (4,'Sarah', 'Johnson','321 Elm St', 'Townsville', 'MA', '45678','978-555-4321',NULL),
    (5,'John', 'Smith','123 Oak St', 'Cityville', 'MA', '01234','413-555-1234',NULL);


DROP TABLE IF EXISTS `trips`;

CREATE TABLE `trips` (
  `Vessel_ID` int NOT NULL,
  `Passenger_ID` int NOT NULL,
  `Date` date NOT NULL,
  `Departure_Time` time NOT NULL,
  `Length_in_Hours` decimal(5,2) NOT NULL,
  `Total_Passengers` int NOT NULL,
  PRIMARY KEY (`Vessel_ID`,`Date`,`Departure_Time`),
  FOREIGN KEY (`Vessel_ID`) REFERENCES `vessels` (`ID`),
  FOREIGN KEY (`Passenger_ID`) REFERENCES `passengers` (`ID`)
);

INSERT INTO `trips` VALUES 
	(1,1,'2025-03-01', '09:00:00',3.00,3),
	(1,1,'2025-03-02', '10:00:00',2.00,3),
    (1,1,'2025-03-05', '11:30:00',3.50,3),
    (1,1,'2025-03-09', '09:30:00',1.50,3),
    (1,2,'2025-03-03', '11:00:00',4.00,6),
    (1,2,'2025-03-04', '09:30:00',2.00,6),
    (1,2,'2025-03-10', '10:30:00',3.00,6),
    (1,2,'2025-03-12', '08:45:00',3.50,6),
    (1,2,'2025-03-14', '07:00:00',3.00,6),
    (2,3,'2025-03-06', '07:00:00',2.00,2),
    (2,3,'2025-03-10', '08:00:00',2.00,2),
    (2,3,'2025-03-11', '09:30:00',2.00,2),
    (2,4,'2025-03-03', '12:30:00',2.50,4),
    (2,4,'2025-03-04', '07:45:00',3.00,4),
    (2,4,'2025-03-09', '07:00:00',3.00,4),
    (2,4,'2025-03-15', '11:30:00',3.50,4),
    (3,5,'2025-03-02', '08:30:00',1.50,5),
    (3,5,'2025-03-10', '12:00:00',2.50,5);


/* Add your code below here */

-- Create AND call a view called "All Trips" that displays one row per voyage and has the following column headers: Date and Time, Vessel Name, Passenger Name, Passenger Address, Passenger Phone, Voyage Length, and Amount Paid.

CREATE VIEW `All Trips` AS
SELECT 
    CONCAT(t.Date, ' ', t.Departure_Time) AS `Date and Time`,
    v.Vessel AS `Vessel Name`,
    CONCAT(p.First_Name, ' ', p.Last_Name) AS `Passenger Name`,
    CONCAT(p.Street, ', ', p.City, ', ', p.State, ' ', p.ZIP) AS `Passenger Address`,
    p.phone AS `Passenger Phone`,
    CONCAT(t.Length_in_Hours, ' hours') AS `Voyage Length`,
    CONCAT('$', FORMAT(t.Length_in_Hours * v.Cost_Per_Hour, 2)) AS `Amount Paid`
FROM trips t
JOIN vessels v ON t.Vessel_ID = v.ID
JOIN passengers p ON t.Passenger_ID = p.ID
-- Sort this by date/time with the most recent Voyages at the top. You will need to combine text fields and perform mathematical operations on multiple columns to achieve this. Format dates/times so that non-technical users will understand them.
ORDER BY t.Date DESC, t.Departure_Time DESC;

-- Call the view to display all trips
SELECT * FROM `All Trips`;

-- Create AND call a view called "Total Revenue by Vessel" that uses the above view as a datasource, sorted highest to lowest revenue.
-- It should have column headers named Vessel Name and Revenue. The Revenue column should sum the revenue for each vessel.
CREATE VIEW `Total Revenue by Vessel` AS
SELECT 
    v.Vessel AS `Vessel Name`,
    CONCAT('$', FORMAT(SUM(t.Length_in_Hours * v.Cost_Per_Hour), 2)) AS `Revenue`
FROM trips t
JOIN vessels v ON t.Vessel_ID = v.ID
GROUP BY v.Vessel
ORDER BY SUM(t.Length_in_Hours * v.Cost_Per_Hour) DESC;


-- Create a function called "getVesselId" that gets the Vessel id number based on its name. It should return -1 if not found. 
DELIMITER $$
CREATE FUNCTION getVesselId(vesselName VARCHAR(50))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE vesselId INT;
    
    SELECT ID INTO vesselId FROM vessels WHERE Vessel = vesselName;
    
    IF vesselId IS NULL THEN
        RETURN -1;
    ELSE
        RETURN vesselId;
    END IF;
END $$
DELIMITER ;

-- Create a function called "getPassengerId" the Passenger id number based on their name. It should return -1 if not found. 
DELIMITER $$
CREATE FUNCTION getPassengerId(firstName VARCHAR(50), lastName VARCHAR(50))
RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE passengerId INT;
    
    SELECT ID INTO passengerId FROM passengers WHERE First_Name = firstName AND Last_Name = lastName;
    
    IF passengerId IS NULL THEN
        RETURN -1;
    ELSE
        RETURN passengerId;
    END IF;
END $$
DELIMITER ;

-- Create a procedure called "addPassenger" that adds a new Passenger to the Passenger table. It should handle the case when a Passenger with the same name already exists.  It should handle the case where a match isn't found for a passenger.
DELIMITER $$
CREATE PROCEDURE addPassenger(
    IN p_First_Name VARCHAR(50),
    IN p_Last_Name VARCHAR(50),
    IN p_Street VARCHAR(50),  
    IN p_City VARCHAR(50),
    IN p_State CHAR(2),
    IN p_ZIP CHAR(5),
    IN p_phone CHAR(12)
)
BEGIN
    DECLARE existingId INT;
    SET existingId = getPassengerId(p_First_Name, p_Last_Name);
    IF existingId = -1 THEN
        INSERT INTO passengers (First_Name, Last_Name, Street, City, State, ZIP, phone)
        VALUES (p_First_Name, p_Last_Name, p_Street, p_City, p_State, p_ZIP, p_phone);
    END IF;
END $$
DELIMITER ;

CALL addPassenger('Vegeta', 'Breifs', '123 Capsule St', 'Capsule Corp', 'WC', '33389', '451-312-5524');  

-- Create a procedure called "addVessel" that adds a new Vessel to the Vessel table. It should handle the case when a Vessel with the same name already exists. It should handle the case where a match isn't found for a vessel.
DELIMITER $$
CREATE PROCEDURE addVessel(
    IN v_Vessel VARCHAR(50),
    IN v_Cost_Per_Hour DECIMAL(6,2)
)
BEGIN
    DECLARE existingId INT;
    SET existingId = getVesselId(v_Vessel);
    IF existingId = -1 THEN
        INSERT INTO vessels (Vessel, Cost_Per_Hour)
        VALUES (v_Vessel, v_Cost_Per_Hour);
    END IF;
END $$
DELIMITER ;

-- Add a new vessel using this procedure.
CALL addVessel('A Saiyans Pride', 9000.00);  

-- Create a procedure called "addTrip" that adds a new trip to the table using vessel and passenger names. Needs to use getPassengerId" and "getVesselId" functions 
DELIMITER $$
CREATE PROCEDURE addTrip(
    IN t_Vessel_Name VARCHAR(50),
    IN t_Passenger_First_Name VARCHAR(50),
    IN t_Passenger_Last_Name VARCHAR(50),
    IN t_Date DATE,
    IN t_Departure_Time TIME,
    IN t_Length_in_Hours DECIMAL(5,2),
    IN t_Total_Passengers INT
)

BEGIN
    DECLARE v_Vessel_ID INT;
    DECLARE v_Passenger_ID INT;
    
    SET v_Vessel_ID = getVesselId(t_Vessel_Name);
    SET v_Passenger_ID = getPassengerId(t_Passenger_First_Name, t_Passenger_Last_Name);
    
    IF v_Vessel_ID = -1 THEN
        SELECT CONCAT('The Vessel "', t_Vessel_Name, '" is not available.') AS Result;
    ELSEIF v_Passenger_ID = -1 THEN
        SELECT CONCAT('The Passenger "', t_Passenger_First_Name, ' ', t_Passenger_Last_Name, '" is not on the list.') AS Result;
    ELSE
        INSERT INTO trips (Vessel_ID, Passenger_ID, Date, Departure_Time, Length_in_Hours, Total_Passengers)
        VALUES (v_Vessel_ID, v_Passenger_ID, t_Date, t_Departure_Time, t_Length_in_Hours, t_Total_Passengers);
    END IF;
END $$
DELIMITER ;

-- Add at least one new trip using the new passenger and vessel added in steps 7 and 8 above.
CALL addTrip('A Saiyans Pride', 'Vegeta', 'Breifs', '2026-03-22', '10:00:00', 5.00, 4);
CALL addVessel('The Legendary One', 500.00);
CALL addPassenger('Broly', 'Tara', '789 Saiyan Rd', 'Planet Vegeta', 'PV', '44456', '555-123-4567');
CALL addTrip('The Legendary One', 'Broly', 'Tara', '2026-04-22', '5:00:00', 2.5, 4);

-- Call the "All Trips" and "Total Revenue by Vessel" views again to show your new data loaded successfully
SELECT * FROM `All Trips`;
SELECT * FROM `Total Revenue by Vessel`;
