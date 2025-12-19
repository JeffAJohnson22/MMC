from DAL import CharacterDAL, BattleDAL

class CharacterBLL:
    def __init__(self, db_connection):
        self.dal = CharacterDAL(db_connection)
    
    def get_all_characters(self):
        characters = self.dal.get_all_characters()
        if characters:
            for char in characters:
                char['Status'] = 'Alive' if char.get('Is_Alive') else 'Deceased'
                if char.get('Base_Power_Level'):
                    char['Base_Power_Level_Display'] = f"{float(char['Base_Power_Level']):,.0f}"
        return characters
    
    def add_character(self, name, race, alignment, power_level, is_alive, planet):
        if not name or len(name) < 2:
            return {"error": "Name must be at least 2 characters"}
        if power_level < 0:
            return {"error": "Power level cannot be negative"}
        
        result = self.dal.add_character(name, race, alignment, 
                                       power_level, is_alive, planet)
        return result
    
    def update_character(self, character_id, name, power_level, is_alive):
        if not name or len(name) < 2:
            return {"error": "Name must be at least 2 characters"}
        if power_level < 0:
            return {"error": "Power level cannot be negative"}
        
        return self.dal.update_character(character_id, name, power_level, is_alive)
    
    def delete_character(self, character_id):
        return self.dal.delete_character(character_id)

class BattleBLL:
    def __init__(self, db_connection):
        self.dal = BattleDAL(db_connection)
    
    def get_all_battles(self):
        battles = self.dal.get_all_battles()
        if battles:
            for battle in battles:
                # Format large numbers
                if battle.get('Avg_Power_Level'):
                    battle['Avg_Power_Display'] = f"{float(battle['Avg_Power_Level']):,.0f}"
                if battle.get('Max_Power_Level'):
                    battle['Max_Power_Display'] = f"{float(battle['Max_Power_Level']):,.0f}"
        return battles
