from player import Player 
from equipment import  Equipment, Weapon, Helmet
from creating_player import create_player
from fight import Fight
from enemy import Vampire



# Main code
print("Welcome to the Player Creation Menu!")
player=create_player()

vampire = Vampire(name="Vampire", hit_points=20, lives=3, damage=2)

# Start the fight
print(vampire)
fight = Fight(player, vampire)
fight.start()