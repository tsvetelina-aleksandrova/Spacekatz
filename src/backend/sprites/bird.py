class Bird:
	def __init__(self, position, move_strategy):
		self.position = position # x and y ints
		self.health = 2 # max = 10, min = 0
		self.strength = 1 # min = 1, max = 5
		self.move_strategy = move_strategy

	def move(self):
		print("Moved according to the strategy")

	def shoot(self):
		bullet = Bullet(self.position, self.strength)
		bullet.move()
