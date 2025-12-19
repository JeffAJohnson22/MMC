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
        if self.connection and self.connection.is_connected():
            self.connection.close()
    
    def execute_procedure(self, procedure_name, params=None):
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
    
    def add_character(self, name, race, alignment, power_level, is_alive, planet):
        params = (name, race, alignment, power_level, is_alive, planet)
        return self.db.execute_procedure('Add_Character', params)
    
    def delete_character(self, character_id):
        try:
            cursor = self.db.connection.cursor()
            cursor.execute("DELETE FROM Characters WHERE Character_ID = %s", (character_id,))
            self.db.connection.commit()
            rows_deleted = cursor.rowcount
            cursor.close()
            return rows_deleted > 0
        except Error as e:
            print(f"Error deleting character: {e}")
            return False
    
    def get_all_characters(self):
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
        return self.db.execute_procedure('Get_All_Battles')
