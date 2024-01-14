from characters.creating_player import create_player, print_race_descriptions
from combat.fight import Fight
from saving_data.save_player import save_player_to_json, load_player_from_json
from characters.enemy import *


from characters.creating_player import create_player, print_race_descriptions
from saving_data.save_player import save_player_to_json, load_player_from_json

player = create_player()

save_player_to_json(player)

