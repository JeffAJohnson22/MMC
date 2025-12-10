-- Dragon Ball Z Database
-- Final Project - Jeff Johnson
-- CSC 6302

DROP DATABASE IF EXISTS DragonBallZ;
CREATE DATABASE DragonBallZ;
USE DragonBallZ;

-- Table 1: Characters (Main character information)
CREATE TABLE Characters (
    Character_ID INT AUTO_INCREMENT PRIMARY KEY,
    Character_Name VARCHAR(100) NOT NULL,
    Race ENUM('Saiyan', 'Namekian', 'Human', 'Android', 'Majin', 'Kai', 'Demon', 'Fusion', 'Other') NOT NULL,
    Alignment ENUM('Hero', 'Villain', 'Neutral') NOT NULL,
    Birth_Date DATE,
    Base_Power_Level DECIMAL(15, 2) NOT NULL,
    Is_Alive BOOLEAN DEFAULT TRUE,
    Planet_Origin VARCHAR(50),
    First_Appearance_Date DATE,
    UNIQUE(Character_Name)
);

-- Table 2: Transformations (Different forms characters can achieve)
CREATE TABLE Transformations (
    Transformation_ID INT AUTO_INCREMENT PRIMARY KEY,
    Transformation_Name VARCHAR(100) NOT NULL,
    Power_Multiplier DECIMAL(6, 2) NOT NULL,
    Energy_Drain_Rate DECIMAL(5, 2),
    Required_Power_Level DECIMAL(15, 2),
    Description TEXT,
    UNIQUE(Transformation_Name)
);

-- Table 3: Battles (Individual battle events)
CREATE TABLE Battles (
    Battle_ID INT AUTO_INCREMENT PRIMARY KEY,
    Battle_Name VARCHAR(150) NOT NULL,
    Location VARCHAR(100) NOT NULL,
    Battle_Date DATE NOT NULL,
    Start_Time TIME,
    Duration_Minutes INT,
    Outcome ENUM('Hero Victory', 'Villain Victory', 'Draw', 'Interrupted') NOT NULL,
    Saga VARCHAR(50),
    Destroyed_Planet BOOLEAN DEFAULT FALSE
);

