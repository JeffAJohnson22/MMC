"""
Simplified Data Access Layer (DAL)
Handles database interactions using stored procedures
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

class CharacterDAL:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def add_character(self, name, race, alignment, birth_date, power_level, is_alive, planet):
        """Add new character"""
        params = (name, race, alignment, birth_date, power_level, is_alive, planet)
        return self.db.execute_procedure('Add_Character', params)
    
    def update_character(self, character_id, name, power_level, is_alive):
        """Update character"""
        params = (character_id, name, power_level, is_alive)
        return self.db.execute_procedure('Update_Character', params)
    
    def delete_character(self, character_id):
        """Delete character (cascades to Battle_Participants)"""
        return self.db.execute_procedure('Delete_Character', (character_id,))
    
    def get_all_characters(self):
        """Get all characters"""
        try:
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Characters ORDER BY Base_Power_Level DESC")
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error getting characters: {e}")
            return []

class BattleDAL:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def get_all_battles(self):
        """Get all battles with aggregate data"""
        return self.db.execute_procedure('Get_All_Battles')
    
    def add_battle_participant(self, battle_id, character_id, transformation_id, 
                               power_level, damage_dealt, damage_taken, was_winner):
        """Add participant to battle"""
        params = (battle_id, character_id, transformation_id, power_level, 
                 damage_dealt, damage_taken, was_winner)
        return self.db.execute_procedure('Add_Battle_Participant', params)
    
    def get_battles_list(self):
        """Get simple battle list"""
        try:
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute("SELECT Battle_ID, Battle_Name FROM Battles ORDER BY Battle_Date DESC")
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error getting battles: {e}")
            return []

class TransformationDAL:
    def __init__(self, db_connection):
        self.db = db_connection
    
    def get_all_transformations(self):
        """Get all transformations"""
        try:
            cursor = self.db.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM Transformations ORDER BY Power_Multiplier DESC")
            results = cursor.fetchall()
            cursor.close()
            return results
        except Error as e:
            print(f"Error getting transformations: {e}")
            return []
