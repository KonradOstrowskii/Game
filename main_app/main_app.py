import os
import sys

# Add the project root directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from characters.creating_player import create_player, print_race_descriptions
from combat.fight import Fight
from saving_data.save_and_load_player import save_player_to_json, load_player_from_json, list_available_players, print_json_file
from characters.enemy import Skeleton
from characters.race import Elf, Dwarf, Orc

player_name = ""
created_player = None
loaded_player = None

def print_menu():
    print("Menu:")
    print("1. Create a new player")
    print("2. Load an existing player")
    print("3. Exit")

if __name__ == "__main__":
    save_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'saved_players')
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            created_player = create_player()
            filename = os.path.join(save_dir, f"{created_player.name.lower()}_player.json")
            save_player_to_json(created_player)
            print_json_file(filename)
            break
        elif choice == "2":
            # List available players
            available_players = list_available_players()
            print(available_players)
            if not available_players:
                print("No players found.")
            else:
                print("Available Players:")
                for name in available_players:
                    print(name)

                # Enter the name of the player you want to load
                player_name = input("Enter the name of the player you want to load: ").capitalize()

                # Check if the entered player name is in the available players list
                if player_name not in available_players:
                    print(f"Player '{player_name}' not found.")
                else:
                    # Construct the filename based on the entered player name
                    filename = os.path.join(save_dir, f"{player_name.lower()}_player.json")

                    # Load the player from the file
                    loaded_player = load_player_from_json(player_name)
                    # Print the loaded player information
                    if loaded_player:
                        print("Player loaded successfully:")
                        print_json_file(filename)
                        break
                    else:
                        print(f"Failed to load player '{player_name}'.")
                        break
        elif choice == "3":
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
