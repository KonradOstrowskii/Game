from race import Elf, Dwarf, Race
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
            return("**** dodge *****")
        elif self.race and hasattr(self.race, 'block') and self.race.block():
            return("**** block *****")
        else:
            total_hit_points = self._hit_points
            remaining_points = total_hit_points - damage

            if remaining_points >= 0:
                self._hit_points = remaining_points  # Update hit points
                return "{0.name} took {1} points damage and has {2} hit points left.".format(self, damage, self._hit_points)
            else:
                self._lives -= 1
                
                if self._lives > 0:
                    self._hit_points = self._level * 10 + self.race.extra_hit_points
                    return "{0.name} lost a life".format(self)
                else:
                    self.alive = False
                    return "{0.name} is dead".format(self)

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

            for skill_name, skill_function in self.race.skills.items():
                self.add_skill(skill_name, skill_function)





    def __str__(self):
        race_name = self.race.name if self.race else "No race"
        return "Name: {0.player}, Lives: {0._lives},Damage: {0._damage} Level: {0._level}, Score {0._score},Hit Points {0._hit_points}, Race: {1}".format(self,race_name)

