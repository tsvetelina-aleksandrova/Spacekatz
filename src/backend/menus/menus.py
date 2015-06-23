class GameMenu:
    def __init__(self, game):
        self.game = game
        self.options = {}

    def select(self, option):
        if option not in self.options.keys():
            raise ValueError("Unexpected menu option was selected")
        game_option = getattr(self.game, self.options[option])

        if callable(game_option):
            game_option()
            print("Selected menu action was executed")
        else:
            raise ValueError("Menu option is not valid")

    def display(self):
        for option in self.options:
            print(option)

    def get_available_options(self):
        return [option for option in sorted(self.options.keys(), reverse=True)]


class StartGameMenu(GameMenu):
    def __init__(self, game):
        GameMenu.__init__(self, game)
        self.options = {
            "Start": "",
            "Scoreboard": "load_scoreboard",
            "Exit": "exit"
        }


class PauseGameMenu(GameMenu):
    def __init__(self, game):
        GameMenu.__init__(self, game)
        self.options = {
            "Resume": "resume",
            "End game": "end"
        }


class KatNameGameMenu(GameMenu):
    def __init__(self, game):
        GameMenu.__init__(self, game)
        self.options = {
            "Start": "start"
        }
