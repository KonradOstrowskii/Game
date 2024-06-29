import random

class Monster:
    def __init__(self, name="Enemy", hit_points=0, lives=1, damage=0, experience_reward=0, alive=True):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.damage = damage
        self.initial_hit_points = hit_points
        self.experience_reward = experience_reward
        self.alive = alive

    def take_damage(self, damage):
        remaining_points = self.hit_points - damage

        if remaining_points >= 0:
            self.hit_points = remaining_points
            print("{} took {} points damage and has {} left.".format(self.name, damage, self.hit_points))
        else:
            self.lives -= 1

            if self.lives > 0:
                lost_hp = self.initial_hit_points - self.hit_points
                self.hit_points = self.initial_hit_points
                print("{} lost a life, took {} points damage, and reset to {} hit points.".format(self.name, damage, self.hit_points))
                print("{} has {} lives remaining.".format(self.name, self.lives))
            else:
                print("{} lost a life, took {} points damage".format(self.name, damage))
                print("{} is dead.".format(self.name))
                self.alive = False
                self.hit_points = 0

    def __str__(self) -> str:
        return "Name : {}, Lives: {}, Hit points: {}".format(self.name, self.lives, self.hit_points)

    def attack(self, target):
        damage_dealt = self.damage
        attack_result = target.take_damage(damage_dealt)
        print(attack_result)

    def defeat(self):
        print("You defeated the {}!".format(self.name))
        return self.experience_reward

class Troll(Monster):
    def __init__(self, name="Troll", hit_points=25, lives=1, damage=6, experience_reward=250):
        super().__init__(name, hit_points, lives, damage, experience_reward)

class Vampire(Monster):
    def __init__(self, name, hit_points, lives, damage, experience_reward, alive=True):
        super().__init__(name, hit_points, lives, damage, experience_reward, alive)

    def dodges(self):
        if random.randint(1, 3) == 3:
            print("**** {} dodges *****".format(self.name))
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges():
            super().take_damage(damage)

class Wolf(Monster):
    def __init__(self, name="Wolf", hit_points=22, lives=1, damage=5, experience_reward=200):
        super().__init__(name, hit_points, lives, damage, experience_reward)

class Zombie(Monster):
    def __init__(self, name="Zombie", hit_points=20, lives=1, damage=5, experience_reward=200):
        super().__init__(name, hit_points, lives, damage, experience_reward)

class Skeleton(Monster):
    def __init__(self, name="Skeleton", hit_points=15, lives=1, damage=4, experience_reward=150):
        super().__init__(name, hit_points, lives, damage, experience_reward)

class Werewolf(Monster):
    def __init__(self, name="Werewolf", hit_points=30, lives=1, damage=8, experience_reward=300):
        super().__init__(name, hit_points, lives, damage, experience_reward)

    def transform(self):
        if random.randint(1, 5) == 5:
            self.damage += 3
            self.hit_points += 5
            print("{} transformed into a more powerful form!".format(self.name))

class Ghost(Monster):
    def __init__(self, name="Ghost", hit_points=18, lives=1, damage=3, experience_reward=180):
        super().__init__(name, hit_points, lives, damage, experience_reward)

    def phase_through_walls(self):
        if random.randint(1, 3) == 3:
            print("{} phases through the walls, avoiding damage!".format(self.name))
            return True
        else:
            return False
