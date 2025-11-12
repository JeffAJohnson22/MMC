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

