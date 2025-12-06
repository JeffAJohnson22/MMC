"""
Business Logic Layer (BLL)
Contains business rules and validation logic.
Acts as intermediary between View and Data Access Layer.
"""

from DAL import CharacterDAL, BattleDAL, TransformationDAL
from datetime import datetime

class CharacterBLL:
    def __init__(self, db_connection):
        self.dal = CharacterDAL(db_connection)
    
    def get_all_characters(self):
        """Get all characters for display"""
        characters = self.dal.get_all_characters()
        if characters:
            # Format data for view
            for char in characters:
                char['Status'] = 'Alive' if char.get('Is_Alive') else 'Deceased'
                if char.get('Base_Power_Level'):
                    char['Base_Power_Level'] = f"{char['Base_Power_Level']:,.0f}"
                if char.get('Max_Power_Potential'):
                    char['Max_Power_Potential'] = f"{char['Max_Power_Potential']:,.0f}"
        return characters
    
    def get_character_details(self, character_id):
        """Get detailed character information"""
        return self.dal.get_character_details(character_id)
    
    def add_character(self, name, race, alignment, birth_date, base_power, is_alive, planet, first_appearance):
        """Add new character with validation"""
        # Validation
        if not name or len(name.strip()) == 0:
            return {'error': 'Character name is required'}
        
        try:
            base_power = float(base_power)
            if base_power < 0:
                return {'error': 'Base power level must be positive'}
        except ValueError:
            return {'error': 'Invalid power level'}
        
        # Convert string boolean to actual boolean
        is_alive_bool = is_alive in [True, 'True', 'true', 1, '1']
        
        result = self.dal.add_character(name, race, alignment, birth_date, 
                                       base_power, is_alive_bool, planet, first_appearance)
        return result
    
    def update_character(self, char_id, name, race, alignment, birth_date, base_power, is_alive, planet):
        """Update character with validation"""
        if not name or len(name.strip()) == 0:
            return {'error': 'Character name is required'}
        
        try:
            base_power = float(base_power)
            if base_power < 0:
                return {'error': 'Base power level must be positive'}
        except ValueError:
            return {'error': 'Invalid power level'}
        
        is_alive_bool = is_alive in [True, 'True', 'true', 1, '1']
        
        result = self.dal.update_character(char_id, name, race, alignment, 
                                          birth_date, base_power, is_alive_bool, planet)
        return result
    
    def delete_character(self, character_id):
        """Delete character"""
        return self.dal.delete_character(character_id)
    
    def get_character_battle_history(self, character_id):
        """Get formatted battle history"""
        history = self.dal.get_character_battle_history(character_id)
        if history:
            for battle in history:
                if battle.get('Power_Level_In_Battle'):
                    battle['Power_Level_In_Battle'] = f"{battle['Power_Level_In_Battle']:,.0f}"
                if battle.get('Damage_Dealt'):
                    battle['Damage_Dealt'] = f"{battle['Damage_Dealt']:,.0f}"
                if battle.get('Damage_Taken'):
                    battle['Damage_Taken'] = f"{battle['Damage_Taken']:,.0f}"
                battle['Result'] = 'Won' if battle.get('Was_Winner') else 'Lost'
        return history
    
    def get_character_transformations(self, character_id):
        """Get all transformations a character can use"""
        transformations = self.dal.get_character_transformations(character_id)
        if transformations:
            for trans in transformations:
                if trans.get('Power_Multiplier'):
                    trans['Multiplier'] = f"{trans['Power_Multiplier']}x"
                if trans.get('Max_Power_With_Transform'):
                    trans['Max_Power_With_Transform'] = f"{trans['Max_Power_With_Transform']:,.0f}"
        return transformations


