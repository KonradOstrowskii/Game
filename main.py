from player import Player
from enemy import Troll, Vampire

konrad = Player("Konrad")


cave_troll = Troll("cave_troll")

vampire = Vampire("Dracula")
print(vampire)
while vampire.alive:
        vampire.take_damage(1)
        print(vampire)
