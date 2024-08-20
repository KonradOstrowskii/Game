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
                save_dir, f"{created_player.name.lower()}_player.json"
            )
            save_player_to_json(created_player)
            print_json_file(filename)
            break
        elif choice == "2":
            available_players = list_available_players()
            print(available_players)
            if not available_players:
                print("No players found.")
            else:
                print("Available Players:")
                for name in available_players:
                    print(name)

                player_name = input(
                    "Enter the name of the player you want to load: "
                ).capitalize()

                if player_name not in available_players:
                    print(f"Player '{player_name}' not found.")
                else:
                    filename = os.path.join(
                        save_dir, f"{player_name.lower()}_player.json"
                    )
                    loaded_player = load_player_from_json(player_name)
                    if loaded_player:
                        print("Player loaded successfully:")
                        print_json_file(filename)
                        break
                    else:
                        print(f"Failed to load player '{player_name}'.")
                        break
        elif choice == "3":
            available_players = list_available_players()
            
            if not available_players:
                print("No saved players available.")
            else:
                print("Available players:")
                for idx, player in enumerate(available_players, start=1):
                    display_name = player.replace('_player.json', '')
                    print(f"{idx}. {display_name}")
                player_choice = input("Enter the number of the player you want to view: ")
                
                try:
                    player_choice = int(player_choice)
                    if 1 <= player_choice <= len(available_players):
                        selected_player = available_players[player_choice - 1]
                        player_file_path = os.path.join(f"{selected_player.lower()}_player.json")
                        print_json_file(player_file_path)
                    else:
                        print("Invalid choice. Please select a valid player number.")
                except ValueError:
                    print("Invalid input. Please enter a number.")

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
