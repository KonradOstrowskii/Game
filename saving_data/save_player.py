import json
from characters.race import Elf, Dwarf, Orc
from characters.player import Player


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
            "skills": player.race.get_skills_dict()
        }
    }

    with open(filename, "w") as json_file:
        json.dump(player_data, json_file, indent=4)


def load_player_from_json(filename):
    with open(filename, 'r') as json_file:
        player_data = json.load(json_file)

    player = Player(player_data["name"])
    player.level = player_data["level"]
    player.experience = player_data["experience"]
    player.damage = player_data["damage"]
    player.hit_points = player_data["hit_points"]

    # Load race attributes dynamically
    race_name = player_data["race_attributes"]["name"]
    race_bonus_dmg = player_data["race_attributes"]["bonus_dmg"]
    race_extra_hit_points = player_data["race_attributes"]["extra_hit_points"]
    race_skills_data = player_data["race_attributes"]["skills"]

    # Find the race class dynamically based on the race name
    race_class = globals().get(race_name, None)

    if race_class is not None:
        player.race = race_class(name=race_name, bonus_dmg=race_bonus_dmg, extra_hit_points=race_extra_hit_points)

        # Add skills to the player based on the loaded race skills
        for skill_name, skill_function_name in race_skills_data.items():
            skill_function = getattr(player.race, skill_function_name, None)
            if skill_function:
                player.race.add_skill(skill_name, skill_function)

    return player
