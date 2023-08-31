from characters.player import Player 
# from characters.equipment import  Equipment, Weapon, Helmet
from characters.creating_player import create_player
from combat.fight import Fight
from characters.enemy import Vampire
from saving_data.save_player import save_player_to_json, load_player_from_json
import json






# Main code
# print("Welcome to the Player Creation Menu!")
# player=create_player()
# print(player)
# player_filename = player.name
# print(player.skills)
# vampire = Vampire(name="Vampire", hit_points=20, lives=3, damage=2,experience_reward = 500)

# # Start the fight
# print(vampire)
# fight = Fight(player, vampire)
# fight.start()




# Before starting the game
load_choice = input("Load player data? (y/n): ")
if load_choice.lower() == 'y':
    player_filename = input("Enter the filename of the player data: ")
    player = load_player_from_json(player_filename)
    print("Player data loaded successfully.")
    print(player)


vampire = Vampire(name="Vampire", hit_points=20, lives=3, damage=2,experience_reward = 500)

# Start the fight
print(vampire)
fight = Fight(player, vampire)
fight.start()