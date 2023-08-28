from characters.player import Player 
from characters.equipment import  Equipment, Weapon, Helmet
from characters.race import Elf, Dwarf, Orc
from combat.fight import Fight
from characters.enemy import Vampire
import random


def print_race_descriptions():
    print("Available Races:")
    print("1. Elf")
    print(Elf.__str__(Elf()))
    print("2. Dwarf")
    print(Dwarf.__str__(Dwarf()))
    print("3. Orc")
    print(Orc.__str__(Orc()))

def create_player():
    player_name = input("Please choose your player name: ")

    print_race_descriptions()

    while True:
        player = Player(player_name)
        print(player)
        race_choice = input("Choose a race (1 for Elf, 2 for Dwarf, 3 for Orc): ")
        if race_choice == "1":
            player.race = Elf()
            player.apply_race_bonuses()
            weak_sword = Weapon("Narrow Sword", "A dull sword",damage_bonus= 2)
            weak_helmet = Helmet("Basic Cap", "A simple cap", hit_points_bonus=1)
            equipment = Equipment()
            equipment.equip(weak_sword)
            equipment.equip(weak_helmet)
            player.equip_items(equipment)
            break
        elif race_choice == "2":
            player.race = Dwarf()
            player.apply_race_bonuses()
            weak_hammer = Weapon("Weak Hammer", "A lightweight hammer", damage_bonus=2)
            weak_helmet = Helmet("Plain Helmet", "A simple helmet", hit_points_bonus=1) 
            equipment = Equipment()
            equipment.equip(weak_hammer)
            equipment.equip(weak_helmet)
            player.equip_items(equipment)
            break
        elif race_choice == "3":
            player.race = Orc()
            player.apply_race_bonuses()
            weak_axe = Weapon("Blunt Axe", "A dull axe", damage_bonus=2)
            weak_helmet = Helmet("Old Helmet", "A worn helmet", hit_points_bonus=1)
            equipment = Equipment()
            equipment.equip(weak_axe)
            equipment.equip(weak_helmet)
            player.equip_items(equipment)
            break
        else:
            print("Invalid choice. Please choose 1 for Elf, 2 for Dwarf, or 3 for Orc")

    print("Player created:")
    print(player)
    return player  # Return the created player object