class BattleBLL:
    def __init__(self, db_connection):
        self.dal = BattleDAL(db_connection)
    
    def get_all_battles(self):
        """Get all battles for display"""
        battles = self.dal.get_all_battles()
        if battles:
            for battle in battles:
                if battle.get('Avg_Power_Level'):
                    battle['Avg_Power_Level'] = f"{battle['Avg_Power_Level']:,.0f}"
                if battle.get('Max_Power_Level'):
                    battle['Max_Power_Level'] = f"{battle['Max_Power_Level']:,.0f}"
                if battle.get('Total_Damage'):
                    battle['Total_Damage'] = f"{battle['Total_Damage']:,.0f}"
                battle['Planet_Destroyed'] = 'Yes' if battle.get('Destroyed_Planet') else 'No'
        return battles
    
    def get_battle_details(self, battle_id):
        """Get detailed battle information"""
        details = self.dal.get_battle_details(battle_id)
        if details:
            for participant in details:
                if participant.get('Power_Level_In_Battle'):
                    participant['Power_Level_In_Battle'] = f"{participant['Power_Level_In_Battle']:,.0f}"
                if participant.get('Damage_Dealt'):
                    participant['Damage_Dealt'] = f"{participant['Damage_Dealt']:,.0f}"
                if participant.get('Damage_Taken'):
                    participant['Damage_Taken'] = f"{participant['Damage_Taken']:,.0f}"
        return details
    
    def add_battle(self, name, location, battle_date, start_time, duration, outcome, saga, destroyed_planet):
        """Add new battle with validation"""
        if not name or len(name.strip()) == 0:
            return {'error': 'Battle name is required'}
        
        if not location or len(location.strip()) == 0:
            return {'error': 'Location is required'}
        
        try:
            duration = int(duration)
            if duration <= 0:
                return {'error': 'Duration must be positive'}
        except ValueError:
            return {'error': 'Invalid duration'}
        
        destroyed_planet_bool = destroyed_planet in [True, 'True', 'true', 1, '1']
        
        result = self.dal.add_battle(name, location, battle_date, start_time, 
                                     duration, outcome, saga, destroyed_planet_bool)
        return result
    
    def update_battle(self, battle_id, name, location, battle_date, start_time, duration, outcome, saga, destroyed_planet):
        """Update battle with validation"""
        if not name or len(name.strip()) == 0:
            return {'error': 'Battle name is required'}
        
        try:
            duration = int(duration)
            if duration <= 0:
                return {'error': 'Duration must be positive'}
        except ValueError:
            return {'error': 'Invalid duration'}
        
        destroyed_planet_bool = destroyed_planet in [True, 'True', 'true', 1, '1']
        
        result = self.dal.update_battle(battle_id, name, location, battle_date, 
                                       start_time, duration, outcome, saga, destroyed_planet_bool)
        return result
    
    def delete_battle(self, battle_id):
        """Delete battle"""
        return self.dal.delete_battle(battle_id)
    
    def add_battle_participant(self, battle_id, character_id, transformation_id, 
                              power_level, damage_dealt, damage_taken, was_winner):
        """Add participant to battle"""
        try:
            power_level = float(power_level)
            damage_dealt = float(damage_dealt)
            damage_taken = float(damage_taken)
        except ValueError:
            return {'error': 'Invalid numeric values'}
        
        was_winner_bool = was_winner in [True, 'True', 'true', 1, '1']
        
        # If transformation_id is None or empty, pass None
        trans_id = transformation_id if transformation_id else None
        
        return self.dal.add_battle_participant(battle_id, character_id, trans_id,
                                              power_level, damage_dealt, damage_taken, was_winner_bool)
    
    def get_saga_statistics(self):
        """Get saga statistics"""
        stats = self.dal.get_saga_statistics()
        if stats:
            for saga in stats:
                if saga.get('Avg_Duration'):
                    saga['Avg_Duration'] = f"{saga['Avg_Duration']:.1f}"
        return stats


class TransformationBLL:
    def __init__(self, db_connection):
        self.dal = TransformationDAL(db_connection)
    
    def get_all_transformations(self):
        """Get all transformations"""
        transformations = self.dal.get_all_transformations()
        if transformations:
            for trans in transformations:
                if trans.get('Power_Multiplier'):
                    trans['Multiplier'] = f"{trans['Power_Multiplier']}x"
                if trans.get('Energy_Drain_Rate'):
                    trans['Energy_Drain_Rate'] = f"{trans['Energy_Drain_Rate']:.1f}"
        return transformations
