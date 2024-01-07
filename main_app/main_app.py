from Game.characters.creating_player import create_player, print_race_descriptions
from Game.combat.fight import Fight
from Game.saving_data.save_player import save_player_to_json, load_player_from_json
from Game.characters.enemy import *


def main():
    # Step 2: Create instances of Player and Vampire
    # player = create_player()
    # vampire = Troll("Count Dracula", hit_points=30, lives=1, damage=8, experience_reward=300)
    # #
    # # # Step 3: Create an instance of the Fight class
    # # vampire_fight = Fight(player, vampire)
    # #
    # # # Step 4: Start the fight
    # # vampire_fight.start()
    #
    # save_player_to_json(player, 'postac.json')
    load_player_from_json('postac.json')
if __name__ == "__main__":
    main()
