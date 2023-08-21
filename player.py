class Player(object):

    def __init__(self, name):
        """ Player class : creating new player.

        Args:
            name (str): Name of the player
            lives (int):  Lives of the player
            level (int): Level of the player
            score (float): Score of the player
        """
        self.name = name
        self._lives = 1
        self._level = 1
        self._hit_points = self._level * 10
        self._score = 0

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

    def __str__(self):
        return "Name: {0.name}, Lives: {0.lives}, Level: {0.level}, Score {0.score}".format(self)

