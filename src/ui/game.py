import pygame
import pygame.event
from backend.game import Game
from ui.util.starfield import StarField
from ui.util.helpers import Helpers
from ui.menu_ui import StartGameMenuUI, PauseGameMenuUI
from ui.menu_ui import PlayerNameGameMenuUI
from ui.menu_ui import ScoreGameMenuUI

class Spacekatz:
	def __init__(self):
		self.event_listeners = []

	def play(self):
		pygame.init()
		const = Helpers.get_constants()

		screen = pygame.display.set_mode((const["size"]["display_width"],
										const["size"]["display_height"]))
		pygame.display.set_caption("Spacekatz")

		self.game = Game(const["size"]["display_width"], 
			const["size"]["display_height"])

		name_menu = PlayerNameGameMenuUI(screen, self)
		score_menu = ScoreGameMenuUI(screen, self)
		start_menu = StartGameMenuUI(screen, self)
		pause_menu = PauseGameMenuUI(screen, self)

		start_menu.set_next_menus({
			"Start": name_menu,
			"Scoreboard": score_menu
		})
		score_menu.set_next_menus({
			"Back": start_menu
		})
		
		self.event_listeners.append(name_menu)
		self.event_listeners.append(score_menu)
		self.event_listeners.append(start_menu)
		self.event_listeners.append(pause_menu)


		clock = pygame.time.Clock()
		star_field = StarField(screen, 250)
		game_exit = False

		screen.fill(const["color"]["black"])

		while not game_exit:
			clock.tick(60)
			screen.fill(const["color"]["black"])

			start_menu.display()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					game_exit = True
				for listener in self.event_listeners:
					listener.notify(event)

			# star_field.redraw_stars()
			pygame.display.update()

	def start(self):
		self.game.start()

	def pause(self):
		pass

	def resume(self):
		pass

	def end(self):
		pass

	def exit(self):
		print("Game is exited")

	def next_level(self):
		pass