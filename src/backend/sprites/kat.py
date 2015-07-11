from backend.sprites.bullet import Bullet


class Kat:
	def __init__(self, position, name, board):
		self.position = position # x and y ints
		self.health = 6 # max = 6, min = 0
		self.strength = 1 # min = 1, max = 5
		self.score = 0
		self.name = name
		self.is_dead = False
		self.board = board

	def move(self, x_delta=0, y_delta=0):
		self.position.x += x_delta
		self.position.y += y_delta
		print(self.position.x)
		print(self.position.y)
		cell = self.board.matrix[self.position.x][self.position.y]
		if cell == "*":
			bird = board.get_bird_on_pos(self.position.x, self.position.y)
			bird.get_shot()

	def shoot(self):
		return Bullet(self.position, self.strength, self.board, True)

	def get_shot(self, strength):
		print("Kat got shot")
		self.health -= strength
		if self.health <= 0:
			self.is_dead = True