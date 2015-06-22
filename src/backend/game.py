from backend.menus.scoreboard import Scoreboard
from backend.menus.menus import GameMenu, StartGameMenu, PauseGameMenu
from backend.util.board import Board
# from backend.sprites.kat import Player

class Game:
	def __init__(self, width, height, player_num=1):
		self.scoreboard = Scoreboard()
		self.board = Board(width, height)
		self.player_num = player_num
		# self.players = [Player() for i in range(player_num)]
		
		#self.levels = [Level(1), Level(2), 
		#	Level(3), Level(4), Level(5)]

	def init(self):
		menu = StartGameMenu(self)
		menu.display()
		# get user input

	def start(self):
		self.current_level = 0
		self.levels[self.current_level].start()

	def pause(self):
		self.levels[self.current_level].pause()
		menu = PauseGameMenu(self)
		menu.display()
		# get user input
		
	def load_scoreboard(self):
		self.scoreboard.display()

	def resume(self):
		print("Gameplay is resumed")
		self.levels[self.current_level].start()

	def end(self):
		self.levels[self.current_level].pause()
		self.board.clear()
		print("Game is ended")
		for player in self.players:
			self.scoreboard.add(Score(player.name, player.score))
		self.load_scoreboard()

	def exit(self):
		print("Game is exited")
		# exit

	def next_level(self):
		self.levels[self.current_level].pause()
		self.board.clear()
		if self.current_level == len(self.levels) - 1:
			print("No more levels. Game is completed!")
			self.end()
		else:
			self.current_level += 1
			self.levels[self.current_level].start()
