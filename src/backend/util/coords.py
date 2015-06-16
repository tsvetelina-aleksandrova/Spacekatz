class Coords:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __set__(self, attr, value):
		if isinstance(value, int):
			self.attr = value
		else:
			raise ValueError("Coords should be ints")

class Board:
	def __init__(self, width, height):
		self.matrix = [[0 for x in range(width)] for x in range(height)]
		self. width = width
		self.height = height

	def show(self, sprites):
		for row in self.height:
			for col in self.width:
				symbol = "."
				for sprite in sprites:
					# should also care about size
					if sprite.position.x == row and sprite.position.y == col:
						symbol = "*"
				print symbol,
