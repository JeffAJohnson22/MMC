-- Dragon Ball Z Database 
-- CSC 6302

DROP DATABASE IF EXISTS DragonBallZ;
CREATE DATABASE DragonBallZ;
USE DragonBallZ;

-- Table 1: Characters 
CREATE TABLE Characters (
    Character_ID INT AUTO_INCREMENT PRIMARY KEY,
    Character_Name VARCHAR(100) NOT NULL UNIQUE,
    Race ENUM('Saiyan', 'Namekian', 'Human', 'Android', 'Majin', 'Other') NOT NULL,
    Alignment ENUM('Hero', 'Villain', 'Neutral') NOT NULL,
    Birth_Date DATE,
    Base_Power_Level DECIMAL(15, 2) NOT NULL,
    Is_Alive BOOLEAN DEFAULT TRUE,
    Planet_Origin VARCHAR(50)
);

-- Table 2: Transformations
CREATE TABLE Transformations (
    Transformation_ID INT AUTO_INCREMENT PRIMARY KEY,
    Transformation_Name VARCHAR(100) NOT NULL UNIQUE,
    Power_Multiplier DECIMAL(6, 2) NOT NULL,
    Description TEXT
);

-- Table 3: Battles
CREATE TABLE Battles (
    Battle_ID INT AUTO_INCREMENT PRIMARY KEY,
    Battle_Name VARCHAR(150) NOT NULL,
    Location VARCHAR(100) NOT NULL,
    Battle_Date DATE NOT NULL,
    Start_Time TIME,
    Duration_Minutes INT,
    Outcome ENUM('Hero Victory', 'Villain Victory', 'Draw') NOT NULL,
    Saga VARCHAR(50)
);

-- Table 4: Battle_Participants 
CREATE TABLE Battle_Participants (
    Battle_ID INT NOT NULL,
    Character_ID INT NOT NULL,
    Transformation_ID INT NULL,
    Power_Level_In_Battle DECIMAL(15, 2) NOT NULL,
    Damage_Dealt DECIMAL(15, 2) DEFAULT 0,
    Damage_Taken DECIMAL(15, 2) DEFAULT 0,
    Was_Winner BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (Battle_ID, Character_ID),
    FOREIGN KEY (Battle_ID) REFERENCES Battles(Battle_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Character_ID) REFERENCES Characters(Character_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Transformation_ID) REFERENCES Transformations(Transformation_ID) ON DELETE SET NULL ON UPDATE CASCADE
);


-- Insert Characters
INSERT INTO Characters (Character_Name, Race, Alignment, Birth_Date, Base_Power_Level, Is_Alive, Planet_Origin) VALUES
('Goku', 'Saiyan', 'Hero', '1984-04-16', 100000.00, TRUE, 'Vegeta'),
('Vegeta', 'Saiyan', 'Hero', '1982-01-01', 95000.00, TRUE, 'Vegeta'),
('Gohan', 'Saiyan', 'Hero', '2000-05-11', 80000.00, TRUE, 'Earth'),
('Piccolo', 'Namekian', 'Hero', '1988-05-09', 75000.00, TRUE, 'Namek'),
('Krillin', 'Human', 'Hero', '1980-10-29', 15000.00, TRUE, 'Earth'),
('Trunks', 'Saiyan', 'Hero', '2015-07-09', 70000.00, TRUE, 'Earth'),
('Goten', 'Saiyan', 'Hero', '2017-11-12', 65000.00, TRUE, 'Earth'),
('Frieza', 'Other', 'Villain', '1931-01-01', 12000.00, TRUE, 'Unknown'),
('Cell', 'Android', 'Villain', '1992-01-01', 11000.00, FALSE, 'Earth'),
('Majin Buu', 'Majin', 'Villain', '1000-01-01', 13000.00, TRUE, 'Unknown'),
('Yamcha', 'Human', 'Hero', '1981-03-20', 1200.00, TRUE, 'Earth'),
('Tien', 'Human', 'Hero', '1979-01-01', 1800.00, TRUE, 'Earth'),
('Android 17', 'Android', 'Neutral', '1990-01-01', 8500.00, TRUE, 'Earth'),
('Android 18', 'Android', 'Hero', '1990-01-01', 8500.00, TRUE, 'Earth'),
('Raditz', 'Saiyan', 'Villain', '1983-01-01', 1500.00, FALSE, 'Vegeta'),
('Nappa', 'Saiyan', 'Villain', '1950-01-01', 4000.00, FALSE, 'Vegeta'),
('Broly', 'Saiyan', 'Villain', '1984-04-16', 15000.00, TRUE, 'Vegeta'),
('Beerus', 'Other', 'Neutral', '1000-01-01', 90000.00, TRUE, 'Beerus Planet'),
('Hit', 'Other', 'Neutral', '1000-01-01', 30000.00, TRUE, 'Universe 6'),
('Jiren', 'Other', 'Hero', '1990-01-01', 60000.00, TRUE, 'Universe 11'),
('Gogeta', 'Saiyan', 'Hero', NULL, 20000.00, TRUE, NULL),
('Vegito', 'Saiyan', 'Hero', NULL, 20000.00, TRUE, NULL),
('Gotenks', 'Saiyan', 'Hero', NULL, 12000.00, TRUE, NULL),
('Mr. Satan', 'Human', 'Hero', '1970-04-07', 10.00, TRUE, 'Earth'),
('Videl', 'Human', 'Hero', '2001-01-01', 300.00, TRUE, 'Earth'),
('Future Trunks', 'Saiyan', 'Hero', '2002-01-01', 8500.00, TRUE, 'Earth'),
('Bardock', 'Saiyan', 'Hero', '1960-01-01', 10000.00, FALSE, 'Vegeta'),
('Chi-Chi', 'Human', 'Hero', '1983-05-12', 500.00, TRUE, 'Earth'),
('Bulma', 'Human', 'Hero', '1982-08-18', 5.00, TRUE, 'Earth'),
('Master Roshi', 'Human', 'Hero', '1850-01-01', 1000.00, TRUE, 'Earth');

