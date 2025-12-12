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
    Base_Power_Level DECIMAL(15, 2) NOT NULL,
    Is_Alive BOOLEAN DEFAULT TRUE,
    Planet_Origin VARCHAR(50)
);

-- Table 2: Transformations
CREATE TABLE Transformations (
    Transformation_ID INT AUTO_INCREMENT PRIMARY KEY,
    Transformation_Name VARCHAR(100) NOT NULL UNIQUE,
    Power_Multiplier DECIMAL(6, 2) NOT NULL
);

-- Table 3: Battles
CREATE TABLE Battles (
    Battle_ID INT AUTO_INCREMENT PRIMARY KEY,
    Battle_Name VARCHAR(150) NOT NULL,
    Location VARCHAR(100) NOT NULL,
    Battle_Date DATE NOT NULL,
    Outcome ENUM('Hero Victory', 'Villain Victory', 'Draw') NOT NULL
);

-- Table 4: Battle_Participants 
CREATE TABLE Battle_Participants (
    Battle_ID INT NOT NULL,
    Character_ID INT NOT NULL,
    Transformation_ID INT NULL,
    Power_Level_In_Battle DECIMAL(15, 2) NOT NULL,
    Was_Winner BOOLEAN DEFAULT FALSE,
    PRIMARY KEY (Battle_ID, Character_ID),
    FOREIGN KEY (Battle_ID) REFERENCES Battles(Battle_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Character_ID) REFERENCES Characters(Character_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Transformation_ID) REFERENCES Transformations(Transformation_ID) ON DELETE SET NULL ON UPDATE CASCADE
);


INSERT INTO Characters (Character_Name, Race, Alignment, Base_Power_Level, Is_Alive, Planet_Origin) VALUES
('Goku', 'Saiyan', 'Hero', 100000.00, TRUE, 'Vegeta'),
('Vegeta', 'Saiyan', 'Hero', 95000.00, TRUE, 'Vegeta'),
('Gohan', 'Saiyan', 'Hero', 80000.00, TRUE, 'Earth'),
('Piccolo', 'Namekian', 'Hero', 75000.00, TRUE, 'Namek'),
('Krillin', 'Human', 'Hero', 15000.00, TRUE, 'Earth'),
('Trunks', 'Saiyan', 'Hero', 70000.00, TRUE, 'Earth'),
('Goten', 'Saiyan', 'Hero', 65000.00, TRUE, 'Earth'),
('Frieza', 'Other', 'Villain', 12000.00, TRUE, 'Unknown'),
('Cell', 'Android', 'Villain', 11000.00, FALSE, 'Earth'),
('Majin Buu', 'Majin', 'Villain', 13000.00, TRUE, 'Unknown'),
('Yamcha', 'Human', 'Hero', 1200.00, TRUE, 'Earth'),
('Tien', 'Human', 'Hero', 1800.00, TRUE, 'Earth'),
('Android 17', 'Android', 'Neutral', 8500.00, TRUE, 'Earth'),
('Android 18', 'Android', 'Hero', 8500.00, TRUE, 'Earth'),
('Raditz', 'Saiyan', 'Villain', 1500.00, FALSE, 'Vegeta'),
('Nappa', 'Saiyan', 'Villain', 4000.00, FALSE, 'Vegeta'),
('Broly', 'Saiyan', 'Villain', 15000.00, TRUE, 'Vegeta'),
('Beerus', 'Other', 'Neutral', 90000.00, TRUE, 'Beerus Planet'),
('Hit', 'Other', 'Neutral', 30000.00, TRUE, 'Universe 6'),
('Jiren', 'Other', 'Hero', 60000.00, TRUE, 'Universe 11'),
('Gogeta', 'Saiyan', 'Hero', 20000.00, TRUE, NULL),
('Vegito', 'Saiyan', 'Hero', 20000.00, TRUE, NULL),
('Gotenks', 'Saiyan', 'Hero', 12000.00, TRUE, NULL),
('Mr. Satan', 'Human', 'Hero', 10.00, TRUE, 'Earth'),
('Videl', 'Human', 'Hero', 300.00, TRUE, 'Earth'),
('Future Trunks', 'Saiyan', 'Hero', 8500.00, TRUE, 'Earth'),
('Bardock', 'Saiyan', 'Hero', 10000.00, FALSE, 'Vegeta'),
('Chi-Chi', 'Human', 'Hero', 500.00, TRUE, 'Earth'),
('Bulma', 'Human', 'Hero', 5.00, TRUE, 'Earth'),
('Master Roshi', 'Human', 'Hero', 1000.00, TRUE, 'Earth');

INSERT INTO Transformations (Transformation_Name, Power_Multiplier) VALUES
('Super Saiyan', 50.00),
('Super Saiyan 2', 100.00),
('Super Saiyan 3', 400.00),
('Super Saiyan God', 500.00),
('Super Saiyan Blue', 1000.00),
('Ultra Instinct', 5000.00),
('Kaioken', 2.00),
('Golden Frieza', 100.00),
('Perfect Form', 50.00),
('Fusion', 100.00),
('Great Ape', 10.00),
('Majin', 2.50),
('Zenkai Boost', 1.50),
('Hakai', 2550.00);

