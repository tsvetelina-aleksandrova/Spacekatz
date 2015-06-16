class Game:
	def __init__(self, width, height, player_num=1):
		self.scoreboard = Scoreboard()
		self.board = Board(width, height)
		self.player_num = player_num
		self.players = [Player() for i in range(player_num)]
		
		self.levels = [Level(1), Level(2), 
			Level(3), Level(4), Level(5)]
		

	def init(self):
		menu = StartMenu(self)
		menu.show()

	def start(self):
		self.current_level = 0
		self.levels[self.current_level].start()
		self.board.show()

	def pause(self):
		menu = GameMenu(self)
		menu.show()
		
	def load_scoreboard(self):
		self.scoreboard.show()

	def resume(self):
		print("Gameplay is resumed")
		self.board.show()

	def end(self):
		print("Game is ended")
		for player in self.players:
			self.scoreboard.add(Score(player.name, player.score))
		self.load_scoreboard()

	def exit(self):
		print("Game is exited")


	def next_level(self):
		if self.current_level == len(self.levels) - 1:
			self.end()
		else:
			self.current_level += 1
			self.levels[self.current_level].start()
