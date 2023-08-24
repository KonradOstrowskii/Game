from player import Player 
from equipment import  Equipment, Weapon, Helmet
from creating_player import create_player
from fight import Fight
from enemy import Vampire



# Main code
player = Player("")
print(player)

equipment = Equipment()
sword = Weapon("Sword", "A sharp sword", 5)
helmet = Helmet("Helmet", "A sturdy helmet", 3)
equipment.equip(sword)
equipment.equip(helmet)
player.equip_items(equipment)
print("Welcome to the Player Creation Menu!")
create_player()

cave_troll = Vampire(name="Vampire", hit_points=20, lives=3, damage=8)

# Start the fight
fight = Fight(player, cave_troll)
fight.start()