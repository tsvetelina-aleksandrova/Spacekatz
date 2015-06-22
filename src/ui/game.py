import pygame
import pygame.event
from backend.game import Game
from ui.util.starfield import StarField
from ui.util.helpers import Helpers
from ui.menu_ui import StartGameMenuUI, PauseGameMenuUI

class Spacekatz:
	@staticmethod
	def play():
		pygame.init()
		const = Helpers.get_constants()

		screen = pygame.display.set_mode((const["size"]["display_width"],
										const["size"]["display_height"]))
		pygame.display.set_caption("Spacekatz")
		game = Game(const["size"]["display_width"], const["size"]["display_height"])
		start_menu = StartGameMenuUI(screen, game)
		pause_menu = PauseGameMenuUI(screen, game)
		
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
				if start_menu.is_pending_input:
					start_menu.handle_event(event)

			star_field.redraw_stars()
			pygame.display.update()