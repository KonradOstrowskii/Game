"""
Module defining race.
"""

import random


class Race:
    def __init__(self, name, bonus_dmg=0, extra_hit_points=0):
        self.name = name
        self.bonus_dmg = bonus_dmg
        self.extra_hit_points = extra_hit_points
        self.skills = {}

    def add_skill(self, skill_name, skill_function=None):
        if skill_function is not None:
            self.skills[skill_name] = skill_function

    def get_skills_dict(self):
        return {
            skill_name: skill_function.__name__ if skill_function else None
            for skill_name, skill_function in self.skills.items()
        }


class Elf(Race):
    """
    Elves are graceful and intelligent beings, known for their agility and affinity for magic.
    As an Elf, you possess the unique ability to dodge attacks with a 20% chance,
    showcasing your exceptional reflexes and evasive skills.
    Elves start with a Narrow Sword and a Basic Cap, providing additional damage and hit points.
    """

    def __init__(self, name="Elf", bonus_dmg=6, extra_hit_points=5):
        """

        Args:
            name (str): Elf
            bonus_dmg (int): Bonus damage . Defaults to 6.
            extra_hit_points (int): extra hit points . Defaults to 5.
        """
        self.name = name
        self.bonus_dmg = bonus_dmg
        self.extra_hit_points = extra_hit_points
        super().__init__(name, bonus_dmg, extra_hit_points)
        self.add_skill("dodge", self.dodges)

    def __str__(self):
        description = """
        Elves are graceful and intelligent beings, known for their agility and affinity for magic.
        As an Elf, you possess the unique ability to dodge attacks with a 20% chance, 
        showcasing your exceptional reflexes and evasive skills.
        Elves start with a Narrow Sword and an Basic Cap and Rusty ring providing additional damage and hit points.
        """
        return description

    @staticmethod
    def dodges():
        """
        Checks if the Elf successfully dodges an attack there is 20% chance.

        Returns:
            bool: True if the dodge is successful, False otherwise.
        """
        if random.randint(1, 5) == 5:
            return True
        else:
            return False


class Dwarf(Race):
    """
    Dwarf class that player can choose early in the game.
    Dwarves are sturdy and resilient beings, known for their mining skills and craftsmanship.
    As a Dwarf, your natural resistance to damage grants you the ability to block attacks with a 20% chance,
    allowing you to mitigate incoming damage and showcase your toughness.
    Dwarf start with a Weak Hammer and a Plain Helmet and Dirty shoes providing additional damage and hit points.
    """

    def __init__(self, name="Dwarf", bonus_dmg=4, extra_hit_points=7):
        """

        Args:
            name (str): Dwarf
            bonus_dmg (int): Bonus damage . Defaults to 3.
            extra_hit_points (int): extra hit points . Defaults to 10.
        """
        self.name = name
        self.bonus_dmg = bonus_dmg
        self.extra_hit_points = extra_hit_points
        super().__init__(name, bonus_dmg, extra_hit_points)
        self.add_skill("block", self.block)

    def __str__(self):
        description = """
        Dwarves are sturdy and resilient beings, known for their mining skills and craftsmanship.
        As a Dwarf, your natural resistance to damage grants you the ability to block attacks with a 20% chance,
        allowing you to mitigate incoming damage and showcase your toughness.
        Dwarf start with a Weak Hammer and an Plain Helmet and Shattered shield providing additional damage and hit points.
        """
        return description

    @staticmethod
    def block():
        """
        Checks if the Dwarf successfully blocks an attack there is 20 % chance.

        Returns:
            bool: True if the block is successful, False otherwise.
        """
        if random.randint(1, 5) == 5:
            return True
        else:
            return False


class Orc(Race):
    """
    Orc class that player can choose early in the game.
    Orcs are fierce and powerful creatures, known for their raw strength and aggression.
    As an Orc, you have a 20% chance to trigger your Berserk ability, allowing you to deal
    increased damage for a limited time. Unleash your inner fury and overwhelm your foes!
    Orcs start with a Blunt Axe and an Old Helmet, providing additional damage and hit points.
    """

    def __init__(self, name="Orc", bonus_dmg=7, extra_hit_points=4):
        """
        Args:
            name (str): Orc
            bonus_dmg (int): Bonus damage. Defaults to 4.
            extra_hit_points (int): Extra hit points. Defaults to 5.
        """
        self.name = name
        self.bonus_dmg = bonus_dmg
        self.extra_hit_points = extra_hit_points
        super().__init__(name, bonus_dmg, extra_hit_points)
        self.add_skill("berserk", self.berserk)

    def __str__(self) -> str:
        description = """
        Orcs are fierce and powerful creatures, known for their raw strength and aggression.
        As an Orc, you have a 20% chance to trigger your Berserk ability, allowing you to deal
        increased damage for a limited time. Unleash your inner fury and overwhelm your foes!
        Orcs start with a Blunt Axe and an Old Helmet, providing additional damage and hit points.
        """
        return description

    def berserk(self):
        """
        Check if the Orc's Berserk ability triggers.

        Returns:
            bool: True if the Berserk ability triggers, False otherwise.
        """
        if random.randint(1, 5) == 5:
            self.bonus_dmg += 5
            return True
        else:
            return False
