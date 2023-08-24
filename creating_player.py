from player import Player 
from equipment import  Equipment, Weapon, Helmet
from race import Elf, Dwarf, Orc
from fight import Fight
from enemy import Vampire
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
            Player.race = Elf()
            Player.apply_race_bonuses(Elf)
            break
        elif race_choice == "2":
            Player.race = Dwarf()
            Player.apply_race_bonuses(Dwarf)
            break
        elif race_choice == "3":
            Player.race = Orc()
            Player.apply_race_bonuses(Orc)
            break
        else:
            print("Invalid choice. Please choose 1 for Elf, 2 for Dwarf or 3 for Orc")

    print("Player created:")
    print(Player)
