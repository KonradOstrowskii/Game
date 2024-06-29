"""
Module defining the combat system.
"""

class Fight:
    def __init__(self, player, monster):
        """
        Initialize a new fight.

        Args:
            player (Player): The player character.
            monster (Monster): The monster character.
        """
        self.player = player
        self.monster = monster

    def start(self):
        """
        Start the fight.
        """
        while self.player.alive and self.monster.alive:
            self.player.attack(self.monster)
            if self.monster.alive:
                self.monster.attack(self.player)
        if self.player.alive:
            print(f"{self.player.name} won the fight!")
        else:
            print(f"{self.monster.name} won the fight!")
