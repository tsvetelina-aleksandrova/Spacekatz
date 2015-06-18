class Kat:
	def __init__(self, position, name, board):
		self.position = position # x and y ints
		self.health = 10 # max = 10, min = 0
		self.strength = 1 # min = 1, max = 5
		self.score = 0
		self.name = name
		self.is_dead = False

	def move(self, x_delta=0, y_delta=0):
		self.position.x += x_delta
		self.position.y += y_delta
		if self.board[self.position.x][self.position.y] == "*":
			bird = board.get_bird_on_pos(self.position.x, self.position.y)
			bird.get_shot()

	def shoot(self):
		bullet = Bullet(self.position, self.strength, self.board, True)
		bullet.move()

	def get_shot(self, strength):
		self.health -= strength
		if self.health <= 0:
			self.is_dead = True
			# remove from board