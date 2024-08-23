"""
Main application module for the game.
"""

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from characters.creating_player import create_player, print_race_descriptions
from combat.fight import Fight
from saving_data.save_and_load_player import (
    save_player_to_json,
    load_player_from_json,
    list_available_players,
    print_json_file,
)
from characters.enemy import Skeleton
from characters.race import Elf, Dwarf, Orc


player_name = ""
created_player = None
loaded_player = None


def print_menu():
    """
    Print the main menu.
    """
    print("Menu:")
    print("1. Create a new player")
    print("2. Load an existing player")
    print("3. Show available players")
    print("4. Exit")


if __name__ == "__main__":
    save_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saved_players")
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            created_player = create_player()
            filename = os.path.join(
                save_dir, f"{created_player.name.lower()}.json"
            )
            save_player_to_json(created_player)
            print_json_file(filename)
            break
        elif choice == "2" or choice == "3":
            available_players = list_available_players()
            if not available_players:
                print("No players found.")
            else:
                print("Available Players:")
                for index, name in enumerate(available_players, start=1):
                    print(f"{index}. {name}")

                player_index = input(
                    "Enter the number of the player you want to load: "
                )

                if not player_index.isdigit() or int(player_index) < 1 or int(player_index) > len(available_players):
                    print(f"Invalid selection.")
                else:
                    player_name = available_players[int(player_index) - 1]
                    filename = os.path.join(
                        save_dir, f"{player_name.lower()}.json"
                    )
                    loaded_player = load_player_from_json(player_name)
                    if loaded_player:
                        print("Player loaded successfully:")
                        print_json_file(filename)
                        break
                    else:
                        print(f"Failed to load player '{player_name}'.")
                        break
        elif choice == "4":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


    
    monster_instance = Skeleton() 
    fight = None
    if created_player is None:
        fight = Fight(loaded_player, monster_instance)
    else:
        fight = Fight(created_player, monster_instance)
    if fight:
        fight.start()
