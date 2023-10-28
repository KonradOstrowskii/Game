import json

from Game.characters.race import Elf, Dwarf, Orc
from Game.characters.player import Player


def save_player_to_json(player, filename):
    player_data = {
        "name": player.name,
        "level": player._level,
        "lives": player._lives,
        "experience": player._experience,
        "damage": player._damage,
        "hit_points": player._hit_points,
        "race_attributes": {
            "name": player.race.name,
            "bonus_dmg": player.race.bonus_dmg,
            "extra_hit_points": player.race.extra_hit_points,
            "skills": player.race.get_skills_dict()  # Get the skills dictionary
        }
    }

    with open(filename, "w") as json_file:
        json.dump(player_data, json_file, indent=4)


def load_player_from_json(filename):
    with open(filename, 'r') as json_file:
        player_data = json.load(json_file)

    player = Player(player_data["name"])
    player._level = player_data["level"]
    player._experience = player_data["experience"]
    player._damage = player_data["damage"]
    player._hit_points = player_data["hit_points"]

    # Load race attributes
    race_name = player_data["race_attributes"]["name"]
    race_bonus_dmg = player_data["race_attributes"]["bonus_dmg"]
    race_extra_hit_points = player_data["race_attributes"]["extra_hit_points"]
    race_skills = player_data["race_attributes"]["skills"]

    if race_name == "Elf":
        player.race = Elf(name=race_name, bonus_dmg=race_bonus_dmg, extra_hit_points=race_extra_hit_points)
    elif race_name == "Dwarf":
        player.race = Dwarf(name=race_name, bonus_dmg=race_bonus_dmg, extra_hit_points=race_extra_hit_points)
    elif race_name == "Orc":
        player.race = Orc(name=race_name, bonus_dmg=race_bonus_dmg, extra_hit_points=race_extra_hit_points)

    # Add skills to the player based on the loaded race skills
    for skill_name in race_skills:
        skill_function = getattr(player.race, skill_name)
        player.add_skill(skill_name, skill_function)

    # Load more attributes as needed

    return player
