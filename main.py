from characters.player import Player 
from characters.equipment import  Equipment, Weapon, Helmet
from characters.creating_player import create_player
from combat.fight import Fight
from characters.enemy import Vampire



# Main code
print("Welcome to the Player Creation Menu!")
player=create_player()

vampire = Vampire(name="Vampire", hit_points=20, lives=3, damage=2,experience_reward = 500)

# Start the fight
print(vampire)
fight = Fight(player, vampire)
fight.start()
