import random
class Monster:

    def __init__(self,name = "Enemy", hit_points = 0, lives= 1):
        """_summary_

        Args:
            name (str, optional): Name of the monster. Defaults to "Enemy".
            hit_points (int, optional): Hit points of the monster. Defaults to 0.
            lives (int, optional): Lives of the monster. Defaults to 1.
        """
        self._name = name
        self._hit_points = hit_points
        self._lives = lives
        self.alive = True
        
    def take_damage(self,damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left.".format(damage, self._hit_points))
        else:
            self._lives -=1
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
            else:
                print("{0._name} is dead".format(self))
                self.alive = False
            
    def __str__(self) -> str:
        return "Name : {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)
    
    
class Troll(Monster):
    
    def __init__(self, name):
        super().__init__(name=name, hit_points=1, lives=1)
        
class Vampire(Monster):
    
    def __init__(self, name="Enemy", hit_points=12, lives=3):
        super().__init__(name, hit_points, lives)
        
    def dodges(self):
        if random.randint(1,3) == 3:
            print("****{0._name} dodges *****".format(self))
            return True
        else:
            return False
    
    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage)