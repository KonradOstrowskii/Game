from characters.creating_player import create_player, print_race_descriptions
from combat.fight import Fight
from saving_data.save_load_player import save_player_to_json, load_player_from_json, list_available_players, print_json_file
from characters.enemy import *
import os

def print_menu():
    print("Menu:")
    print("1. Create a new player")
    print("2. Load an existing player")
    print("3. Exit")

# x = create_player()
# save_player_to_json(x)
# y = create_player()
# save_player_to_json(y)
# p = create_player()
# save_player_to_json(p)
if __name__ == "__main__":
    while True:
        print_menu()
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            create_player()
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
                    filename = os.path.join("saved_players", f"{player_name.lower()}_player.json")

                    # Load the player from the file
                    loaded_player = load_player_from_json(player_name)


                    # Print the loaded player information
                    if loaded_player:
                        print("Player loaded successfully:")
                        print_json_file(filename)
                    else:
                        print(f"Failed to load player '{player_name}'.")
        elif choice == "3":
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


