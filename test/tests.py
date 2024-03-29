from characters.player import Player
from combat.fight import Fight
from characters.enemy import Vampire


# Test Player class
def test_player_creation():
    player = Player(name="TestPlayer")
    assert player.name == "TestPlayer"
    assert player._lives == 1
    assert player._level == 1
    assert player._experience == 0
    assert player._damage == 5
    assert player._hit_points == 10
    assert player.race is None
    assert player.skills == {}
    assert player.alive is True


def test_player_take_damage():
    player = Player(name="TestPlayer")
    initial_hit_points = player._hit_points
    damage_taken = 3
    player.take_damage(damage_taken)
    assert player._hit_points == initial_hit_points - damage_taken


def test_player_level_up():
    player = Player(name="TestPlayer")
    player.gain_experience(500)
    assert player._level == 2
    assert player._damage == 7  # Check if damage increased after leveling up
    assert player._hit_points == 20  # Check if hit points increased after leveling up


# Test Fight class
def test_fight_start():
    player = Player(name="TestPlayer")
    Vamp = Vampire("Vamp", 10, 1, 1, 200,alive=True)
    fight = Fight(player, Vampire)
    fight.start()


def test_enemy_take_damage():
    vampire = Vampire("Vamp", 10, 1, 1, 200, alive=True)
    initial_hit_points = vampire.hit_points
    damage_taken = 5
    vampire.take_damage(damage_taken)
    assert vampire.hit_points > initial_hit_points - damage_taken