INSERT INTO Battles (Battle_Name, Location, Battle_Date, Outcome) VALUES
('Goku vs Vegeta - First Encounter', 'Earth', '1989-12-13', 'Draw'),
('Goku vs Frieza', 'Planet Namek', '1991-08-31', 'Hero Victory'),
('Gohan vs Cell', 'Earth', '1992-11-24', 'Hero Victory'),
('Goku vs Majin Vegeta', 'Earth', '2001-08-28', 'Draw'),
('Goku and Vegeta vs Kid Buu', 'Supreme Kai Planet', '2002-03-29', 'Hero Victory'),
('Vegito vs Super Buu', 'Earth', '2002-02-09', 'Hero Victory'),
('Goku vs Beerus', 'Earth', '2013-08-10', 'Villain Victory'),
('Goku vs Frieza - Resurrection', 'Earth', '2015-08-02', 'Hero Victory'),
('Goku vs Hit', 'Tournament Arena', '2016-02-21', 'Villain Victory'),
('Goku Ultra Instinct vs Jiren', 'Tournament of Power', '2018-03-18', 'Hero Victory'),
('Goku and Piccolo vs Raditz', 'Earth', '1989-04-19', 'Hero Victory'),
('Vegeta vs Dodoria', 'Planet Namek', '1990-07-18', 'Hero Victory'),
('Gohan vs Nappa', 'Earth', '1989-11-29', 'Hero Victory'),
('Goku vs Captain Ginyu', 'Planet Namek', '1990-11-28', 'Hero Victory'),
('Trunks vs Frieza - Future', 'Earth', '1991-08-03', 'Hero Victory'),
('Vegeta vs Semi-Perfect Cell', 'Earth', '1992-08-12', 'Villain Victory'),
('Gogeta vs Broly', 'Earth', '2018-12-14', 'Hero Victory'),
('Gotenks vs Super Buu', 'Hyperbolic Time Chamber', '2002-01-22', 'Draw'),
('Vegeta vs Android 19', 'Earth', '1992-03-11', 'Hero Victory'),
('Goku vs Pikkon', 'Other World', '1994-08-24', 'Hero Victory');

INSERT INTO Battle_Participants (Battle_ID, Character_ID, Transformation_ID, Power_Level_In_Battle, Was_Winner) VALUES
(1, 1, 7, 32000.00, FALSE),
(1, 2, 11, 180000.00, FALSE),
(2, 1, 1, 150000000.00, TRUE),
(2, 8, 8, 120000000.00, FALSE),
(3, 3, 2, 1000000000.00, TRUE),
(3, 9, 9, 900000000.00, FALSE),
(4, 1, 2, 800000000.00, FALSE),
(4, 2, 12, 850000000.00, FALSE),
(5, 1, 3, 1600000000.00, TRUE),
(5, 2, 2, 1000000000.00, TRUE),
(5, 10, 14, 1300000000.00, FALSE),
(6, 22, 1, 5000000000.00, TRUE),
(6, 10, 1, 2000000000.00, FALSE),
(7, 1, 4, 5000000000.00, FALSE),
(7, 18, 1, 50000000000.00, TRUE),
(8, 1, 5, 10000000000.00, TRUE),
(8, 8, 8, 12000000000.00, FALSE),
(9, 1, 5, 10000000000.00, FALSE),
(9, 19, 1, 30000000000.00, TRUE),
(10, 1, 6, 500000000000.00, TRUE),
(10, 20, 1, 480000000000.00, FALSE),
(11, 1, 7, 416.00, TRUE),
(11, 4, 1, 408.00, TRUE),
(11, 15, 1, 1500.00, FALSE),
(14, 1, 7, 360000.00, TRUE),
(15, 26, 1, 2850000.00, TRUE),
(15, 8, 9, 120000000.00, FALSE),
(17, 21, 5, 50000000000.00, TRUE),
(17, 17, 1, 45000000000.00, FALSE),
(12, 2, 1, 2500000.00, TRUE),
(13, 3, 1, 2800.00, TRUE),
(13, 16, 11, 40000.00, FALSE),
(16, 2, 1, 950000000.00, FALSE),
(16, 9, 9, 1100000000.00, TRUE),
(18, 23, 3, 6000000000.00, FALSE),
(18, 10, 14, 2500000000.00, FALSE),
(19, 2, 1, 475000000.00, TRUE),
(19, 13, NULL, 8500.00, FALSE),
(20, 1, 2, 1000000000.00, TRUE);

DROP VIEW IF EXISTS Battle_Summary_View;
CREATE VIEW Battle_Summary_View AS
SELECT 
    b.Battle_ID,
    b.Battle_Name,
    b.Location,
    b.Battle_Date,
    b.Outcome,
    COUNT(DISTINCT bp.Character_ID) AS Total_Fighters,
    AVG(bp.Power_Level_In_Battle) AS Avg_Power_Level,
    MAX(bp.Power_Level_In_Battle) AS Max_Power_Level
FROM Battles b
LEFT JOIN Battle_Participants bp ON b.Battle_ID = bp.Battle_ID
GROUP BY b.Battle_ID, b.Battle_Name, b.Location, b.Battle_Date, b.Outcome
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
    IN p_Base_Power_Level DECIMAL(15,2),
    IN p_Is_Alive BOOLEAN,
    IN p_Planet_Origin VARCHAR(50)
)
BEGIN
    INSERT INTO Characters (
        Character_Name, Race, Alignment, 
        Base_Power_Level, Is_Alive, Planet_Origin
    ) VALUES (
        p_Character_Name, p_Race, p_Alignment,
        p_Base_Power_Level, p_Is_Alive, p_Planet_Origin
    );
    
    SELECT LAST_INSERT_ID() AS Character_ID;
END $$
DELIMITER ;
