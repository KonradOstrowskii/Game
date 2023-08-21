class Elf(object):
    """
    
     Dwarf class that player can choose early in the game
     
    """
    def __init__(self, bonus_dmg = 6, extra_hit_points = 5):
        """

        Args:
            bonus_dmg (int): Bonus damage . Defaults to 6.
            extra_hit_points (int): extra hit points . Defaults to 5.
        """
        self.bonus_dmg = bonus_dmg
        self.extra_hit_points = extra_hit_points
        
class Dwarf(object):
    """
    
     Dwarf class that player can choose early in the game
     
    """
    def __init__(self, bonus_dmg = 3, extra_hit_points = 10):
        """

        Args:
            bonus_dmg (int): Bonus damage . Defaults to 3.
            extra_hit_points (int): extra hit points . Defaults to 10.
        """
        self.bonus_dmg = bonus_dmg
        self.extra_hit_points = extra_hit_points
