import pygame
from backend.menus.menus import GameMenu, StartGameMenu
from backend.menus.menus import PauseGameMenu, KatNameGameMenu
from ui.util.helpers import Helpers 


class GameMenuUI():
	def __init__(self, screen, game, game_ui=None):
		self.screen = screen
		self.game = game
		self.menu = GameMenu(game)
		self.text_rects = {}
		self.is_pending_input = True
		if game_ui:
			self.game_ui = game_ui

	def display(self):
		if self.is_pending_input:
			y_delta = 0
			for option_name in self.menu.get_available_options():
				new_text_rect = Helpers.display_message(self.screen, 
					option_name, 0, y_delta)
				self.text_rects.update({option_name: new_text_rect})
				y_delta += 50

	def handle_event(self, event):
		if self.is_pending_input:
			# mouse pressing is not ok
			if pygame.mouse.get_pressed():
				mouse_pos = pygame.mouse.get_pos()
				for option_name, rect in self.text_rects.items():
					if rect.collidepoint(mouse_pos):
						self.is_pending_input = False
						if option_name == "Start":
							self.game_ui.name_menu.is_pending_input = True
						else: 
							self.menu.select(option_name)
						return


class StartGameMenuUI(GameMenuUI):
	def __init__(self, screen, game, game_ui=None):
		GameMenuUI.__init__(self, screen, game, game_ui)
		self.menu = StartGameMenu(game)


class KatNameGameMenuUI(GameMenuUI):
	def __init__(self, screen, game, game_ui=None):
		GameMenuUI.__init__(self, screen, game, game_ui)
		self.menu = KatNameGameMenu(game)
		self.is_pending_input = False

	def display(self):
		GameMenuUI.display(self)
		if self.is_pending_input:
			print("getname")
			Helpers.ask(self.screen, "Name")


class PauseGameMenuUI(GameMenuUI):
	def __init__(self, screen, game, game_ui=None):
		GameMenuUI.__init__(self, screen, game, game_ui)
		self.menu = PauseGameMenu(game)