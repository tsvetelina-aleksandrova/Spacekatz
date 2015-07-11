import pygame
import pygame.event
from backend.game import Game
from backend.sprites.kat import Kat
from ui.util.background import StarField
from ui.util.helpers import Helpers
from ui.menu_ui import StartGameMenuUI, PauseGameMenuUI
from ui.menu_ui import PlayerNameGameMenuUI
from ui.menu_ui import ScoreGameMenuUI
from backend.util.coords import Coords
from ui.sprites.kat_ui import KatUI
from ui.sprites.bird_ui import BirdUI
from pygame.sprite import Group

class Spacekatz:
	def __init__(self):
		self.event_listeners = []
		self.actions = {
			"start": False, 
			"exit": False, 
			"resume": False, 
			"end": False
			}
		self.current_event = None
		self.game_size = (Helpers.const["size"]["display_width"],
			Helpers.const["size"]["display_height"])
		
		pygame.init()
		self.screen = pygame.display.set_mode(self.game_size)
		pygame.display.set_caption("Spacekatz")

		self.game = Game(self.game_size)

		self.name_menu = PlayerNameGameMenuUI(self)
		self.score_menu = ScoreGameMenuUI(self)
		self.start_menu = StartGameMenuUI(self)
		self.pause_menu = PauseGameMenuUI(self)

		self.start_menu.set_next_menus({
			"Start": self.name_menu,
			"Scoreboard": self.score_menu
		})
		self.score_menu.set_next_menus({
			"Back": self.start_menu
		})
		
		self.event_listeners.append(self.name_menu)
		self.event_listeners.append(self.score_menu)
		self.event_listeners.append(self.start_menu)
		self.event_listeners.append(self.pause_menu)

		self.start_menu.is_listening = True
		self.game_exit = False

	def play(self):
		self.starfield_backgr = StarField(self.screen, 250)
		clock = pygame.time.Clock()

		kat_name = self.name_menu.current_input
		self.kat_group = Group()
		self.bullet_group = Group()
		self.bird_group = Group()

		kat_back = Kat(Coords(100, 100), 
			kat_name, self.game.board)
		self.kat = KatUI(self.screen, kat_back, self.bullet_group) 
		self.kat.add(self.kat_group)

		self.game.start(self.screen, self.bullet_group, self.bird_group)

		while not self.game_exit:
			clock.tick(60)
			self.screen.fill(Helpers.const["color"]["black"])

			# only the ones that are currently listening
			# will be displayed
			self.start_menu.display()
			self.score_menu.display()
			self.name_menu.display()
			self.pause_menu.display()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.game_exit = True
				else:
					self.current_event = event
					for listener in self.event_listeners:
						listener.notify(event)
			
			for action_name, value in self.actions.items():
				if value:
					getattr(self, action_name + "_action")()

			pygame.display.flip()

	def start_action(self):	
		self.screen.fill(Helpers.const["color"]["black"])
		self.starfield_backgr.redraw_stars()

		self.kat.handle_event(self.current_event)

		Helpers.display_message(self.screen, 
			"Score: " + str(self.kat.kat.score), 80, -200)
		Helpers.display_message(self.screen, 
			"Health: " + str(self.kat.kat.health), 80, 200)
		Helpers.display_message(self.screen, 
			self.kat.kat.name, 50, 50)

		self.kat_group.update(1)
		self.bullet_group.update(0.1)
		self.bird_group.update(0.5)

		self.kat_group.draw(self.screen)
		self.bird_group.draw(self.screen)
		self.bullet_group.draw(self.screen)

		pygame.display.flip()
		

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