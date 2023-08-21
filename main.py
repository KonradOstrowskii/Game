from player import Player
from enemy import Enemy, Troll

konrad = Player("Konrad")
random_monster = Enemy("Basic enemy",12,1)
print(random_monster)
random_monster.take_damage(4)
print(random_monster)

random_monster.take_damage(8)
print(random_monster)


random_monster.take_damage(9)
print(random_monster)

cave_troll = Troll("cave_troll",14)

print(cave_troll)