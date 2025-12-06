"""
Data Access Layer (DAL)
Handles all direct database interactions using stored procedures and views only.
"""

import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self, host, username, password, database, port=3306):
        self.host = host
        self.username = username
        self.password = password
        self.database = database
        self.port = port
        self.connection = None
    
    def connect(self):
        """Establish database connection"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.username,
                password=self.password,
                database=self.database,
                port=self.port
            )
            return self.connection.is_connected()
        except Error as e:
            print(f"Error connecting to database: {e}")
            return False
    
    def close(self):
        """Close database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
    
    def execute_procedure(self, procedure_name, params=None):
        """Execute stored procedure and return results"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            if params:
                cursor.callproc(procedure_name, params)
            else:
                cursor.callproc(procedure_name)
            
            results = []
            for result in cursor.stored_results():
                results.extend(result.fetchall())
            
            self.connection.commit()
            cursor.close()
            return results
        except Error as e:
            print(f"Error executing procedure {procedure_name}: {e}")
            return None
    
    def execute_query(self, query):
        """Execute a direct query (for views)"""
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error executing query: {e}")
            return None


class CharacterDAL:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def get_all_characters(self):
        """Get all characters using stored procedure"""
        return self.db.execute_procedure('Get_All_Characters')
    
    def get_character_details(self, character_id):
        """Get detailed character information"""
        return self.db.execute_procedure('Get_Character_Details', [character_id])
    
    def add_character(self, name, race, alignment, birth_date, base_power, is_alive, planet, first_appearance):
        """Add new character"""
        return self.db.execute_procedure('Add_Character', 
            [name, race, alignment, birth_date, base_power, is_alive, planet, first_appearance])
    
    def update_character(self, char_id, name, race, alignment, birth_date, base_power, is_alive, planet):
        """Update existing character"""
        return self.db.execute_procedure('Update_Character',
            [char_id, name, race, alignment, birth_date, base_power, is_alive, planet])
    
    def delete_character(self, character_id):
        """Delete character (cascades to related tables)"""
        return self.db.execute_procedure('Delete_Character', [character_id])
    
    def get_character_battle_history(self, character_id):
        """Get character's battle history with statistics"""
        return self.db.execute_procedure('Get_Character_Battle_History', [character_id])
    
    def get_character_transformations(self, character_id):
        """Get all transformations a character can use"""
        return self.db.execute_procedure('Get_Character_Transformations', [character_id])


class BattleDAL:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def get_all_battles(self):
        """Get all battles with summary information"""
        return self.db.execute_procedure('Get_All_Battles')
    
    def get_battle_details(self, battle_id):
        """Get detailed battle information including participants"""
        return self.db.execute_procedure('Get_Battle_Details', [battle_id])
    
    def add_battle(self, name, location, battle_date, start_time, duration, outcome, saga, destroyed_planet):
        """Add new battle"""
        return self.db.execute_procedure('Add_Battle',
            [name, location, battle_date, start_time, duration, outcome, saga, destroyed_planet])
    
    def update_battle(self, battle_id, name, location, battle_date, start_time, duration, outcome, saga, destroyed_planet):
        """Update existing battle"""
        return self.db.execute_procedure('Update_Battle',
            [battle_id, name, location, battle_date, start_time, duration, outcome, saga, destroyed_planet])
    
    def delete_battle(self, battle_id):
        """Delete battle (cascades to participants)"""
        return self.db.execute_procedure('Delete_Battle', [battle_id])
    
    def add_battle_participant(self, battle_id, character_id, transformation_id, power_level, damage_dealt, damage_taken, was_winner):
        """Add participant to battle"""
        return self.db.execute_procedure('Add_Battle_Participant',
            [battle_id, character_id, transformation_id, power_level, damage_dealt, damage_taken, was_winner])
    
    def get_saga_statistics(self):
        """Get aggregate statistics by saga"""
        return self.db.execute_procedure('Get_Saga_Statistics')


class TransformationDAL:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def get_all_transformations(self):
        """Get all transformations"""
        return self.db.execute_procedure('Get_All_Transformations')
