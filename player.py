from race import Elf, Dwarf, Race, Orc

class Player(object):
    """
    Player class: Represents a player character in the game.

    Args:
        name (str): The name of the player character.
    
    Attributes:
        player (str): The name of the player character.
        lives (int): The number of lives the player has.
        level (int): The level of the player character.
        damage (int): The base damage inflicted by the player character.
        hit_points (int): The current hit points of the player character.
        score (float): The current score of the player character.
        race (Race): The chosen race instance for the player character.
        race_name (str): The name of the chosen race.
        skills (dict): A dictionary of player skills.
        alive (bool): Indicates if the player character is alive.

    Note:
        The player's damage and hit points are initialized based on the initial level.
    """
    def __init__(self, name):
        self.name = name
        self._lives = 1
        self._level = 1
        self._damage = 5
        self._hit_points = self._level * 10
        self._score = 0
        self.race = None
        self.race_name = None
        self.skills = {}
        self.alive = True

    def _get_lives(self):
        return self._lives
    
    def _get_score(self):
        return self.score

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):
        return self._level


    lives = property(_get_lives, _set_lives,_get_score)

    @property 
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
        
    
    def take_damage(self, damage):
        if self.race and hasattr(self.race, 'dodges') and self.race.dodges():
            return("**** Player dodge *****")
        elif self.race and hasattr(self.race, 'block') and self.race.block():
            return("**** Player block *****")
        else:
            total_hit_points = self._hit_points
            remaining_points = total_hit_points - damage

            if remaining_points >= 0:
                self._hit_points = remaining_points  # Update hit points
                return "Player took {1} points damage and has {2} hit points left.".format(self, damage, self._hit_points)
            else:
                self._lives -= 1
                
                if self._lives > 0:
                    self._hit_points = self._level * 10 + self.race.extra_hit_points
                    return "Player lost a life".format(self)
                else:
                    self.alive = False
                    return "Player is dead".format(self)

    def add_skill(self, skill_name, skill_function):
        self.skills[skill_name] = skill_function
        
    def apply_race_bonuses(self):
        if self.race:
            self._damage += self.race.bonus_dmg  # Add bonus damage from the race to the player's damage
            self._hit_points += self.race.extra_hit_points  # Add extra hit points from the race to the player's hit points
            
            for attribute in dir(self.race):
                if not attribute.startswith('__') and not callable(getattr(self.race, attribute)):
                    if not hasattr(self, attribute):
                        setattr(self, attribute, getattr(self.race, attribute))

            if hasattr(self.race, 'dodges'):
                self.dodges = self.race.dodges
            
            if hasattr(self.race, 'block'):
                self.block = self.race.block
                
            if hasattr(self.race, 'berserk'):
                self.berserk = self.race.berserk

            for skill_name, skill_function in self.race.skills.items():
                self.add_skill(skill_name, skill_function)

    def attack(self, target):
        # Check if the player's race has the berserk ability
        if hasattr(self.race, 'berserk') and self.race.berserk():
            print("**** Berserk activated! ****")
            # Add the bonus damage from Berserk to the total damage
            damage_dealt = self._damage + self.bonus_dmg
        else:
            damage_dealt = self._damage
        
        target.take_damage(damage_dealt)
        

    def equip_items(self, equipment):
            """
            Equip items from the equipment to the player.
            
            Args:
                equipment (Equipment): The equipment containing items to be equipped.
            """
            for slot_type, item in equipment.slots.items():
                if item:
                    self.apply_item_bonus(item)

    def apply_item_bonus(self, item):
        """
        Apply the bonus provided by the equipped item.
        
        Args:
            item (Item): The equipped item.
        """
        if isinstance(item, Weapon) and item.damage_bonus:
            self._damage += item.damage_bonus
        elif isinstance(item, Helmet) and item.hit_points_bonus:
            self._hit_points += item.hit_points_bonus

    def __str__(self):
        race_name = self.race.name if self.race else "No race"
        return "Name: Player, Lives: {0._lives},Damage: {0._damage} Level: {0._level}, Score {0._score}, Hit Points {0._hit_points}, Race: {1}".format(self,race_name)


class Equipment:
    """
    Represents the equipment slots for a player character.
    
    Attributes:
        helmet (Helmet): The equipped helmet.
        weapon (Weapon): The equipped weapon.
        shield (Shield): The equipped shield.
        armor (Armor): The equipped armor.
    """
    def __init__(self):
        self.slots = {
            'helmet': None,
            'weapon': None,
            'shield': None,
            'armor': None
        }

    def equip(self, item):
        """
        Equip the specified item to the corresponding equipment slot.
        
        Args:
            item (Item): The item to be equipped.
        """
        slot_type = item.slot_type
        if slot_type in self.slots:
            self.slots[slot_type] = item

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Weapon(Item):
    def __init__(self, name, description, damage_bonus):
        super().__init__(name, description)
        self.damage_bonus = damage_bonus
        self.slot_type = 'weapon'

class Helmet(Item):
    def __init__(self, name, description, hit_points_bonus):
        super().__init__(name, description)
        self.hit_points_bonus = hit_points_bonus
        self.slot_type = 'helmet'


