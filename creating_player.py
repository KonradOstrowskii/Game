from player import Player
from race import Elf , Dwarf

player_name = input("Please chose your player name : ")
elf_race = Elf()
dwarf_race = Dwarf()
player = Player(player_name)

available_race = ("Elf or Dwarf")
print(available_race)
print(Elf.__str__(elf_race))
print(Dwarf.__str__(dwarf_race))
race_choice = input("Choose a race: ")

# Set player's race based on choice
if race_choice.lower() == "elf":
    player.race = elf_race
    player.apply_race_bonuses()
elif race_choice.lower() == "dwarf":
    player.race = dwarf_race
    player.apply_race_bonuses()
print(player)  
print(player.take_damage(8))
print(player.take_damage(8))
print(player.take_damage(8))
