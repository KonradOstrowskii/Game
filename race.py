import random

class Race:
    def __init__(self, name, bonus_dmg=0, extra_hit_points=0):
        self.name = name
        self.bonus_dmg = bonus_dmg
        self.extra_hit_points = extra_hit_points
        self.skills = {}
        

class Elf(Race):
    """
    Elves are graceful and intelligent beings, known for their agility and affinity for magic.
    As an Elf, you possess the unique ability to dodge attacks with a 20% chance, 
    showcasing your exceptional reflexes and evasive skills.
    """
    def __init__(self,name ="Elf", bonus_dmg = 6, extra_hit_points = 5):
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
        self.skills["dodges"] = self.dodges
        
    def __str__(self):
            description = """
            Elves are graceful and intelligent beings, known for their agility and affinity for magic.
            As an Elf, you possess the unique ability to dodge attacks with a 20% chance, 
            showcasing your exceptional reflexes and evasive skills.
            """
            return description
    
    def dodges(self):
        """
        Checks if the Elf successfully dodges an attack there is 20% chance.

        Returns:
            bool: True if the dodge is successful, False otherwise.
        """
        if random.randint(1,5) == 5:
            return True
        else:
            return False
    
        
class Dwarf(Race):
    """
    Dwarf class that player can choose early in the game.
    Dwarves are sturdy and resilient beings, known for their mining skills and craftsmanship.
    As a Dwarf, your natural resistance to damage grants you the ability to block attacks with a 20% chance,
    allowing you to mitigate incoming damage and showcase your toughness.
    """
    def __init__(self,name = "Dwarf", bonus_dmg =3, extra_hit_points = 10):
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
    
    def __str__(self):
        description = """
        Dwarves are sturdy and resilient beings, known for their mining skills and craftsmanship.
        As a Dwarf, your natural resistance to damage grants you the ability to block attacks with a 20% chance,
        allowing you to mitigate incoming damage and showcase your toughness.
        """
        return description
    
    def block(self):
        """
        Checks if the Dwarf successfully blocks an attack there is 20 % chance.

        Returns:
            bool: True if the block is successful, False otherwise.
        """
        if random.randint(1,5) == 5:
            return True
        else:
            return False