-- Insert Transformations 
INSERT INTO Transformations (Transformation_Name, Power_Multiplier, Description) VALUES
('Super Saiyan', 50.00, 'Legendary Saiyan transformation with golden hair'),
('Super Saiyan 2', 100.00, 'Ascended form beyond Super Saiyan'),
('Super Saiyan 3', 400.00, 'Ultimate form with long golden hair'),
('Super Saiyan God', 500.00, 'Divine transformation with red hair'),
('Super Saiyan Blue', 1000.00, 'Combination of Super Saiyan and God ki'),
('Ultra Instinct', 5000.00, 'Autonomous movement technique'),
('Kaioken', 2.00, 'Technique that multiplies power'),
('Golden Frieza', 100.00, 'Frieza golden transformation'),
('Perfect Form', 50.00, 'Cell perfect state'),
('Fusion', 100.00, 'Fusion dance combining two warriors'),
('Great Ape', 10.00, 'Saiyan giant ape transformation'),
('Majin', 2.50, 'Dark magic enhancement from Babidi'),
('Zenkai Boost', 1.50, 'Power increase after recovery from near death'),
('Hakai', 2550.00, 'Destoryer technique used by Gods of Destruction');

-- Insert Battles 
INSERT INTO Battles (Battle_Name, Location, Battle_Date, Start_Time, Duration_Minutes, Outcome, Saga) VALUES
('Goku vs Vegeta - First Encounter', 'Earth', '1989-12-13', '18:30:00', 120, 'Draw', 'Saiyan Saga'),
('Goku vs Frieza', 'Planet Namek', '1991-08-31', '14:00:00', 240, 'Hero Victory', 'Frieza Saga'),
('Gohan vs Cell', 'Earth', '1992-11-24', '15:45:00', 90, 'Hero Victory', 'Cell Saga'),
('Goku vs Majin Vegeta', 'Earth', '2001-08-28', '20:00:00', 60, 'Draw', 'Majin Buu Saga'),
('Goku and Vegeta vs Kid Buu', 'Supreme Kai Planet', '2002-03-29', '16:00:00', 150, 'Hero Victory', 'Majin Buu Saga'),
('Vegito vs Super Buu', 'Earth', '2002-02-09', '13:30:00', 45, 'Hero Victory', 'Majin Buu Saga'),
('Goku vs Beerus', 'Earth', '2013-08-10', '19:00:00', 75, 'Villain Victory', 'Battle of Gods'),
('Goku vs Frieza - Resurrection', 'Earth', '2015-08-02', '12:00:00', 90, 'Hero Victory', 'Resurrection F'),
('Goku vs Hit', 'Tournament Arena', '2016-02-21', '10:00:00', 30, 'Villain Victory', 'Universe 6 Saga'),
('Goku Ultra Instinct vs Jiren', 'Tournament of Power', '2018-03-18', '10:30:00', 48, 'Hero Victory', 'Tournament of Power'),
('Goku and Piccolo vs Raditz', 'Earth', '1989-04-19', '11:00:00', 45, 'Hero Victory', 'Saiyan Saga'),
('Vegeta vs Dodoria', 'Planet Namek', '1990-07-18', '09:00:00', 15, 'Hero Victory', 'Frieza Saga'),
('Gohan vs Nappa', 'Earth', '1989-11-29', '14:00:00', 30, 'Hero Victory', 'Saiyan Saga'),
('Goku vs Captain Ginyu', 'Planet Namek', '1990-11-28', '13:00:00', 40, 'Hero Victory', 'Frieza Saga'),
('Trunks vs Frieza - Future', 'Earth', '1991-08-03', '10:00:00', 5, 'Hero Victory', 'Android Saga'),
('Vegeta vs Semi-Perfect Cell', 'Earth', '1992-08-12', '16:30:00', 25, 'Villain Victory', 'Cell Saga'),
('Gogeta vs Broly', 'Earth', '2018-12-14', '14:00:00', 60, 'Hero Victory', 'Broly Movie'),
('Gotenks vs Super Buu', 'Hyperbolic Time Chamber', '2002-01-22', '12:00:00', 30, 'Draw', 'Majin Buu Saga'),
('Vegeta vs Android 19', 'Earth', '1992-03-11', '11:00:00', 20, 'Hero Victory', 'Android Saga'),
('Goku vs Pikkon', 'Other World', '1994-08-24', '12:00:00', 35, 'Hero Victory', 'Other World Tournament');

