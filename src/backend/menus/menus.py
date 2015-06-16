class MenuOption:
	def __init__(self, select_action):
		self.select_action = select_action
		
	def select(self):
		self.select_action()
		print("Selected menu action was executed")

class Menu:
	pass

class StartMenu(Menu):
	def __init__(self, game):
		Menu.__init__(self)
		self.start = MenuOption(game.start)
		self.show_scoreboard = MenuOption(game.load_scoreboard)
		self.exit = MenuOption(game.exit)

class GameMenu(Menu):
	def __init__(self, game):
		Menu.__init__(self)
		self.resume = MenuOption(game.resume)
		self.end = MenuOption(game.end)
