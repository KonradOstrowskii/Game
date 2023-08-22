import random
class Monster:

    def __init__(self,name = "Enemy", hit_points = 0, lives= 1, damage = 0):
        """A class representing a monster in the game.

        Attributes:
            _name (str): The name of the monster.
            _hit_points (int): The hit points of the monster.
            _lives (int): The remaining lives of the monster.
            damage (int): The damage dealt by the monster.
            alive (bool): True if the monster is still alive, False otherwise.

        Args:
            name (str): The name of the monster. Defaults to "Enemy".
            hit_points (int): The initial hit points of the monster. Defaults to 0.
            lives (int): The initial lives of the monster. Defaults to 1.
            damage (int): The damage dealt by the monster. Defaults to 0.
        """
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self._damage = damage
        self.alive = True
        
    def take_damage(self,damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("{} took {} points damage and have {} left.".format(self._name,damage, self._hit_points))
        else:
            self._lives -=1
            
            if self._lives > 0:
                print("{} took {} points damage and have {} left.".format(self._name,damage, self._hit_points))
                print("{0._name} lost a life".format(self))
                self._hit_points == self._hit_points 
            else:
                print("{0._name} is dead".format(self))
                self.alive = False
            
    def __str__(self) -> str:
        return "Name : {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)
    
    def attack(self, target):
        damage_dealt = self._damage

        attack_result = target.take_damage(damage_dealt)
        print(attack_result)
    
    
class Troll(Monster):
    
    def __init__(self, name,hit_points,lives,damage):
        super().__init__(name,hit_points, lives,damage)
        
class Vampire(Monster):
    
    def __init__(self, name, hit_points, lives, damage):
        super().__init__(name, hit_points, lives, damage)
        
    def dodges(self):
        if random.randint(1,3) == 3:
            print("****{0._name} dodges *****".format(self))
            return True
        else:
            return False
    
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage)