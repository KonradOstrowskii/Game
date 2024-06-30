import os
import unittest
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from combat.fight import Fight
from characters.player import Player
from characters.enemy import Vampire


class TestGame(unittest.TestCase):

    def test_player_creation(self):
        player = Player(name="TestPlayer")
        self.assertEqual(player.name, "TestPlayer")
        self.assertEqual(player._lives, 1)
        self.assertEqual(player._level, 1)
        self.assertEqual(player._experience, 0)
        self.assertEqual(player._damage, 5)
        self.assertEqual(player._hit_points, 10)
        self.assertIsNone(player.race)
        self.assertDictEqual(player.skills, {})
        self.assertTrue(player.alive)

    def test_player_take_damage(self):
        player = Player(name="TestPlayer")
        initial_hit_points = player._hit_points
        damage_taken = 3
        player.take_damage(damage_taken)
        self.assertEqual(player._hit_points, initial_hit_points - damage_taken)

    def test_player_level_up(self):
        player = Player(name="TestPlayer")
        player.gain_experience(500)
        self.assertEqual(player._level, 2)
        self.assertEqual(player._damage, 7)
        self.assertEqual(player._hit_points, 20)

    def test_fight_start(self):
        player = Player(name="TestPlayer")
        vamp = Vampire("Vamp", 10, 1, 1, 200, alive=True)
        fight = Fight(player, vamp)
        fight.start()
        self.assertIsNotNone(fight)

    def test_enemy_take_damage(self):
        vampire = Vampire("Vamp", 10, 1, 1, 200, alive=True)
        initial_hit_points = vampire.hit_points
        damage_taken = 5
        vampire.take_damage(damage_taken)
        if vampire.dodges():
            self.assertEqual(vampire.hit_points, initial_hit_points)
        else:
            self.assertEqual(vampire.hit_points, initial_hit_points - damage_taken)


if __name__ == "__main__":
    unittest.main()
