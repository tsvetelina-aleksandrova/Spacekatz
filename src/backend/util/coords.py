class Coords:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __set__(self, attr, value):
		if isinstance(value, int):
			self.attr = value
		else:
			raise ValueError("Coords should be ints")
