from combat.fight import Fight
from characters.player import Player
from characters.enemy import Vampire
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


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
    assert player._damage == 7
    assert player._hit_points == 20


def test_fight_start():
    player = Player(name="TestPlayer")
    vamp = Vampire("Vamp", 10, 1, 1, 200, alive=True)
    fight = Fight(player, vamp)
    fight.start()


def test_enemy_take_damage():
    vampire = Vampire("Vamp", 10, 1, 1, 200, alive=True)
    initial_hit_points = vampire.hit_points
    damage_taken = 5
    vampire.take_damage(damage_taken)
    if vampire.dodges():
        assert vampire.hit_points == initial_hit_points
    else:
        assert vampire.hit_points == initial_hit_points - damage_taken


if __name__ == "__main__":
    test_player_creation()
    test_player_take_damage()
    test_player_level_up()
    test_fight_start()
    test_enemy_take_damage()
