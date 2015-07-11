class Bullet():
	def __init__(self, position, strength, board, from_player):
		self.position = position # x and y ints
		self.strength = strength # min = 1, max = 5
		self.board = board
		self.from_player = from_player
		self.to_remove = False

	def move(self):
		mtrx = self.board.matrix
		if self.from_player:
			self.position.y -= 10
			if self.position.y not in range (self.board.height):
				self.to_remove = True
			else:
				cell = mtrx[self.position.x][self.position.y]
				if cell == "*":
					bird = board.get_bird_on_pos(self.position.x, 
						self.position.y)
					bird.get_shot()
		else:
			self.position.y += 10
			if self.position.y not in range (self.board.height):
				self.to_remove = True
			else:
				cell = mtrx[self.position.x][self.position.y]
				if cell == "^":
					kat = board.get_kat_on_pos(self.position.x, 
						self.position.y)
					kat.get_shot()
