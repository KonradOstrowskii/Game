"""
Module defining the Player class.
"""

from .equipment import Equipment


class Player(object):
    """
    Player class: Represents a player character in the game.

    Args:
        name (str): The name of the player character.

    Attributes:
        name (str): The name of the player character.
        _lives (int): The number of lives the player has.
        _level (int): The level of the player character.
        _experience (int): The experience points earned by the player.
        _damage (int): The base damage inflicted by the player character.
        _hit_points (int): The current hit points of the player character.
        _hit_points_max (int): The maximum hit points of the player.
        race (Race): The chosen race instance for the player character.
        skills (dict): A dictionary of player skills, mainly for saving/loading.
        alive (bool): Indicates if the player character is alive.
        equipment (Equipment): The player's equipped items.
        inventory (list): The player's backpack for storing items.
        gold (int): The amount of gold the player has.
        _score (int): The player's score.
    """

    def __init__(self, name):
        self.name = name
        self._lives = 1
        self._level = 1
        self._experience = 0
        self._damage = 5
        self._hit_points_max = 10
        self._hit_points = self._hit_points_max
        self.race = None
        self.skills = {}
        self.alive = True
        self.equipment = Equipment()
        self.inventory = []
        self.gold = 200
        self._score = 0

    def __str__(self):
        race_name = self.race.name if self.race else "No race"
        return "Name: {}, Level: {}, HP: {}/{}, Damage: {}, Exp: {}, Gold: {}, Race: {}".format(
            self.name,
            self._level,
            self._hit_points,
            self._hit_points_max,
            self._damage,
            self._experience,
            self.gold,
            race_name,
        )

    # --- Properties Section ---
    def _get_lives(self):
        return self._lives

    def _set_lives(self, lives):
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    lives = property(_get_lives, _set_lives)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if value >= 0:
            self._score = value
        else:
            print("Score cannot be negative.")
            self._score = 0
    
    # --- Combat and Stats Methods ---
    def take_damage(self, damage):
        if hasattr(self, "dodges") and self.dodges():
            print(f"**** {self.name} dodged the attack! ****")
            return
        elif hasattr(self, "block") and self.block():
            print(f"**** {self.name} blocked the attack! ****")
            return
        
        remaining_points = self._hit_points - damage

        if remaining_points > 0:
            self._hit_points = remaining_points
            print(f"{self.name} took {damage} points of damage and has {self._hit_points}/{self._hit_points_max} HP left.")
        else:
            self._lives -= 1
            if self._lives > 0:
                self._hit_points = self._hit_points_max
                print(f"{self.name} lost a life and was restored to full health.")
            else:
                self.alive = False
                self._hit_points = 0
                print(f"--- {self.name} is dead. ---")

    def attack(self, target):
        damage_dealt = self._damage
        if hasattr(self, "berserk") and self.berserk():
            print("**** Berserk activated! Damage increased! ****")
            damage_dealt = int(damage_dealt * 1.5)
        
        print(f"{self.name} attacks {target.name}, dealing {damage_dealt} damage.")
        target.take_damage(damage_dealt)

    # --- Character Progression and Management ---
    def apply_race_bonuses(self):
        """
        Applies bonuses from the player's race. This includes base stats
        and copying specific, known skills from the race to the player instance.
        """
        if self.race:
            self._damage += self.race.bonus_dmg
            self._hit_points_max += self.race.extra_hit_points
            self._hit_points = self._hit_points_max
            
            # --- POPRAWIONA WERSJA ---
            # Jawne i proste kopiowanie umiejętności. Bez pętli.
            # To jest czysty, bezpieczny i czytelny kod.
            if hasattr(self.race, "dodges"):
                self.skills['dodge'] = self.race.dodges
                self.dodges = self.race.dodges
            if hasattr(self.race, "block"):
                self.skills['block'] = self.race.block
                self.block = self.race.block
            if hasattr(self.race, "berserk"):
                self.skills['berserk'] = self.race.berserk
                self.berserk = self.race.berserk

    def apply_item_bonus(self, item):
        """
        Applies bonuses from an equipped item.
        We decided to go with Option B: items only increase the maximum stats,
        they do not provide healing on equip.
        """
        if hasattr(item, "damage_bonus") and item.damage_bonus:
            self._damage += item.damage_bonus
        if hasattr(item, "hit_points_bonus") and item.hit_points_bonus:
            self._hit_points_max += item.hit_points_bonus
            # Nie dodajemy już bonusu do aktualnego HP, tylko do max.

    def gain_experience(self, amount):
        self._experience += amount
        print(f"{self.name} gained {amount} experience points.")
        self.level_up()

    def level_up(self):
        base_experience = 200
        experience_multiplier = 2.3
        leveled_up = False
        
        required_experience = int(base_experience * (experience_multiplier ** (self._level - 1)))
        while self._experience >= required_experience:
            self._level += 1
            self._experience -= required_experience
            print(f"🎉 {self.name} has leveled up to level {self._level}! 🎉")
            self._level_up_attributes()
            leveled_up = True
            required_experience = int(base_experience * (experience_multiplier ** (self._level - 1)))
        
        if not leveled_up:
            print(f"Experience to next level: {self._experience}/{required_experience}")

    def _level_up_attributes(self):
        self._damage += 2
        self._hit_points_max += 10
        self._hit_points = self._hit_points_max # Awans na poziom przywraca pełne zdrowie
        print(f"Damage increased to {self._damage}, Max Hit Points increased to {self._hit_points_max}.")