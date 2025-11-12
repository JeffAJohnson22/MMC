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

-- Create All Trips
CREATE VIEW `All Trips` AS
SELECT 
    CONCAT(DATE_FORMAT(t.Date, '%M %e, %Y'), ' at ', DATE_FORMAT(t.Departure_Time, '%h:%i %p')) AS `Date and Time`,
    v.Vessel AS `Vessel Name`,
    CONCAT(p.First_Name, ' ', p.Last_Name) AS `Passenger Name`,
    CONCAT(p.Street, ', ', p.City, ', ', p.State, ' ', p.ZIP) AS `Passenger Address`,
    p.phone AS `Passenger Phone`,
    CONCAT(t.Length_in_Hours, ' hours') AS `Voyage Length`,
    CONCAT('$', FORMAT(v.Cost_Per_Hour * t.Length_in_Hours, 2)) AS `Amount Paid`
FROM trips t
JOIN vessels v ON t.Vessel_ID = v.ID
JOIN passengers p ON t.Passenger_ID = p.ID
ORDER BY t.Date DESC, t.Departure_Time DESC;

-- Call the view to display all trips
SELECT * FROM `All Trips`;

-- Create Total Revenue by Vessel view using All Trips as datasource
CREATE VIEW `Total Revenue by Vessel` AS
SELECT 
    `Vessel Name`,
    CONCAT('$', FORMAT(SUM(CAST(REPLACE(REPLACE(`Amount Paid`, '$', ''), ',', '') AS DECIMAL(10,2))), 2)) AS `Revenue`
FROM `All Trips`
GROUP BY `Vessel Name`
ORDER BY SUM(CAST(REPLACE(REPLACE(`Amount Paid`, '$', ''), ',', '') AS DECIMAL(10,2))) DESC;

-- Call the view to display total revenue by vessel
SELECT * FROM `Total Revenue by Vessel`;

-- Create getVesselId function
DELIMITER //
CREATE FUNCTION getVesselId(vesselName VARCHAR(50))
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE vesselId INT;
    
    SELECT ID INTO vesselId
    FROM vessels
    WHERE Vessel = vesselName
    LIMIT 1;
    
    IF vesselId IS NULL THEN
        RETURN -1;
    ELSE
        RETURN vesselId;
    END IF;
END//
DELIMITER ;

-- Create getPassengerId function
DELIMITER //
CREATE FUNCTION getPassengerId(firstName VARCHAR(50), lastName VARCHAR(50))
RETURNS INT
DETERMINISTIC
READS SQL DATA
BEGIN
    DECLARE passengerId INT;
    
    SELECT ID INTO passengerId
    FROM passengers
    WHERE First_Name = firstName AND Last_Name = lastName
    LIMIT 1;
    
    IF passengerId IS NULL THEN
        RETURN -1;
    ELSE
        RETURN passengerId;
    END IF;
END//
DELIMITER ;

-- Create addPassenger procedure
DELIMITER //
CREATE PROCEDURE addPassenger(
    IN p_firstName VARCHAR(50),
    IN p_lastName VARCHAR(50),
    IN p_street VARCHAR(50),
    IN p_city VARCHAR(50),
    IN p_state CHAR(2),
    IN p_zip CHAR(5),
    IN p_phone CHAR(12),
    IN p_getsSeasick TINYINT
)
BEGIN
    DECLARE existingId INT;
    
    -- Check if passenger already exists
    SELECT ID INTO existingId
    FROM passengers
    WHERE First_Name = p_firstName AND Last_Name = p_lastName
    LIMIT 1;
    
    -- If passenger doesn't exist, add them
    IF existingId IS NULL THEN
        INSERT INTO passengers (First_Name, Last_Name, Street, City, State, ZIP, phone, getsSeasick)
        VALUES (p_firstName, p_lastName, p_street, p_city, p_state, p_zip, p_phone, p_getsSeasick);
        SELECT CONCAT('Passenger ', p_firstName, ' ', p_lastName, ' added successfully with ID: ', LAST_INSERT_ID()) AS Result;
    ELSE
        SELECT CONCAT('Passenger ', p_firstName, ' ', p_lastName, ' already exists with ID: ', existingId) AS Result;
    END IF;
END//
DELIMITER ;

-- Call the procedure to add a new passenger
CALL addPassenger('David', 'Williams', '999 Cedar Ln', 'Springfield', 'MA', '78901', '413-555-9999', 0);

