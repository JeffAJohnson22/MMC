"""
Simplified Business Logic Layer (BLL)
Contains validation logic between View and Data Access Layer
"""

from DAL import CharacterDAL, BattleDAL, TransformationDAL
from datetime import datetime

class CharacterBLL:
    def __init__(self, db_connection):
        self.dal = CharacterDAL(db_connection)
    
    def get_all_characters(self):
        """Get all characters with formatting"""
        characters = self.dal.get_all_characters()
        if characters:
            for char in characters:
                char['Status'] = 'Alive' if char.get('Is_Alive') else 'Deceased'
                if char.get('Base_Power_Level'):
                    char['Base_Power_Level_Display'] = f"{float(char['Base_Power_Level']):,.0f}"
        return characters
    
    def add_character(self, name, race, alignment, birth_date, power_level, is_alive, planet):
        """Add new character with validation"""
        # Validation
        if not name or len(name) < 2:
            return {"error": "Name must be at least 2 characters"}
        if power_level < 0:
            return {"error": "Power level cannot be negative"}
        
        # Convert birth_date string to date if needed
        if isinstance(birth_date, str):
            try:
                birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
            except:
                birth_date = None
        
        result = self.dal.add_character(name, race, alignment, birth_date, 
                                       power_level, is_alive, planet)
        return result
    
    def update_character(self, character_id, name, power_level, is_alive):
        """Update character with validation"""
        if power_level < 0:
            return {"error": "Power level cannot be negative"}
        
        return self.dal.update_character(character_id, name, power_level, is_alive)
    
    def delete_character(self, character_id):
        """Delete character (cascades to Battle_Participants)"""
        return self.dal.delete_character(character_id)

class BattleBLL:
    def __init__(self, db_connection):
        self.dal = BattleDAL(db_connection)
    
    def get_all_battles(self):
        """Get all battles with aggregate data formatted"""
        battles = self.dal.get_all_battles()
        if battles:
            for battle in battles:
                # Format large numbers
                if battle.get('Avg_Power_Level'):
                    battle['Avg_Power_Display'] = f"{float(battle['Avg_Power_Level']):,.0f}"
                if battle.get('Max_Power_Level'):
                    battle['Max_Power_Display'] = f"{float(battle['Max_Power_Level']):,.0f}"
                if battle.get('Total_Damage_Dealt'):
                    battle['Total_Damage_Display'] = f"{float(battle['Total_Damage_Dealt']):,.0f}"
        return battles
    
    def get_battles_list(self):
        """Get simple battle list for dropdowns"""
        return self.dal.get_battles_list()
    
    def add_battle_participant(self, battle_id, character_id, transformation_id,
                              power_level, damage_dealt, damage_taken, was_winner):
        """Add participant with validation"""
        if power_level < 0 or damage_dealt < 0 or damage_taken < 0:
            return {"error": "Values cannot be negative"}
        
        return self.dal.add_battle_participant(battle_id, character_id, transformation_id,
                                              power_level, damage_dealt, damage_taken, was_winner)

class TransformationBLL:
    def __init__(self, db_connection):
        self.dal = TransformationDAL(db_connection)
    
    def get_all_transformations(self):
        """Get all transformations"""
        return self.dal.get_all_transformations()
