class Bullet():
	def __init__(self, position, strength, board, from_player):
		self.position = position # x and y ints
		self.strength = strength # min = 1, max = 5
		self.board = board
		self.from_player = from_player

	def move(self):
		while self.position.y < self.board.height:
			self.position.y += 20
			if self.from_player:
				if self.board.matrix[self.position.x][self.position.y] == "*":
					bird = board.get_bird_on_pos(self.position.x, self.position.y)
					bird.get_shot()
			else:
				if self.board.matrix[self.position.x][self.position.y] == "^":
					kat = board.get_kat_on_pos(self.position.x, self.position.y)
					kat.get_shot()


