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
            expected_callable = menu.options[test_option]

            menu.select(test_option)
            callable_attr = getattr(self.mock_game, expected_callable)
            self.assertTrue(callable_attr.called)

    def test_select_error(self):
        non_existent_option = "TestTest"
        test_attr_name = "players"
        non_callable_option = {test_attr_name: test_attr_name}
        self.mock_game.players = test_attr_name

        for menu in self.menus:
            menu.options.update(non_callable_option)
            with self.assertRaises(ValueError):
                menu.select(non_existent_option)

            with self.assertRaises(ValueError):
                menu.select(test_attr_name)

if __name__ == '__main__':
    unittest.main()
