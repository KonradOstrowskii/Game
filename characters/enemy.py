"""
Module defining enemy class.
"""

import random


class Monster:
    """
    Base class for all monster characters in the game.
    """
    def __init__(
        self,
        name="Enemy",
        hit_points=10,
        damage=3,
        experience_reward=50,
        lives=1,
        alive=True,
    ):
        self.name = name
        self.hit_points = hit_points
        self.hit_points_max = hit_points
        self.lives = lives
        self.damage = damage
        self.experience_reward = experience_reward
        self.alive = alive

    def take_damage(self, damage):
        """Reduces the monster's hit points and checks for death."""
        self.hit_points -= damage

        if self.hit_points > 0:
            print(f"{self.name} took {damage} points of damage and has {self.hit_points}/{self.hit_points_max} HP left.")
        else:
            self.lives -= 1
            if self.lives > 0:
                self.hit_points = self.hit_points_max
                print(f"{self.name} lost a life, but is still standing with {self.hit_points} HP!")
            else:
                print(f"--- {self.name} is dead. ---")
                self.alive = False
                self.hit_points = 0

    def __str__(self) -> str:
        return f"Name: {self.name}, Lives: {self.lives}, HP: {self.hit_points}"

    def attack(self, target):
        """
        The monster attacks a target.
        """
        # --- ZMIANA: Usunęliśmy stąd losową transformację ---
        damage_dealt = self.damage
        print(f"{self.name} attacks {target.name}, dealing {damage_dealt} damage.")
        target.take_damage(damage_dealt)


    def gold_reward(self):
        """Returns a random amount of gold."""
        return random.randint(10, 50) * (self.experience_reward // 50)
    
    def exp_reward(self):
        """Returns the monster's experience reward."""
        return self.experience_reward


class Troll(Monster):
    def __init__(self, name="Troll", hit_points=25, damage=6, experience_reward=250):
        super().__init__(name, hit_points, damage, experience_reward)


class Vampire(Monster):
    def __init__(self, name="Vampire", hit_points=20, damage=7, experience_reward=220):
        super().__init__(name, hit_points, damage, experience_reward)

    def take_damage(self, damage):
        if random.randint(1, 4) == 4: # 25% szans
            print(f"**** {self.name} vanishes in the shadows and dodges the attack! ****")
            return
        super().take_damage(damage)


class Wolf(Monster):
    def __init__(self, name="Wolf", hit_points=22, damage=5, experience_reward=200):
        super().__init__(name, hit_points, damage, experience_reward)


class Zombie(Monster):
    def __init__(self, name="Zombie", hit_points=20, damage=5, experience_reward=200):
        super().__init__(name, hit_points, damage, experience_reward)


class Skeleton(Monster):
    def __init__(self, name="Skeleton", hit_points=15, damage=4, experience_reward=150):
        super().__init__(name, hit_points, damage, experience_reward)


class Werewolf(Monster):
    def __init__(self, name="Werewolf", hit_points=30, damage=8, experience_reward=300):
        super().__init__(name, hit_points, damage, experience_reward)
        self.transformed = False

    def transform(self):
        if not self.transformed:
            self.damage += 3
            self.hit_points_max += 10
            self.hit_points = self.hit_points_max
            self.transformed = True
            print(f"🌕 The {self.name} is enraged! It transforms into a hulking beast! 🌕")

    # --- NOWA, ULEPSZONA LOGIKA ---
    def take_damage(self, damage):
        # Najpierw potwór otrzymuje obrażenia, tak jak każdy inny
        super().take_damage(damage)
        
        # A teraz, po otrzymaniu obrażeń, sprawdzamy warunek transformacji
        # Sprawdzamy, czy potwór jeszcze żyje, żeby martwy się nie transformował
        if self.alive and not self.transformed and self.hit_points <= (self.hit_points_max / 2):
            self.transform()


class Ghost(Monster):
    def __init__(self, name="Ghost", hit_points=18, damage=3, experience_reward=180):
        super().__init__(name, hit_points, damage, experience_reward)

    def take_damage(self, damage):
        if random.randint(1, 3) == 3: # 33% szans
            print(f"**** The {self.name} becomes ethereal and the attack passes through it! ****")
            return
        super().take_damage(damage)