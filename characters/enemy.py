import random


class Monster:

    def __init__(self, name="Enemy", hit_points=0, lives=1, damage=0, experience_reward=0):
        """A class representing a monster in the game.

        Attributes:
            _name (str): The name of the monster.
            _hit_points (int): The hit points of the monster.
            _lives (int): The remaining lives of the monster.
            _damage (int): The damage dealt by the monster.
            _initial_hit_points (int): Initial hit points for fight.
            _experience_reward (int): IThe amount of experience points the player receives for defeating the enemy. 
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
        self._initial_hit_points = hit_points
        self.experience_reward = experience_reward
        self.alive = True

    def take_damage(self, damage):
        remaining_points = self._hit_points - damage

        if remaining_points >= 0:
            self._hit_points = remaining_points
            print("{} took {} points damage and have {} left.".format(self._name, damage, self._hit_points))
        else:
            self._lives -= 1

            if self._lives > 0:
                lost_hp = self._initial_hit_points - self._hit_points  # Calculate lost hit points
                self._hit_points = self._initial_hit_points  # Reset hit points to initial value
                print("{0._name} lost a life, took {1} points damage, and reset to {2} hit points.".format(self, damage,
                                                                                                           self._hit_points))
                print("{0._name} has {1} lives remaining.".format(self, self._lives))
            else:
                print("{0._name} lost a life, took {1} points damage".format(self, damage))
                print("{0._name} is dead.".format(self))
                self.alive = False
                self._hit_points = 0

    def __str__(self) -> str:
        return "Name : {0._name}, Lives: {0._lives}, Hit points: {0._hit_points}".format(self)

    def attack(self, target):
        damage_dealt = self._damage

        attack_result = target.take_damage(damage_dealt)
        print(attack_result)

    def defeat(self):
        print("You defeated the {}!".format(self._name))
        return self.experience_reward


class Troll(Monster):

    def __init__(self, name, hit_points, lives, damage, experience_reward):
        super().__init__(name, hit_points, lives, damage, experience_reward)


class Vampire(Monster):

    def __init__(self, name, hit_points, lives, damage, experience_reward):
        super().__init__(name, hit_points, lives, damage, experience_reward)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("****{0._name} dodges *****".format(self))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage)


class Wolf(Monster):
    def __init__(self, name="Wolf", hit_points=22, lives=1, damage=5, experience_reward=200):
        super().__init__(name, hit_points, lives, damage, experience_reward)
