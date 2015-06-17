class Bird:
	def __init__(self, position, move_strategy):
		self.position = position # x and y ints
		self.health = 2 # max = 10, min = 0
		self.strength = 1 # min = 1, max = 5
		self.move_strategy = move_strategy

	def move(self):
		self.position.x += self.move_strategy.get_delta_x()
		self.position.y += self.move_strategy.get_delta_y()
		print("Moved according to the strategy")

	def shoot(self):
		# make it random
		bullet = Bullet(self.position, self.strength)
		bullet.move()