-- Insert Battle_Participants
INSERT INTO Battle_Participants (Battle_ID, Character_ID, Transformation_ID, Power_Level_In_Battle, Damage_Dealt, Damage_Taken, Was_Winner) VALUES
(1, 1, 7, 32000.00, 15000.00, 18000.00, FALSE),
(1, 2, 11, 180000.00, 18000.00, 15000.00, FALSE),
(2, 1, 1, 150000000.00, 100000000.00, 50000000.00, TRUE),
(2, 8, 8, 120000000.00, 50000000.00, 100000000.00, FALSE),
(3, 3, 2, 1000000000.00, 500000000.00, 200000000.00, TRUE),
(3, 9, 9, 900000000.00, 200000000.00, 500000000.00, FALSE),
(4, 1, 2, 800000000.00, 350000000.00, 350000000.00, FALSE),
(4, 2, 12, 850000000.00, 350000000.00, 350000000.00, FALSE),
(5, 1, 3, 1600000000.00, 800000000.00, 400000000.00, TRUE),
(5, 2, 2, 1000000000.00, 500000000.00, 300000000.00, TRUE),
(5, 10, 14, 1300000000.00, 700000000.00, 1300000000.00, FALSE),
(6, 22, 1, 5000000000.00, 3000000000.00, 500000000.00, TRUE),
(6, 10, 1, 2000000000.00, 500000000.00, 3000000000.00, FALSE),
(7, 1, 4, 5000000000.00, 2000000000.00, 8000000000.00, FALSE),
(7, 18, 1, 50000000000.00, 8000000000.00, 2000000000.00, TRUE),
(8, 1, 5, 10000000000.00, 12000000000.00, 5000000000.00, TRUE),
(8, 8, 8, 12000000000.00, 5000000000.00, 12000000000.00, FALSE),
(9, 1, 5, 10000000000.00, 15000000000.00, 20000000000.00, FALSE),
(9, 19, 1, 30000000000.00, 20000000000.00, 15000000000.00, TRUE),
(10, 1, 6, 500000000000.00, 600000000000.00, 400000000000.00, TRUE),
(10, 20, 1, 480000000000.00, 400000000000.00, 600000000000.00, FALSE),
(11, 1, 7, 416.00, 924.00, 600.00, TRUE),
(11, 4, 1, 408.00, 1330.00, 400.00, TRUE),
(11, 15, 1, 1500.00, 1000.00, 1754.00, FALSE),
(14, 1, 7, 360000.00, 120000.00, 80000.00, TRUE),
(15, 26, 1, 2850000.00, 120000000.00, 1000.00, TRUE),
(15, 8, 9, 120000000.00, 1000.00, 120000000.00, FALSE),
(17, 21, 5, 50000000000.00, 75000000000.00, 10000000000.00, TRUE),
(17, 17, 1, 45000000000.00, 10000000000.00, 75000000000.00, FALSE),
(12, 2, 1, 2500000.00, 22000.00, 5000.00, TRUE),
(13, 3, 1, 2800.00, 4000.00, 3000.00, TRUE),
(13, 16, 11, 40000.00, 3000.00, 4000.00, FALSE),
(16, 2, 1, 950000000.00, 500000000.00, 800000000.00, FALSE),
(16, 9, 9, 1100000000.00, 800000000.00, 500000000.00, TRUE),
(18, 23, 3, 6000000000.00, 2000000000.00, 1500000000.00, FALSE),
(18, 10, 14, 2500000000.00, 1500000000.00, 2000000000.00, FALSE),
(19, 2, 1, 475000000.00, 68000000.00, 10000.00, TRUE),
(19, 13, NULL, 8500.00, 10000.00, 68000000.00, FALSE),
(20, 1, 2, 1000000000.00, 500000000.00, 200000000.00, TRUE);


