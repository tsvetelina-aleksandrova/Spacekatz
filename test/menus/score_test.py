import unittest
import sys
import os
sys.path.append(os.path.join('..\..', 'src'))
from backend.menus.score import Score


class ScoreTest(unittest.TestCase):
    def setUp(self):
        self.player_name = "Test"
        self.points = 10
        self.score = Score(self.player_name, self.points)
        self.score_id = "1234"
        self.score2 = Score("Test2")

    def test_increase_score(self):
        incr_points = 20
        self.score.increase_score(incr_points)
        self.assertEqual(self.score.get_points(), self.points + incr_points)

    def test_get_as_map(self):
        expected_dict = {
            "player": self.player_name,
            "points": self.points
        }
        self.assertDictEqual(self.score.get_as_dict(), expected_dict)

    def test_eq(self):
        self.score.set_id(self.score_id)
        self.score2.set_id(self.score_id)
        self.assertTrue(self.score == self.score2)

    def test_not_eq(self):
        score_id2 = "12345678"
        self.score.set_id(self.score_id)
        self.score2.set_id(score_id2)
        self.assertFalse(self.score == self.score2)

    def test_eq_id_not_set(self):
        self.score.set_id(self.score_id)
        with self.assertRaises(AttributeError):
            self.assertFalse(self.score == self.score2)

    def test_str(self):
        expected_str = "Player: " + self.player_name
        expected_str += " Score: " + str(self.points)
        self.assertEqual(str(self.score), expected_str)


if __name__ == '__main__':
    unittest.main()
