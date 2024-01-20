import json
import os
import random
from characters.race import *
from characters.player import Player
from characters.equipment import *


def save_player_to_json(player):
    save_folder = "saved_players"
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    filename = os.path.join(save_folder, f"{player.name.lower()}_player.json")

    # Collect information about equipped items
    equipped_items = []
    for slot_type, item in player.equipment.slots.items():
        if item:
            item_data = {
                "name": item.name,
                "description": item.description,
                "slot_type": item.slot_type,
                # Add more item-specific attributes as needed
            }
            equipped_items.append(item_data)

    player_data = {
        "name": player.name,
        "level": player._level,
        "lives": player._lives,
        "experience": player._experience,
        "damage": player._damage + player.race.bonus_dmg,
        "hit_points": player._hit_points + player.race.extra_hit_points,
        "race_attributes": {
            "name": player.race.name,
            "bonus_dmg": player.race.bonus_dmg,
            "extra_hit_points": player.race.extra_hit_points,
            "skills": player.race.get_skills_dict()
        },
        "equipment": equipped_items  # Include the equipped items list
    }

    with open(filename, "w") as json_file:
        json.dump(player_data, json_file, indent=4)


def print_json_file(filename):
    try:
        with open(filename, 'r') as json_file:
            data = json.load(json_file)
            print(json.dumps(data, indent=4))
    except FileNotFoundError:
        print(f"File not found: {filename}")
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON from file {filename}: {e}")


def list_available_players():
    folder_path = 'saved_players'
    player_files = [file for file in os.listdir(folder_path) if file.endswith("_player.json")]
    player_names = [file.replace("_player.json", "").capitalize() for file in player_files]
    return player_names


def load_player_from_json(player_name):
    folder_path = 'saved_players'
    available_players = list_available_players()

    if not available_players:
        print("No players found in the specified folder.")
        return None

    filename = os.path.join(folder_path, f"{player_name.lower()}_player.json")

    if os.path.exists(filename):
        with open(filename, 'r') as json_file:
            player_data = json.load(json_file)

        # Load race attributes dynamically
        race_name = player_data["race_attributes"]["name"]
        race_bonus_dmg = player_data["race_attributes"]["bonus_dmg"]
        race_extra_hit_points = player_data["race_attributes"]["extra_hit_points"]
        race_skills_data = player_data["race_attributes"]["skills"]

        # Find the race class dynamically based on the race name
        race_class = None
        if race_name == "Dwarf":
            from characters.race import Dwarf
            race_class = Dwarf
        elif race_name == "Elf":
            from characters.race import Elf
            race_class = Elf

        if race_class is not None:
            # Create a Player instance with dynamic attributes
            player = Player(player_name)

            # Set attributes dynamically
            for attr_name, attr_value in player_data.items():
                if hasattr(player, attr_name):
                    setattr(player, attr_name, attr_value)

            # Set the race separately
            player.race = race_class(name=race_name, bonus_dmg=race_bonus_dmg, extra_hit_points=race_extra_hit_points)

            # Add skills to the player based on the loaded race skills
            for skill_name, skill_function_name in race_skills_data.items():
                # Assuming skill_function_name is the actual function name
                skill_function = getattr(player.race, skill_function_name, None)

                if skill_function:
                    player.race.add_skill(skill_name, skill_function)

            # Apply race bonuses and methods
            player.apply_race_bonuses()

            # Load player's equipment
            equipment_data = player_data.get("equipment", [])
            for item_data in equipment_data:
                slot_type = item_data["slot_type"]
                item = None

                if slot_type == "weapon":
                    item = Weapon(
                        name=item_data["name"],
                        description=item_data["description"],
                        damage_bonus=item_data["damage_bonus"]
                    )
                elif slot_type == "helmet":
                    item = Helmet(
                        name=item_data["name"],
                        description=item_data["description"],
                        hit_points_bonus=item_data["hit_points_bonus"]
                    )

                if item:
                    player.equipment.slots[slot_type] = item

            return player
        else:
            print(f"Race class not found for race: {race_name}")
            return None
    else:
        print(f"Player file not found: {filename}")
        return None
