class GameMenu:
    def __init__(self, game):
        self.game = game
        self.options = {}

    def select(self, option):
        if option not in self.options.keys():
            raise ValueError("Unexpected menu option was selected")

        game_option = self.options[option]
        if callable(game_option):
            game_option()
            print("Selected menu action was executed")
        elif not game_option == "":
            raise ValueError("Menu option is not valid")

    def get_available_options(self):
        return [option for option in sorted(self.options.keys(), reverse=True)]


class StartGameMenu(GameMenu):
    def __init__(self, game):
        GameMenu.__init__(self, game)
        self.options = {
            "Start": "",
            "Scoreboard": "",
            "Exit": self.game.exit
        }


class PauseGameMenu(GameMenu):
    def __init__(self, game):
        GameMenu.__init__(self, game)
        self.options = {
            "Resume": self.game.resume,
            "End game": self.game.end
        }


class PlayerNameGameMenu(GameMenu):
    def __init__(self, game):
        GameMenu.__init__(self, game)
        self.options = {
            "Start": self.game.start
        }

class ScoreGameMenu(GameMenu):
    def __init__(self, game):
        GameMenu.__init__(self, game)
        self.options = {
            "Back": ""
        }