from player import Player
from race import Elf, Dwarf, Orc
from fight import Fight
from enemy import Troll, Vampire
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
        race_choice = input("Choose a race (1 for Elf, 2 for Dwarf, 3 for Orc): ")
        if race_choice == "1":
            player.race = Elf()
            player.apply_race_bonuses()
            break
        elif race_choice == "2":
            player.race = Dwarf()
            player.apply_race_bonuses()
            break
        elif race_choice == "3":
            player.race = Orc()
            player.apply_race_bonuses()
            break
        else:
            print("Invalid choice. Please choose 1 for Elf, 2 for Dwarf or 3 for Orc")

    print("Player created:")
    print(player)

# Main code
player = Player("")

print("Welcome to the Player Creation Menu!")
create_player()

cave_troll = Vampire(name="Vampire", hit_points=20, lives=3, damage=8)

# Start the fight
fight = Fight(player, cave_troll)
fight.start()