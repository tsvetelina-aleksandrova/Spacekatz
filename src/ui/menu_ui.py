import pygame
from backend.menus.menus import GameMenu, StartGameMenu, PauseGameMenu
from ui.util.helpers import Helpers 


class GameMenuUI():
	def __init__(self, screen, game):
		self.screen = screen
		self.game = game
		self.menu = GameMenu(game)
		self.text_rects = {}
		self.is_pending_input = True

	def display(self):
		self.is_pending_input = True
		y_delta = 0
		for option_name in self.menu.get_available_options():
			new_text_rect = Helpers.display_message(self.screen, 
				option_name, 0, y_delta)
			self.text_rects.update({option_name: new_text_rect})
			y_delta += 50

	def handle_event(self, event):
		if pygame.mouse.get_pressed():
			mouse_pos = pygame.mouse.get_pos()
			for option_name, rect in self.text_rects.items():
				if rect.collidepoint(mouse_pos):
					is_pending_input = False
					self.menu.select(option_name)
					return


class StartGameMenuUI(GameMenuUI):
	def __init__(self, screen, game):
		GameMenuUI.__init__(self, screen, game)
		self.menu = StartGameMenu(game)


class PauseGameMenuUI(GameMenuUI):
	def __init__(self, screen, game):
		GameMenuUI.__init__(self, screen, game)
		self.menu = PauseGameMenu(game)