-- Table 4: Battle_Participants (Composite Primary Key - tracks who fought in which battles)
-- This is the junction table with composite primary key
-- Links to Character_Transformations to ensure characters only use transformations they've unlocked
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
    -- Composite foreign key to Character_Transformations ensures data integrity
    FOREIGN KEY (Character_ID, Transformation_ID) REFERENCES Character_Transformations(Character_ID, Transformation_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Table 5: Character_Transformations (tracks which characters can use which transformations)
-- Another table with composite primary key
CREATE TABLE Character_Transformations (
    Character_ID INT NOT NULL,
    Transformation_ID INT NOT NULL,
    Date_Unlocked DATE,
    Mastery_Level TINYINT DEFAULT 1 CHECK (Mastery_Level BETWEEN 1 AND 10),
    PRIMARY KEY (Character_ID, Transformation_ID),
    FOREIGN KEY (Character_ID) REFERENCES Characters(Character_ID) ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (Transformation_ID) REFERENCES Transformations(Transformation_ID) ON DELETE CASCADE ON UPDATE CASCADE
);

-- Insert Characters (35 rows - exceeds minimum of 30)
INSERT INTO Characters (Character_Name, Race, Alignment, Birth_Date, Base_Power_Level, Is_Alive, Planet_Origin, First_Appearance_Date) VALUES
('Goku', 'Saiyan', 'Hero', '1984-04-16', 10000.00, TRUE, 'Vegeta', '1984-12-03'),
('Vegeta', 'Saiyan', 'Hero', '1982-01-01', 9500.00, TRUE, 'Vegeta', '1989-03-19'),
('Gohan', 'Saiyan', 'Hero', '2000-05-11', 8000.00, TRUE, 'Earth', '1989-10-18'),
('Piccolo', 'Namekian', 'Hero', '1988-05-09', 7500.00, TRUE, 'Namek', '1988-02-09'),
('Krillin', 'Human', 'Hero', '1980-10-29', 1500.00, TRUE, 'Earth', '1985-09-19'),
('Trunks', 'Saiyan', 'Hero', '2015-07-09', 7000.00, TRUE, 'Earth', '1991-07-10'),
('Goten', 'Saiyan', 'Hero', '2017-11-12', 6500.00, TRUE, 'Earth', '1993-11-10'),
('Frieza', 'Other', 'Villain', '1931-01-01', 12000.00, TRUE, 'Unknown', '1990-09-04'),
('Cell', 'Android', 'Villain', '1992-01-01', 11000.00, FALSE, 'Earth', '1992-01-29'),
('Majin Buu', 'Majin', 'Villain', '1000-01-01', 13000.00, TRUE, 'Unknown', '1994-03-06'),
('Yamcha', 'Human', 'Hero', '1981-03-20', 1200.00, TRUE, 'Earth', '1985-02-26'),
('Tien', 'Human', 'Hero', '1979-01-01', 1800.00, TRUE, 'Earth', '1985-11-12'),
('Android 17', 'Android', 'Neutral', '1990-01-01', 8500.00, TRUE, 'Earth', '1992-03-25'),
('Android 18', 'Android', 'Hero', '1990-01-01', 8500.00, TRUE, 'Earth', '1992-05-06'),
('Master Roshi', 'Human', 'Hero', '1850-01-01', 1000.00, TRUE, 'Earth', '1984-12-03'),
('Bulma', 'Human', 'Hero', '1982-08-18', 5.00, TRUE, 'Earth', '1984-12-03'),
('Chi-Chi', 'Human', 'Hero', '1983-05-12', 500.00, TRUE, 'Earth', '1987-11-11'),
('Raditz', 'Saiyan', 'Villain', '1983-01-01', 1500.00, FALSE, 'Vegeta', '1989-02-22'),
('Nappa', 'Saiyan', 'Villain', '1950-01-01', 4000.00, FALSE, 'Vegeta', '1989-11-29'),
('King Kai', 'Kai', 'Hero', '1000-01-01', 3500.00, TRUE, 'King Kai Planet', '1990-01-10'),
('Supreme Kai', 'Kai', 'Hero', '1000-01-01', 5000.00, TRUE, 'Sacred World of Kai', '1995-02-14'),
('Dabura', 'Demon', 'Villain', '1000-01-01', 9000.00, FALSE, 'Demon Realm', '1994-10-26'),
('Broly', 'Saiyan', 'Villain', '1984-04-16', 15000.00, TRUE, 'Vegeta', '1993-03-06'),
('Beerus', 'Other', 'Neutral', '1000-01-01', 50000.00, TRUE, 'Beerus Planet', '2013-03-30'),
('Whis', 'Other', 'Neutral', '1000-01-01', 100000.00, TRUE, 'Beerus Planet', '2013-03-30'),
('Hit', 'Other', 'Neutral', '1000-01-01', 30000.00, TRUE, 'Universe 6', '2015-12-06'),
('Jiren', 'Other', 'Hero', '1990-01-01', 80000.00, TRUE, 'Universe 11', '2017-10-08'),
('Gogeta', 'Fusion', 'Hero', NULL, 20000.00, TRUE, NULL, '1995-03-04'),
('Vegito', 'Fusion', 'Hero', NULL, 20000.00, TRUE, NULL, '1995-09-07'),
('Gotenks', 'Fusion', 'Hero', NULL, 12000.00, TRUE, NULL, '1995-07-05'),
('Pikkon', 'Other', 'Hero', NULL, 8000.00, TRUE, 'Other World', '1994-03-23'),
('Mr. Satan', 'Human', 'Hero', '1970-04-07', 10.00, TRUE, 'Earth', '1993-06-09'),
('Videl', 'Human', 'Hero', '2001-01-01', 300.00, TRUE, 'Earth', '1993-09-01'),
('Future Trunks', 'Saiyan', 'Hero', '2002-01-01', 8500.00, TRUE, 'Earth', '1991-07-10'),
('Bardock', 'Saiyan', 'Hero', '1960-01-01', 10000.00, FALSE, 'Vegeta', '1990-10-17');

-- Insert Transformations
INSERT INTO Transformations (Transformation_Name, Power_Multiplier, Energy_Drain_Rate, Required_Power_Level, Description) VALUES
('Super Saiyan', 50.00, 5.50, 3000.00, 'The legendary transformation of the Saiyan race, golden hair and aura'),
('Super Saiyan 2', 100.00, 8.00, 10000.00, 'An ascended form beyond Super Saiyan with lightning aura'),
('Super Saiyan 3', 400.00, 15.00, 30000.00, 'Ultimate form with long golden hair and massive power drain'),
('Super Saiyan God', 500.00, 3.00, 50000.00, 'Divine transformation with red hair and godly ki'),
('Super Saiyan Blue', 1000.00, 7.00, 100000.00, 'Combination of Super Saiyan and God ki with blue hair'),
('Ultra Instinct', 5000.00, 20.00, 500000.00, 'Autonomous movement technique with silver hair'),
('Great Ape', 10.00, 2.00, 1000.00, 'Saiyan transformation into giant ape form under full moon'),
('Kaioken', 2.00, 10.00, 500.00, 'Technique that multiplies power at the cost of body strain'),
('Potential Unleashed', 200.00, 1.00, 5000.00, 'Unlocks hidden potential without physical transformation'),
('Fusion', 100.00, 5.00, 2000.00, 'Fusion dance or Potara earrings combining two warriors'),
('Golden Frieza', 100.00, 12.00, 12000.00, 'Frieza golden transformation matching Super Saiyan power'),
('Perfect Form', 50.00, 3.00, 5000.00, 'Cell or Frieza achieving their perfect state'),
('Majin', 2.50, 8.00, 3000.00, 'Dark magic enhancement from Babidi'),
('Super Saiyan Rage', 150.00, 10.00, 8000.00, 'Unique transformation combining Super Saiyan and rage'),
('Ultra Ego', 4000.00, 18.00, 400000.00, 'Destruction God technique that grows stronger from damage');

-- Insert Battles (30+ rows)
INSERT INTO Battles (Battle_Name, Location, Battle_Date, Start_Time, Duration_Minutes, Outcome, Saga, Destroyed_Planet) VALUES
('Goku vs Vegeta - First Encounter', 'Earth', '1989-12-13', '18:30:00', 120, 'Draw', 'Saiyan Saga', FALSE),
('Goku vs Frieza', 'Planet Namek', '1991-08-31', '14:00:00', 240, 'Hero Victory', 'Frieza Saga', TRUE),
('Gohan vs Cell', 'Earth', '1992-11-24', '15:45:00', 90, 'Hero Victory', 'Cell Saga', FALSE),
('Goku vs Majin Vegeta', 'Earth', '2001-08-28', '20:00:00', 60, 'Draw', 'Majin Buu Saga', FALSE),
('Goku and Vegeta vs Kid Buu', 'Supreme Kai Planet', '2002-03-29', '16:00:00', 150, 'Hero Victory', 'Majin Buu Saga', FALSE),
('Vegito vs Super Buu', 'Earth', '2002-02-09', '13:30:00', 45, 'Hero Victory', 'Majin Buu Saga', FALSE),
('Goku vs Beerus', 'Earth', '2013-08-10', '19:00:00', 75, 'Villain Victory', 'Battle of Gods', FALSE),
('Goku vs Frieza - Resurrection', 'Earth', '2015-08-02', '12:00:00', 90, 'Hero Victory', 'Resurrection F', FALSE),
('Goku vs Hit', 'Tournament Arena', '2016-02-21', '10:00:00', 30, 'Villain Victory', 'Universe 6 Saga', FALSE),
('Goku Black vs Future Trunks', 'Future Earth', '2016-08-14', '14:30:00', 45, 'Villain Victory', 'Future Trunks Saga', FALSE),
('Vegito Blue vs Fused Zamasu', 'Future Earth', '2016-11-13', '16:00:00', 60, 'Interrupted', 'Future Trunks Saga', FALSE),
('Goku vs Jiren - First Fight', 'Tournament of Power', '2017-10-08', '11:00:00', 20, 'Villain Victory', 'Tournament of Power', FALSE),
('Goku Ultra Instinct vs Jiren', 'Tournament of Power', '2018-03-18', '10:30:00', 48, 'Hero Victory', 'Tournament of Power', FALSE),
('Piccolo vs Raditz', 'Earth', '1989-04-19', '11:00:00', 45, 'Hero Victory', 'Saiyan Saga', FALSE),
('Vegeta vs Dodoria', 'Planet Namek', '1990-07-18', '09:00:00', 15, 'Hero Victory', 'Frieza Saga', FALSE),
('Gohan vs Nappa', 'Earth', '1989-11-29', '14:00:00', 30, 'Hero Victory', 'Saiyan Saga', FALSE),
('Goku vs Captain Ginyu', 'Planet Namek', '1990-11-28', '13:00:00', 40, 'Hero Victory', 'Frieza Saga', FALSE),
('Trunks vs Frieza - Future', 'Earth', '1991-08-03', '10:00:00', 5, 'Hero Victory', 'Android Saga', FALSE),
('Piccolo vs Android 17', 'Earth', '1992-05-27', '15:00:00', 35, 'Draw', 'Android Saga', FALSE),
('Vegeta vs Semi-Perfect Cell', 'Earth', '1992-08-12', '16:30:00', 25, 'Villain Victory', 'Cell Saga', FALSE),
('Gohan vs Dabura', 'Earth', '2001-03-20', '13:00:00', 40, 'Interrupted', 'Majin Buu Saga', FALSE),
('Goku vs Yakon', 'Babidi Ship', '2001-03-06', '18:00:00', 10, 'Hero Victory', 'Majin Buu Saga', FALSE),
('Vegeta vs Pui Pui', 'Babidi Ship', '2001-02-27', '17:00:00', 8, 'Hero Victory', 'Majin Buu Saga', FALSE),
('Gogeta vs Broly', 'Earth', '2018-12-14', '14:00:00', 60, 'Hero Victory', 'Broly Movie', FALSE),
('Goku and Vegeta vs Broly', 'Arctic', '2018-12-14', '13:00:00', 90, 'Interrupted', 'Broly Movie', FALSE),
('Gotenks vs Super Buu', 'Hyperbolic Time Chamber', '2002-01-22', '12:00:00', 30, 'Draw', 'Majin Buu Saga', FALSE),
('Piccolo and Gohan vs Nappa', 'Earth', '1989-11-29', '13:30:00', 45, 'Hero Victory', 'Saiyan Saga', FALSE),
('Vegeta vs Android 19', 'Earth', '1992-03-11', '11:00:00', 20, 'Hero Victory', 'Android Saga', FALSE),
('Trunks vs Cell - First Form', 'Earth', '1992-06-03', '10:30:00', 25, 'Draw', 'Cell Saga', FALSE),
('Krillin vs Frieza Soldiers', 'Planet Namek', '1990-06-13', '08:00:00', 30, 'Hero Victory', 'Frieza Saga', FALSE),
('Goku vs Pikkon', 'Other World', '1994-08-24', '12:00:00', 35, 'Hero Victory', 'Other World Tournament', FALSE),
('Android 17 vs Piccolo', 'Earth', '1992-05-27', '15:00:00', 40, 'Draw', 'Android Saga', FALSE),
('Vegeta vs Toppo', 'Tournament of Power', '2018-02-11', '10:45:00', 25, 'Hero Victory', 'Tournament of Power', FALSE);

-- Insert Character_Transformations
INSERT INTO Character_Transformations (Character_ID, Transformation_ID, Date_Unlocked, Mastery_Level) VALUES
(1, 1, '1991-03-03', 10), -- Goku Super Saiyan
(1, 2, '1993-11-17', 9),  -- Goku Super Saiyan 2
(1, 3, '1994-11-01', 7),  -- Goku Super Saiyan 3
(1, 4, '2013-03-30', 9),  -- Goku Super Saiyan God
(1, 5, '2015-04-18', 10), -- Goku Super Saiyan Blue
(1, 6, '2017-10-08', 8),  -- Goku Ultra Instinct
(1, 8, '1990-01-10', 10), -- Goku Kaioken
(2, 1, '1992-01-13', 10), -- Vegeta Super Saiyan
(2, 2, '1994-03-08', 9),  -- Vegeta Super Saiyan 2
(2, 4, '2013-03-30', 8),  -- Vegeta Super Saiyan God
(2, 5, '2015-04-18', 10), -- Vegeta Super Saiyan Blue
(2, 15, '2021-12-19', 7), -- Vegeta Ultra Ego
(3, 1, '1992-06-10', 9),  -- Gohan Super Saiyan
(3, 2, '1992-11-11', 10), -- Gohan Super Saiyan 2
(3, 9, '2001-09-16', 10), -- Gohan Potential Unleashed
(6, 1, '1992-05-20', 9),  -- Trunks Super Saiyan
(6, 2, '1992-09-02', 8),  -- Trunks Super Saiyan 2
(7, 1, '1993-05-26', 7),  -- Goten Super Saiyan
(8, 11, '2015-04-18', 9), -- Frieza Golden
(9, 12, '1992-05-27', 10),-- Cell Perfect Form
(10, 12, '2001-03-19', 9),-- Majin Buu transformations
(28, 1, '1995-03-04', 10),-- Gogeta Super Saiyan
(28, 5, '2018-12-14', 10),-- Gogeta Blue
(29, 1, '1995-09-07', 10),-- Vegito Super Saiyan
(29, 5, '2016-11-13', 10),-- Vegito Blue
(30, 1, '1995-07-05', 8), -- Gotenks Super Saiyan
(30, 3, '1995-08-02', 7), -- Gotenks Super Saiyan 3
(2, 13, '2001-08-28', 9), -- Vegeta Majin
(34, 1, '1991-06-10', 9), -- Future Trunks Super Saiyan
(34, 14, '2016-08-28', 8);-- Future Trunks Super Saiyan Rage

-- Insert Battle_Participants (linking battles to characters)
INSERT INTO Battle_Participants (Battle_ID, Character_ID, Transformation_ID, Power_Level_In_Battle, Damage_Dealt, Damage_Taken, Was_Winner) VALUES
-- Battle 1: Goku vs Vegeta First
(1, 1, 8, 32000.00, 15000.00, 18000.00, FALSE),
(1, 2, 7, 180000.00, 18000.00, 15000.00, FALSE),
-- Battle 2: Goku vs Frieza
(2, 1, 1, 150000000.00, 100000000.00, 50000000.00, TRUE),
(2, 8, 12, 120000000.00, 50000000.00, 100000000.00, FALSE),
-- Battle 3: Gohan vs Cell
(3, 3, 2, 1000000000.00, 500000000.00, 200000000.00, TRUE),
(3, 9, 12, 900000000.00, 200000000.00, 500000000.00, FALSE),
-- Battle 4: Goku vs Majin Vegeta
(4, 1, 2, 800000000.00, 350000000.00, 350000000.00, FALSE),
(4, 2, 13, 850000000.00, 350000000.00, 350000000.00, FALSE),
-- Battle 5: Goku/Vegeta vs Kid Buu
(5, 1, 3, 1600000000.00, 800000000.00, 400000000.00, TRUE),
(5, 2, 2, 1000000000.00, 500000000.00, 300000000.00, TRUE),
(5, 10, NULL, 1300000000.00, 700000000.00, 1300000000.00, FALSE),
-- Battle 6: Vegito vs Super Buu
(6, 29, 1, 5000000000.00, 3000000000.00, 500000000.00, TRUE),
(6, 10, NULL, 2000000000.00, 500000000.00, 3000000000.00, FALSE),
-- Battle 7: Goku vs Beerus
(7, 1, 4, 5000000000.00, 2000000000.00, 8000000000.00, FALSE),
(7, 24, NULL, 50000000000.00, 8000000000.00, 2000000000.00, TRUE),
-- Battle 8: Goku vs Frieza Resurrection
(8, 1, 5, 10000000000.00, 12000000000.00, 5000000000.00, TRUE),
(8, 8, 11, 12000000000.00, 5000000000.00, 12000000000.00, FALSE),
-- Battle 9: Goku vs Hit
(9, 1, 5, 10000000000.00, 15000000000.00, 20000000000.00, FALSE),
(9, 26, NULL, 30000000000.00, 20000000000.00, 15000000000.00, TRUE),
-- Battle 13: Goku UI vs Jiren
(13, 1, 6, 500000000000.00, 600000000000.00, 400000000000.00, TRUE),
(13, 27, NULL, 480000000000.00, 400000000000.00, 600000000000.00, FALSE),
-- Battle 14: Piccolo/Goku vs Raditz
(14, 1, NULL, 416.00, 924.00, 600.00, TRUE),
(14, 4, NULL, 408.00, 1330.00, 400.00, TRUE),
(14, 18, NULL, 1500.00, 1000.00, 1754.00, FALSE),
-- Battle 17: Goku vs Ginyu
(17, 1, 8, 360000.00, 120000.00, 80000.00, TRUE),
-- Battle 18: Future Trunks vs Frieza
(18, 34, 1, 2850000.00, 120000000.00, 1000.00, TRUE),
(18, 8, 12, 120000000.00, 1000.00, 120000000.00, FALSE),
-- Battle 24: Gogeta vs Broly
(24, 28, 5, 50000000000.00, 75000000000.00, 10000000000.00, TRUE),
(24, 23, 1, 45000000000.00, 10000000000.00, 75000000000.00, FALSE),
-- Additional participants for variety
(15, 2, 1, 2500000.00, 22000.00, 5000.00, TRUE),
(16, 3, NULL, 2800.00, 4000.00, 3000.00, TRUE),
(16, 19, 7, 40000.00, 3000.00, 4000.00, FALSE),
(19, 4, NULL, 8000000.00, 15000000.00, 10000000.00, FALSE),
(19, 13, NULL, 8500000.00, 10000000.00, 15000000.00, FALSE),
(20, 2, 1, 950000000.00, 500000000.00, 800000000.00, FALSE),
(20, 9, 12, 1100000000.00, 800000000.00, 500000000.00, TRUE),
(26, 30, 3, 6000000000.00, 2000000000.00, 1500000000.00, FALSE),
(26, 10, NULL, 2500000000.00, 1500000000.00, 2000000000.00, FALSE),
(28, 2, 1, 950000000.00, 8500000.00, 2000000.00, TRUE),
(30, 5, NULL, 1500.00, 5000.00, 2000.00, TRUE),
(33, 2, 5, 50000000000.00, 80000000000.00, 40000000000.00, TRUE);

-- ============================================================================
-- STORED PROCEDURES AND VIEWS
-- ============================================================================

-- VIEW 1: Battle Summary with Aggregates (requirement: aggregate function)
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
    SUM(bp.Damage_Dealt) AS Total_Damage,
    b.Destroyed_Planet
FROM Battles b
LEFT JOIN Battle_Participants bp ON b.Battle_ID = bp.Battle_ID
GROUP BY b.Battle_ID, b.Battle_Name, b.Location, b.Battle_Date, b.Start_Time, 
         b.Duration_Minutes, b.Outcome, b.Saga, b.Destroyed_Planet
ORDER BY b.Battle_Date DESC;

-- VIEW 2: Character Power Rankings
DROP VIEW IF EXISTS Character_Power_Rankings;
CREATE VIEW Character_Power_Rankings AS
SELECT 
    c.Character_ID,
    c.Character_Name,
    c.Race,
    c.Alignment,
    c.Base_Power_Level,
    c.Is_Alive,
    COUNT(DISTINCT ct.Transformation_ID) AS Total_Transformations,
    MAX(t.Power_Multiplier) AS Max_Multiplier,
    ROUND(c.Base_Power_Level * COALESCE(MAX(t.Power_Multiplier), 1), 2) AS Max_Power_Potential,
    COUNT(DISTINCT bp.Battle_ID) AS Battles_Participated
FROM Characters c
LEFT JOIN Character_Transformations ct ON c.Character_ID = ct.Character_ID
LEFT JOIN Transformations t ON ct.Transformation_ID = t.Transformation_ID
LEFT JOIN Battle_Participants bp ON c.Character_ID = bp.Character_ID
GROUP BY c.Character_ID, c.Character_Name, c.Race, c.Alignment, c.Base_Power_Level, c.Is_Alive
ORDER BY Max_Power_Potential DESC;

-- PROCEDURE 1: Get All Battles (READ with aggregation)
DROP PROCEDURE IF EXISTS Get_All_Battles;
DELIMITER //
CREATE PROCEDURE Get_All_Battles()
BEGIN
    SELECT * FROM Battle_Summary_View;
END //
DELIMITER ;

-- PROCEDURE 2: Get Battle Details (READ)
DROP PROCEDURE IF EXISTS Get_Battle_Details;
DELIMITER //
CREATE PROCEDURE Get_Battle_Details(IN p_Battle_ID INT)
BEGIN
    SELECT 
        b.Battle_ID,
        b.Battle_Name,
        b.Location,
        b.Battle_Date,
        b.Start_Time,
        b.Duration_Minutes,
        b.Outcome,
        b.Saga,
        b.Destroyed_Planet,
        c.Character_Name,
        c.Race,
        bp.Power_Level_In_Battle,
        t.Transformation_Name,
        bp.Damage_Dealt,
        bp.Damage_Taken,
        bp.Was_Winner
    FROM Battles b
    JOIN Battle_Participants bp ON b.Battle_ID = bp.Battle_ID
    JOIN Characters c ON bp.Character_ID = c.Character_ID
    LEFT JOIN Transformations t ON bp.Transformation_ID = t.Transformation_ID
    WHERE b.Battle_ID = p_Battle_ID
    ORDER BY bp.Power_Level_In_Battle DESC;
END //
DELIMITER ;

-- PROCEDURE 3: Get All Characters (READ)
DROP PROCEDURE IF EXISTS Get_All_Characters;
DELIMITER //
CREATE PROCEDURE Get_All_Characters()
BEGIN
    SELECT * FROM Character_Power_Rankings;
END //
DELIMITER ;

-- PROCEDURE 4: Get Character Details
DROP PROCEDURE IF EXISTS Get_Character_Details;
DELIMITER //
CREATE PROCEDURE Get_Character_Details(IN p_Character_ID INT)
BEGIN
    SELECT 
        c.*,
        COUNT(DISTINCT ct.Transformation_ID) AS Total_Transformations,
        COUNT(DISTINCT bp.Battle_ID) AS Total_Battles
    FROM Characters c
    LEFT JOIN Character_Transformations ct ON c.Character_ID = ct.Character_ID
    LEFT JOIN Battle_Participants bp ON c.Character_ID = bp.Character_ID
    WHERE c.Character_ID = p_Character_ID
    GROUP BY c.Character_ID;
    
    -- Also get transformations
    SELECT 
        t.Transformation_Name,
        t.Power_Multiplier,
        ct.Date_Unlocked,
        ct.Mastery_Level
    FROM Character_Transformations ct
    JOIN Transformations t ON ct.Transformation_ID = t.Transformation_ID
    WHERE ct.Character_ID = p_Character_ID;
END //
DELIMITER ;

-- PROCEDURE 5: Add New Character (CREATE)
DROP PROCEDURE IF EXISTS Add_Character;
DELIMITER //
CREATE PROCEDURE Add_Character(
    IN p_Character_Name VARCHAR(100),
    IN p_Race ENUM('Saiyan', 'Namekian', 'Human', 'Android', 'Majin', 'Kai', 'Demon', 'Fusion', 'Other'),
    IN p_Alignment ENUM('Hero', 'Villain', 'Neutral'),
    IN p_Birth_Date DATE,
    IN p_Base_Power_Level DECIMAL(15,2),
    IN p_Is_Alive BOOLEAN,
    IN p_Planet_Origin VARCHAR(50),
    IN p_First_Appearance_Date DATE
)
BEGIN
    INSERT INTO Characters (
        Character_Name, Race, Alignment, Birth_Date, 
        Base_Power_Level, Is_Alive, Planet_Origin, First_Appearance_Date
    ) VALUES (
        p_Character_Name, p_Race, p_Alignment, p_Birth_Date,
        p_Base_Power_Level, p_Is_Alive, p_Planet_Origin, p_First_Appearance_Date
    );
    
    SELECT LAST_INSERT_ID() AS Character_ID;
END //
DELIMITER ;

-- PROCEDURE 6: Update Character (UPDATE with CASCADE)
DROP PROCEDURE IF EXISTS Update_Character;
DELIMITER //
CREATE PROCEDURE Update_Character(
    IN p_Character_ID INT,
    IN p_Character_Name VARCHAR(100),
    IN p_Race ENUM('Saiyan', 'Namekian', 'Human', 'Android', 'Majin', 'Kai', 'Demon', 'Fusion', 'Other'),
    IN p_Alignment ENUM('Hero', 'Villain', 'Neutral'),
    IN p_Birth_Date DATE,
    IN p_Base_Power_Level DECIMAL(15,2),
    IN p_Is_Alive BOOLEAN,
    IN p_Planet_Origin VARCHAR(50)
)
BEGIN
    -- Update will cascade to related tables due to foreign key constraints
    UPDATE Characters
    SET 
        Character_Name = p_Character_Name,
        Race = p_Race,
        Alignment = p_Alignment,
        Birth_Date = p_Birth_Date,
        Base_Power_Level = p_Base_Power_Level,
        Is_Alive = p_Is_Alive,
        Planet_Origin = p_Planet_Origin
    WHERE Character_ID = p_Character_ID;
    
    SELECT ROW_COUNT() AS Rows_Affected;
END //
DELIMITER ;

-- PROCEDURE 7: Delete Character (DELETE with CASCADE)
DROP PROCEDURE IF EXISTS Delete_Character;
DELIMITER //
CREATE PROCEDURE Delete_Character(IN p_Character_ID INT)
BEGIN
    -- Delete will cascade to Battle_Participants and Character_Transformations
    DELETE FROM Characters WHERE Character_ID = p_Character_ID;
    
    SELECT ROW_COUNT() AS Rows_Deleted;
END //
DELIMITER ;

-- PROCEDURE 8: Add New Battle (CREATE)
DROP PROCEDURE IF EXISTS Add_Battle;
DELIMITER //
CREATE PROCEDURE Add_Battle(
    IN p_Battle_Name VARCHAR(150),
    IN p_Location VARCHAR(100),
    IN p_Battle_Date DATE,
    IN p_Start_Time TIME,
    IN p_Duration_Minutes INT,
    IN p_Outcome ENUM('Hero Victory', 'Villain Victory', 'Draw', 'Interrupted'),
    IN p_Saga VARCHAR(50),
    IN p_Destroyed_Planet BOOLEAN
)
BEGIN
    INSERT INTO Battles (
        Battle_Name, Location, Battle_Date, Start_Time, 
        Duration_Minutes, Outcome, Saga, Destroyed_Planet
    ) VALUES (
        p_Battle_Name, p_Location, p_Battle_Date, p_Start_Time,
        p_Duration_Minutes, p_Outcome, p_Saga, p_Destroyed_Planet
    );
    
    SELECT LAST_INSERT_ID() AS Battle_ID;
END //
DELIMITER ;

-- PROCEDURE 9: Update Battle (UPDATE with CASCADE)
DROP PROCEDURE IF EXISTS Update_Battle;
DELIMITER //
CREATE PROCEDURE Update_Battle(
    IN p_Battle_ID INT,
    IN p_Battle_Name VARCHAR(150),
    IN p_Location VARCHAR(100),
    IN p_Battle_Date DATE,
    IN p_Start_Time TIME,
    IN p_Duration_Minutes INT,
    IN p_Outcome ENUM('Hero Victory', 'Villain Victory', 'Draw', 'Interrupted'),
    IN p_Saga VARCHAR(50),
    IN p_Destroyed_Planet BOOLEAN
)
BEGIN
    UPDATE Battles
    SET 
        Battle_Name = p_Battle_Name,
        Location = p_Location,
        Battle_Date = p_Battle_Date,
        Start_Time = p_Start_Time,
        Duration_Minutes = p_Duration_Minutes,
        Outcome = p_Outcome,
        Saga = p_Saga,
        Destroyed_Planet = p_Destroyed_Planet
    WHERE Battle_ID = p_Battle_ID;
    
    SELECT ROW_COUNT() AS Rows_Affected;
END //
DELIMITER ;

-- PROCEDURE 10: Delete Battle (DELETE with CASCADE)
DROP PROCEDURE IF EXISTS Delete_Battle;
DELIMITER //
CREATE PROCEDURE Delete_Battle(IN p_Battle_ID INT)
BEGIN
    -- Delete will cascade to Battle_Participants
    DELETE FROM Battles WHERE Battle_ID = p_Battle_ID;
    
    SELECT ROW_COUNT() AS Rows_Deleted;
END //
DELIMITER ;

-- PROCEDURE 11: Add Battle Participant
DROP PROCEDURE IF EXISTS Add_Battle_Participant;
DELIMITER //
CREATE PROCEDURE Add_Battle_Participant(
    IN p_Battle_ID INT,
    IN p_Character_ID INT,
    IN p_Transformation_ID INT,
    IN p_Power_Level DECIMAL(15,2),
    IN p_Damage_Dealt DECIMAL(12,2),
    IN p_Damage_Taken DECIMAL(12,2),
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
END //
DELIMITER ;

-- PROCEDURE 12: Get All Transformations
DROP PROCEDURE IF EXISTS Get_All_Transformations;
DELIMITER //
CREATE PROCEDURE Get_All_Transformations()
BEGIN
    SELECT * FROM Transformations ORDER BY Power_Multiplier DESC;
END //
DELIMITER ;

-- PROCEDURE 13: Get Character Battle History (with aggregates)
DROP PROCEDURE IF EXISTS Get_Character_Battle_History;
DELIMITER //
CREATE PROCEDURE Get_Character_Battle_History(IN p_Character_ID INT)
BEGIN
    SELECT 
        b.Battle_Name,
        b.Battle_Date,
        b.Location,
        b.Outcome,
        b.Saga,
        bp.Power_Level_In_Battle,
        t.Transformation_Name,
        bp.Damage_Dealt,
        bp.Damage_Taken,
        bp.Was_Winner,
        COUNT(*) OVER() AS Total_Battles,
        SUM(bp.Was_Winner) OVER() AS Total_Wins
    FROM Battle_Participants bp
    JOIN Battles b ON bp.Battle_ID = b.Battle_ID
    LEFT JOIN Transformations t ON bp.Transformation_ID = t.Transformation_ID
    WHERE bp.Character_ID = p_Character_ID
    ORDER BY b.Battle_Date DESC;
END //
DELIMITER ;

-- PROCEDURE 14: Get Transformation Users
DROP PROCEDURE IF EXISTS Get_Transformation_Users;
DELIMITER //
CREATE PROCEDURE Get_Transformation_Users(IN p_Transformation_ID INT)
BEGIN
    SELECT 
        c.Character_Name,
        c.Race,
        c.Base_Power_Level,
        ct.Date_Unlocked,
        ct.Mastery_Level,
        t.Transformation_Name,
        t.Power_Multiplier,
        ROUND(c.Base_Power_Level * t.Power_Multiplier, 2) AS Max_Power_With_Transform
    FROM Character_Transformations ct
    JOIN Characters c ON ct.Character_ID = c.Character_ID
    JOIN Transformations t ON ct.Transformation_ID = t.Transformation_ID
    WHERE ct.Transformation_ID = p_Transformation_ID
    ORDER BY Max_Power_With_Transform DESC;
END //
DELIMITER ;

-- PROCEDURE 15: Get Saga Statistics (aggregate function)
DROP PROCEDURE IF EXISTS Get_Saga_Statistics;
DELIMITER //
CREATE PROCEDURE Get_Saga_Statistics()
BEGIN
    SELECT 
        Saga,
        COUNT(*) AS Total_Battles,
        AVG(Duration_Minutes) AS Avg_Duration,
        SUM(CASE WHEN Destroyed_Planet = TRUE THEN 1 ELSE 0 END) AS Planets_Destroyed,
        SUM(CASE WHEN Outcome = 'Hero Victory' THEN 1 ELSE 0 END) AS Hero_Victories,
        SUM(CASE WHEN Outcome = 'Villain Victory' THEN 1 ELSE 0 END) AS Villain_Victories
    FROM Battles
    WHERE Saga IS NOT NULL
    GROUP BY Saga
    ORDER BY Total_Battles DESC;
END //
DELIMITER ;

-- Show summary
SELECT 'Database Created Successfully!' AS Status;
SELECT COUNT(*) AS Total_Characters FROM Characters;
SELECT COUNT(*) AS Total_Transformations FROM Transformations;
SELECT COUNT(*) AS Total_Battles FROM Battles;
SELECT COUNT(*) AS Total_Battle_Participants FROM Battle_Participants;
