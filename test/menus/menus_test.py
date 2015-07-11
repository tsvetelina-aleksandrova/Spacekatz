import unittest
import mock
import sys
import os
sys.path.append(os.path.join('..\..', 'src'))

from backend.game import Game
from backend.menus.menus import GameMenu, StartGameMenu, PauseGameMenu


class GameMenuTest(unittest.TestCase):

    @mock.patch('backend.game.Game')
    def setUp(self, mock_game):
        self.mock_game = mock_game
        self.menus = [
            StartGameMenu(mock_game),
            PauseGameMenu(mock_game)
        ]

    def test_select(self):
        for menu in self.menus:
            test_option = menu.get_available_options()[0]
            if not menu.options[test_option] == "":
                expected_prop = menu.options[test_option]

                menu.select(test_option)
                callable_attr = getattr(
                    self.mock_game, expected_prop)
                self.assertTrue(callable_attr)

    def test_select_error(self):
        non_existent_option = "TestTest"
        for menu in self.menus:
            with self.assertRaises(ValueError):
                menu.select(non_existent_option)

if __name__ == '__main__':
    unittest.main()
