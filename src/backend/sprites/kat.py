class Kat:
	def __init__(self, position, name):
		self.position = position # x and y ints
		self.health = 10 # max = 10, min = 0
		self.strength = 1 # min = 1, max = 5
		self.score = 0
		self.name = name

	def move(self, x_delta=0, y_delta=0):
		self.position.x += x_delta
		self.position.y += y_delta

	def shoot(self):
		bullet = Bullet(self.position, self.strength)
		bullet.move()
