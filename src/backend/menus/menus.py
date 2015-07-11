class GameMenu:

    def __init__(self, game):
        self.game = game
        self.options = {}

    def select(self, option):
        if option not in self.options.keys():
            raise ValueError("Unexpected menu option was selected")
        game_option = self.options[option]
        if game_option == "":
            return

        self.game.actions[game_option] = True
        print(option)
        print("Selected menu action was executed")

    def get_available_options(self):
        return [option for option in sorted(self.options.keys(), reverse=True)]


class StartGameMenu(GameMenu):

    def __init__(self, game):
        GameMenu.__init__(self, game)
        self.options = {
            "Start": "",
            "Scoreboard": "",
            "Exit": "exit"
        }


class PauseGameMenu(GameMenu):

    def __init__(self, game):
        GameMenu.__init__(self, game)
        self.options = {
            "Resume": "resume",
            "End game": "end"
        }


class PlayerNameGameMenu(GameMenu):

    def __init__(self, game):
        GameMenu.__init__(self, game)
        self.options = {
            "Start": "start"
        }


class ScoreGameMenu(GameMenu):

    def __init__(self, game):
        GameMenu.__init__(self, game)
        self.options = {
            "Back": ""
        }
