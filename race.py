import random

class Elf(object):
    """
    
     Dwarf class that player can choose early in the game
     
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
        
    def __str__(self):
        description = "Elf : Graceful and intelligent beings, Elves are known for their agility and affinity for magic."
        return description
    
    def dodges(self):
        if random.randint(1,3) == 3:
            print("**** {0.name} dodges *****".format(self))
            return True
        else:
            return False
    
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage)
        
class Dwarf(object):
    """
    
     Dwarf class that player can choose early in the game
     
    """
    def __init__(self,name = "Dwarf", bonus_dmg = 3, extra_hit_points = 10):
        """

        Args:
            name (str): Dwarf
            bonus_dmg (int): Bonus damage . Defaults to 3.
            extra_hit_points (int): extra hit points . Defaults to 10.
        """
        self.name = name
        self.bonus_dmg = bonus_dmg
        self.extra_hit_points = extra_hit_points
        
    def __str__(self):   
        description = "Dwarf : Sturdy and resilient, Dwarves are skilled miners and craftsmen, with a natural resistance to damage."
        return description