DROP VIEW IF EXISTS Battle_Summary_View;
CREATE VIEW Battle_Summary_View AS
SELECT 
    b.Battle_ID,
    b.Battle_Name,
    b.Location,
    b.Battle_Date,
    b.Start_Time,
    b.Duration_Minutes,
    b.Outcome,
    b.Saga,
    COUNT(DISTINCT bp.Character_ID) AS Total_Fighters,
    AVG(bp.Power_Level_In_Battle) AS Avg_Power_Level,
    MAX(bp.Power_Level_In_Battle) AS Max_Power_Level,
    SUM(bp.Damage_Dealt) AS Total_Damage_Dealt
FROM Battles b
LEFT JOIN Battle_Participants bp ON b.Battle_ID = bp.Battle_ID
GROUP BY b.Battle_ID, b.Battle_Name, b.Location, b.Battle_Date, 
         b.Start_Time, b.Duration_Minutes, b.Outcome, b.Saga
ORDER BY b.Battle_Date DESC;


-- PROCEDURE 1: READ 
DROP PROCEDURE IF EXISTS Get_All_Battles;
DELIMITER $$
CREATE PROCEDURE Get_All_Battles()
BEGIN
    SELECT * FROM Battle_Summary_View;
END $$
DELIMITER ;

-- PROCEDURE 2: CREATE - Add New Character
DROP PROCEDURE IF EXISTS Add_Character;
DELIMITER $$
CREATE PROCEDURE Add_Character(
    IN p_Character_Name VARCHAR(100),
    IN p_Race ENUM('Saiyan', 'Namekian', 'Human', 'Android', 'Majin', 'Other'),
    IN p_Alignment ENUM('Hero', 'Villain', 'Neutral'),
    IN p_Birth_Date DATE,
    IN p_Base_Power_Level DECIMAL(15,2),
    IN p_Is_Alive BOOLEAN,
    IN p_Planet_Origin VARCHAR(50)
)
BEGIN
    INSERT INTO Characters (
        Character_Name, Race, Alignment, Birth_Date, 
        Base_Power_Level, Is_Alive, Planet_Origin
    ) VALUES (
        p_Character_Name, p_Race, p_Alignment, p_Birth_Date,
        p_Base_Power_Level, p_Is_Alive, p_Planet_Origin
    );
    
    SELECT LAST_INSERT_ID() AS Character_ID;
END $$
DELIMITER ;

-- PROCEDURE 3: UPDATE
DROP PROCEDURE IF EXISTS Update_Character;
DELIMITER $$
CREATE PROCEDURE Update_Character(
    IN p_Character_ID INT,
    IN p_Character_Name VARCHAR(100),
    IN p_Base_Power_Level DECIMAL(15,2),
    IN p_Is_Alive BOOLEAN
)
BEGIN
    UPDATE Characters
    SET 
        Character_Name = p_Character_Name,
        Base_Power_Level = p_Base_Power_Level,
        Is_Alive = p_Is_Alive
    WHERE Character_ID = p_Character_ID;
    
    SELECT ROW_COUNT() AS Rows_Affected;
END $$
DELIMITER ;

-- PROCEDURE 4: DELETE
DROP PROCEDURE IF EXISTS Delete_Character;
DELIMITER $$
CREATE PROCEDURE Delete_Character(IN p_Character_ID INT)
BEGIN
    DELETE FROM Characters WHERE Character_ID = p_Character_ID;
    SELECT ROW_COUNT() AS Rows_Deleted;
END $$
DELIMITER ;

-- PROCEDURE 5: CREATE 
DROP PROCEDURE IF EXISTS Add_Battle_Participant;
DELIMITER $$
CREATE PROCEDURE Add_Battle_Participant(
    IN p_Battle_ID INT,
    IN p_Character_ID INT,
    IN p_Transformation_ID INT,
    IN p_Power_Level DECIMAL(15,2),
    IN p_Damage_Dealt DECIMAL(15,2),
    IN p_Damage_Taken DECIMAL(15,2),
    IN p_Was_Winner BOOLEAN
)
BEGIN
    INSERT INTO Battle_Participants (
        Battle_ID, Character_ID, Transformation_ID, 
        Power_Level_In_Battle, Damage_Dealt, Damage_Taken, Was_Winner
    ) VALUES (
        p_Battle_ID, p_Character_ID, p_Transformation_ID,
        p_Power_Level, p_Damage_Dealt, p_Damage_Taken, p_Was_Winner
    );
    
    SELECT ROW_COUNT() AS Rows_Inserted;
END $$
DELIMITER ;

-- ============================================================================
-- SUMMARY
-- ============================================================================

SELECT 'Database Created Successfully!' AS Status;

-- Show actual data
SELECT * FROM Characters;

SELECT * FROM Transformations;

SELECT * FROM Battles;

SELECT * FROM Battle_Participants;

SELECT * FROM Battle_Summary_View;
