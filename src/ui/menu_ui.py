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

	# fix this, this sucks
	def handle_event(self, event, is_special_start=False):
		if self.is_pending_input:
			
			if pygame.mouse.get_pressed()[0] == 1:
				print(pygame.mouse.get_pressed()[0])
				mouse_pos = pygame.mouse.get_pos()
				for option_name, rect in self.text_rects.items():
					if rect.collidepoint(mouse_pos):
						self.is_pending_input = False
						if is_special_start and option_name == "Start":
							self.game_ui.name_menu.is_pending_input = True
						else: 
							self.menu.select(option_name)
						return


class StartGameMenuUI(GameMenuUI):
	def __init__(self, screen, game, game_ui=None):
		GameMenuUI.__init__(self, screen, game, game_ui)
		self.menu = StartGameMenu(game)

	def handle_event(self, event, is_special_start=True):
		GameMenuUI.handle_event(self, event, is_special_start)


class KatNameGameMenuUI(GameMenuUI):
	def __init__(self, screen, game, game_ui=None):
		GameMenuUI.__init__(self, screen, game, game_ui)
		self.menu = KatNameGameMenu(game)
		self.is_pending_input = False
		self.current_input = ""

	def display(self):
		GameMenuUI.display(self)
		if self.is_pending_input:
			self.current_input = Helpers.ask(self.screen, "Name", 
				self.current_input, 0, 50)


class PauseGameMenuUI(GameMenuUI):
	def __init__(self, screen, game, game_ui=None):
		GameMenuUI.__init__(self, screen, game, game_ui)
		self.menu = PauseGameMenu(game)