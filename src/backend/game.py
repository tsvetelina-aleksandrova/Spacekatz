from backend.menus.scoreboard import Scoreboard
from backend.menus.menus import GameMenu, StartGameMenu
from backend.menus.menus import PauseGameMenu, PlayerNameGameMenu
from backend.util.board import Board
from backend.util.coords import Coords
from backend.sprites.kat import Kat
from backend.levels import Level


class Game:
	def __init__(self, size):
		self.scoreboard = Scoreboard()
		self.board = Board(size)
		self.kat_name = ""
		self.player = Kat(Coords(0, 0), self.kat_name, self.board)
		
		self.levels = [
			Level(self.board, 1), 
			Level(self.board, 2), 
			Level(self.board, 3), 
			Level(self.board, 4), 
			Level(self.board, 5)
		]
		
	def play(self):
		menu = StartGameMenu(self)
		menu.display()

	def start(self, screen=None, bullet_group=None, bird_group=None):
		self.current_level = 0
		print(self.current_level)
		print(self.levels[self.current_level])
		self.levels[self.current_level].get_enemies()

	def pause(self):
		self.levels[self.current_level].pause()
		menu = PauseGameMenu(self)
		menu.display()

	def resume(self):
		print("Gameplay is resumed")

	def end(self):
		self.levels[self.current_level].pause()
		self.board.clear()
		print("Game is ended")
		self.scoreboard.add(Score(self.kat_name, self.player.score))
		self.load_scoreboard()

	def exit(self):
		print("Game is exited")

	def next_level(self):
		self.levels[self.current_level].pause()
		self.board.clear()
		if self.current_level == len(self.levels) - 1:
			print("No more levels. Game is completed!")
			self.end()
		else:
			self.current_level += 1
			self.levels[self.current_level].start()
