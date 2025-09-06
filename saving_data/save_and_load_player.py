"""
Module for saving and loading player data.
"""
import json
import os

from characters.player import Player
from characters.race import Elf, Dwarf, Orc
from characters.equipment import (
    Equipment, Weapon, Helmet, Armor, Shield, Shoes, Ring, Necklace
)

RACE_CLASSES = {"Elf": Elf, "Dwarf": Dwarf, "Orc": Orc}
ITEM_CLASSES = {
    "weapon": Weapon,
    "helmet": Helmet,
    "armor": Armor,
    "shield": Shield,
    "shoes": Shoes,
    "ring": Ring,
    "necklace": Necklace,
}
SAVE_FOLDER_PATH = os.path.join(os.path.dirname(__file__), "..", "main_app", "saved_players")


def save_player_to_json(player):
    """Saves a player object to a JSON file."""
    if not os.path.exists(SAVE_FOLDER_PATH):
        os.makedirs(SAVE_FOLDER_PATH)

    filename = os.path.join(SAVE_FOLDER_PATH, f"{player.name.lower()}.json")

    equipped_items = {slot: item.to_dict() for slot, item in player.equipment.slots.items() if item}
    inventory_items = [item.to_dict() for item in player.inventory]

    player_data = {
        "name": player.name,
        "level": player._level,
        "lives": player._lives,
        "experience": player._experience,
        "base_damage": player._damage, # Zapisujemy bazowe statystyki
        "base_hp_max": player._hit_points_max,
        "current_hp": player._hit_points,
        "gold": player.gold,
        "score": player._score,
        "race": player.race.name if player.race else None,
        "equipment": equipped_items,
        "inventory": inventory_items,
    }

    try:
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(player_data, json_file, indent=4)
        print(f"Player '{player.name}' saved successfully.")
    except IOError as e:
        print(f"Error: Could not save player data. Reason: {e}")

def _recreate_item_from_data(item_data):
    """Helper function to recreate an item object from its dictionary representation."""
    item_type = item_data.get("slot_type")
    if item_type in ITEM_CLASSES:
        item_class = ITEM_CLASSES[item_type]
        params = item_data.copy()
        params.pop("slot_type", None)
        params.pop("attributes", None) # Usuwamy, jeśli __init__ go nie przyjmuje
        return item_class(**params)
    return None

def load_player_from_json(player_name):
    """Loads a player object from a JSON file."""
    filename = os.path.join(SAVE_FOLDER_PATH, f"{player_name.lower()}.json")

    if not os.path.exists(filename):
        print(f"Error: Save file for '{player_name}' not found.")
        return None

    try:
        with open(filename, "r", encoding="utf-8") as json_file:
            player_data = json.load(json_file)
    except (IOError, json.JSONDecodeError) as e:
        print(f"Error: Could not load player data. Reason: {e}")
        return None

    player = Player(player_data["name"])

    # Krok 1: Ustaw rasę i bazowe bonusy
    race_name = player_data.get("race")
    if race_name in RACE_CLASSES:
        player.race = RACE_CLASSES[race_name]()
        player.apply_race_bonuses()

    # Krok 2: Wczytaj statystyki (bez bonusów)
    player._level = player_data.get("level", 1)
    player._lives = player_data.get("lives", 1)
    player._experience = player_data.get("experience", 0)
    player.gold = player_data.get("gold", 0)
    player._score = player_data.get("score", 0)
    
    # Krok 3: Wczytaj i załóż ekwipunek, nakładając bonusy
    equipment_data = player_data.get("equipment", {})
    for slot, item_data in equipment_data.items():
        item = _recreate_item_from_data(item_data)
        if item:
            player.equipment.equip(item)
            player.apply_item_bonus(item)

    # Krok 4: Wczytaj plecak
    inventory_data = player_data.get("inventory", [])
    for item_data in inventory_data:
        item = _recreate_item_from_data(item_data)
        if item:
            player.inventory.append(item)

    # Krok 5: Ustaw aktualne HP na końcu
    player._hit_points = player_data.get("current_hp", player._hit_points_max)


    print(f"Player '{player_name}' loaded successfully.")
    print(player) # Pokaż statystyki wczytanego gracza
    return player

def list_available_players():
    """Lists all available player save files."""
    if not os.path.exists(SAVE_FOLDER_PATH):
        return []
    player_files = [f for f in os.listdir(SAVE_FOLDER_PATH) if f.endswith(".json")]
    return [os.path.splitext(f)[0].capitalize() for f in player_files]

def print_json_file(filename):
    """Prints the contents of a JSON file."""
    filepath = os.path.join(SAVE_FOLDER_PATH, f"{filename.lower()}.json")
    try:
        with open(filepath, "r", encoding="utf-8") as json_file:
            data = json.load(json_file)
            print(json.dumps(data, indent=4))
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error reading save file: {e}")