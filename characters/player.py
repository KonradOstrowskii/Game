"""
Module defining the Player class.
"""

from .equipment import Equipment, Weapon, Helmet


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
        race (Race): The chosen race instance for the player character.
        skills (dict): A dictionary of player skills.
        alive (bool): Indicates if the player character is alive.

    Note:
        The player's damage and hit points are initialized based on the initial level.
    """

    def __init__(self, name):
        self.name = name
        self._lives = 1
        self._level = 1
        self._experience = 0
        self._damage = 5
        self._hit_points = self._level * 10
        self.race = None
        self.skills = {}
        self.alive = True
        self.equipment = Equipment()

    def __str__(self):
        race_name = self.race.name if self.race else "No race"
        return "Name: {}, Level: {}, Damage: {}, Experience: {}, Hit Points: {}, Race: {}".format(
            self.name,
            self._level,
            self._damage,
            self._experience,
            self._hit_points,
            race_name,
        )

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

    lives = property(_get_lives, _set_lives, _get_score)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        self._score = score

    def take_damage(self, damage):
        if self.race and hasattr(self.race, "dodges") and self.race.dodges():
            return "**** Player dodge *****"
        elif self.race and hasattr(self.race, "block") and self.race.block():
            return "**** Player block *****"
        else:
            total_hit_points = self._hit_points
            remaining_points = total_hit_points - damage

            if remaining_points >= 0:
                self._hit_points = remaining_points  # Update hit points
                return (
                    "Player took {1} points damage and has {2} hit points left.".format(
                        self, damage, self._hit_points
                    )
                )
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
            self._damage += self.race.bonus_dmg
            self._hit_points += self.race.extra_hit_points

            # Copy skills from the race to the player's skills
            for skill_name, skill_function in self.race.skills.items():
                self.add_skill(skill_name, skill_function)

            for attribute in dir(self.race):
                if not attribute.startswith("__") and not callable(
                    getattr(self.race, attribute)
                ):
                    if not hasattr(self, attribute):
                        setattr(self, attribute, getattr(self.race, attribute))

                    if hasattr(self.race, "dodges"):
                        self.dodges = self.race.dodges

                    if hasattr(self.race, "block"):
                        self.block = self.race.block

                    if hasattr(self.race, "berserk"):
                        self.berserk = self.race.berserk

    def attack(self, target):
        # Check if the player's race has the berserk ability
        if hasattr(self.race, "berserk") and self.race.berserk():
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
                return equipment.slots.items()

    def apply_item_bonus(self, item):
        """
        Apply the bonus provided by the equipped item.

        Args:
            item (Item): The equipped item.
        """
        if hasattr(item, "bonus") and item.bonus:
            if isinstance(item, Weapon):
                self._damage += item.bonus
            if isinstance(item, Helmet):
                self._hit_points += item.bonus

    def level_up(self):
        base_experience = 200  # Initial required experience for level 1
        experience_multiplier = (
            2.3  # Multiplier for calculating required experience for each level
        )

        for level in range(self._level + 1, self._level + 2):
            required_experience = int(
                base_experience * (experience_multiplier ** (level - 1))
            )
            if self._experience >= required_experience:
                self._level = level
                self._experience -= required_experience
                print("{0.name} has leveled up to level {0._level}!".format(self))
                self._level_up_attributes()
            else:
                print(
                    "{0.name} does not have enough experience to level up.".format(self)
                )

    def gain_experience(self, amount):
        self._experience += amount
        self.level_up()

    def _level_up_attributes(self):
        """
        Increase player attributes upon leveling up.
        """
        self._damage += 2  # Increase damage
        self._hit_points += 10  # Increase hit points
