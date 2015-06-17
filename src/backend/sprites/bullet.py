class Bullet:
	def __init__(self, position, strength):
		self.position = position # x and y ints
		self.strength = strength # min = 1, max = 5

	def move(self):
		self.position.y += 20
