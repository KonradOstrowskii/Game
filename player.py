class Player(object):

    def __init__(self, name):
        """ Player class : creating new player.

        Args:
            name (str): Name of the player
            lives (int):  Lives of the player
            level (int): Level of the player
            damage (int): Damage of the player
            hit_points (int): Hit points of the player
            score (float): Score of the player
            race (Race, object): Player's chosen race instance.
        """
        self.player = name
        self._lives = 1
        self._level = 1
        self._damage = 5
        self._hit_points = self._level * 10
        self._score = 0
        self.race = None
        self.race_name = None

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
    
    def take_damage(self,damage):
        remaining_points = self._hit_points - damage
        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("I took {} points damage and have {} left.".format(damage, self._hit_points))
        else:
            self._lives -=1
            
            if self._lives > 0:
                print("{0._name} lost a life".format(self))
                self._hit_points == self._hit_points 
            else:
                print("{0._name} is dead".format(self))
                self.alive = False


    lives = property(_get_lives, _set_lives,_get_score)

    @property 
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
        
    def apply_race_bonuses(self):
        if self.race:
            self.race_name = self.race.name
            for attribute in dir(self.race):
                if not attribute.startswith('__') and not callable(getattr(self.race, attribute)):
                    setattr(self, attribute, getattr(self.race, attribute))
                    if attribute == 'extra_hit_points':
                        self._hit_points += getattr(self.race, attribute)  # Add extra hit points
                    if attribute == 'bonus_dmg':
                        self._damage += getattr(self.race, attribute)


    def __str__(self):
        race_name = self.race.name if self.race else "No race"
        return "Name: {0.player}, Lives: {0._lives},Damage: {0._damage} Level: {0._level}, Score {0._score},Hit Points {0._hit_points}, Race: {1}".format(self,race_name)

