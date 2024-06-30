"""
Module for creating players.
"""

from .equipment import Equipment, Weapon, Helmet
from .player import Player
from .race import Elf, Dwarf, Orc

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def print_race_descriptions():
    """
    Print descriptions of the available races for the player to choose from.

    This function displays the names and descriptions of the three available races:
    Elf, Dwarf, and Orc. It uses the __str__ method of each race class to provide
    detailed descriptions.
    """
    print("Available Races:")
    print("1. Elf")
    print(Elf.__str__(Elf()))
    print("2. Dwarf")
    print(Dwarf.__str__(Dwarf()))
    print("3. Orc")
    print(Orc.__str__(Orc()))


def create_player():
    """
    Create a new player character with a chosen race and initial equipment.

    This function prompts the user to input a name for the player character and
    select a race from the available options (Elf, Dwarf, Orc). Based on the chosen
    race, it initializes the player's attributes and equips them with initial items.

    The function does the following:
    1. Prompts the user for the player's name.
    2. Displays the available races and their descriptions.
    3. Prompts the user to select a race.
    4. Creates a Player object with the chosen name.
    5. Sets the player's race and applies race-specific bonuses.
    6. Equips the player with initial items based on the chosen race.

    The loop ensures that a valid race choice is made before proceeding with player
    creation.

    Raises:
        ValueError: If the race choice is invalid.

    Returns:
        Player: The created player object with the chosen race and initial equipment.
    """

    player_name = input("Please choose your player name: ")

    print_race_descriptions()

    while True:
        player = Player(player_name)

        race_choice = input("Choose a race (1 for Elf, 2 for Dwarf, 3 for Orc): ")
        if race_choice == "1":
            player.race = Elf()
            player.apply_race_bonuses()
            weak_sword = Weapon("Narrow Sword", "A dull sword", damage_bonus=2)
            weak_helmet = Helmet("Basic Cap", "A simple cap", hit_points_bonus=1)
            equipment = Equipment()
            equipment.equip(weak_sword, player)
            equipment.equip(weak_helmet, player)
            player.equip_items(equipment)
            break
        if race_choice == "2":
            player.race = Dwarf()
            player.apply_race_bonuses()
            weak_hammer = Weapon("Weak Hammer", "A lightweight hammer", damage_bonus=2)
            weak_helmet = Helmet("Plain Helmet", "A simple helmet", hit_points_bonus=1)
            equipment = Equipment()
            equipment.equip(weak_hammer, player)
            equipment.equip(weak_helmet, player)
            player.equip_items(equipment)
            break
        if race_choice == "3":
            player.race = Orc()
            player.apply_race_bonuses()
            weak_axe = Weapon("Blunt Axe", "A dull axe", damage_bonus=2)
            weak_helmet = Helmet("Old Helmet", "A worn helmet", hit_points_bonus=1)
            equipment = Equipment()
            equipment.equip(weak_axe, player)
            equipment.equip(weak_helmet, player)
            player.equip_items(equipment)
            break
        else:
            print("Invalid choice. Please choose 1 for Elf, 2 for Dwarf, or 3 for Orc")

    print("Player created:")
    return player
