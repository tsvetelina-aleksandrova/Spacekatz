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
		self.actions = {
			"start": False, 
			"exit": False, 
			"resume": False, 
			"end": False
			}

	def play(self):
		pygame.init()

		self.screen = pygame.display.set_mode((Helpers.const["size"]["display_width"],
										Helpers.const["size"]["display_height"]))
		pygame.display.set_caption("Spacekatz")

		self.game = Game(Helpers.const["size"]["display_width"], 
			Helpers.const["size"]["display_height"])

		name_menu = PlayerNameGameMenuUI(self.screen, self)
		score_menu = ScoreGameMenuUI(self.screen, self)
		start_menu = StartGameMenuUI(self.screen, self)
		pause_menu = PauseGameMenuUI(self.screen, self)

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

		start_menu.is_listening = True

		clock = pygame.time.Clock()

		self.game_exit = False

		self.starfield_backgr = StarField(self.screen, 250)

		while not self.game_exit:
			clock.tick(60)
			self.screen.fill(Helpers.const["color"]["black"])

			# only the ones that are currently listening
			# will be displayed
			start_menu.display()
			score_menu.display()
			name_menu.display()
			pause_menu.display()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.game_exit = True
				for listener in self.event_listeners:
					listener.notify(event)
			
			for action_name, value in self.actions.items():
				if value:
					getattr(self, action_name + "_action")()

			pygame.display.flip()

	def start_action(self):
		#self.game.start()
		
		kat_img = Helpers.get_image('/img/bird.png')
		self.screen.fill(Helpers.const["color"]["black"])
		self.screen.blit(kat_img, (100, 100))

		self.starfield_backgr.redraw_stars()

	def pause_action(self):
		pass

	def resume_action(self):
		pass

	def end_action(self):
		pass

	def exit_action(self):
		print("Game is exited")
		self.game_exit = True

	def next_level_action(self):
		pass