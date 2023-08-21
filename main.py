from player import Player
from race import Elf , Dwarf
from enemy import Troll, Vampire

player_name = input("Please chose your player name : ")

player = Player(player_name)

player_race = input("Please choose your race : (Elf, Dwarf): ").casefold()
if  player_race == "elf":
    print("You choose to be Elf")
    player(Elf)
else:
    player(Dwarf)
    print("You choose to be Dwarf")
