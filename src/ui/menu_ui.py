import pygame
from backend.menus.menus import GameMenu, StartGameMenu
from backend.menus.menus import PauseGameMenu, PlayerNameGameMenu
from backend.menus.menus import ScoreGameMenu
from ui.util.helpers import Helpers 
from backend.listener import Listener
from backend.menus.scoreboard import Scoreboard

class GameMenuUI(Listener):
	def __init__(self, screen, game):
		Listener.__init__(self)
		self.screen = screen
		self.game = game
		self.menu = GameMenu(game)
		self.text_rects = {}
		self.next_menus = None

	def set_next_menus(self, next_menus):
		# chain
		self.next_menus = next_menus

	def display(self):
		if self.is_listening:
			y_delta = 0
			for option_name in self.menu.get_available_options():
				new_text_rect = Helpers.display_message(self.screen, 
					option_name, 0, y_delta)
				self.text_rects.update({option_name: new_text_rect})
				y_delta += 50

	def handle_event(self, event):
		if self.is_listening:
			mouse_pos = Helpers.get_mouse_click_pos()
			if mouse_pos:
				for option_name, rect in self.text_rects.items():
					if rect.collidepoint(mouse_pos):
						self.is_listening = False

						if self.next_menus is not None:
							if option_name in self.next_menus.keys():
								opt_next_menu = self.next_menus[option_name]
								opt_next_menu.is_listening = True
								return
						# no next menus
						self.menu.select(option_name)


class StartGameMenuUI(GameMenuUI):
	def __init__(self, screen, game):
		GameMenuUI.__init__(self, screen, game)
		self.menu = StartGameMenu(game)


class PlayerNameGameMenuUI(GameMenuUI):
	def __init__(self, screen, game):
		GameMenuUI.__init__(self, screen, game)
		self.menu = PlayerNameGameMenu(game)
		self.current_input = ""

	def display(self):
		if self.is_listening:
			self.screen.fill(Helpers.const["color"]["black"])
			GameMenuUI.display(self)
			self.current_input = Helpers.ask(self.screen, "Name", 
				self.current_input, 0, 50)


class ScoreGameMenuUI(GameMenuUI):
	def __init__(self, screen, game):
		GameMenuUI.__init__(self, screen, game)
		self.menu = ScoreGameMenu(game)

	def display(self):
		if self.is_listening:
			self.screen.fill(Helpers.const["color"]["black"])
			scoreboard = Scoreboard()
			y_delta = -100
			for score in scoreboard.get_all():	
				Helpers.display_message(self.screen, 
					str(score), 0, y_delta)
				y_delta += 50
			GameMenuUI.display(self)


class PauseGameMenuUI(GameMenuUI):
	def __init__(self, screen, game):
		GameMenuUI.__init__(self, screen, game)
		self.menu = PauseGameMenu(game)
