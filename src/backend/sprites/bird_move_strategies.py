class InPlaceStrategy:
	def get_delta_x(self):
		return 0

	def get_delta_y(self):
		return 0

class DiagonalStrategy:
	# pass diagonally across screen
	def __init__(self, direction='tl'):
		self.direction = direction

	def get_delta_x(self):
		pass

	def get_delta_y(self):
		pass

	# bl, br, tl, tr 
	# bottom left, bottom right, top left, top right
	@static
	def get_available_directions():
		return ["bl", "br", "tl", "tr"]

class BlockStrategy:
	# move in tiny blocks down accross screen
	def get_delta_x(self):
		return 0

	def get_delta_y(self):
		return 10

class BossStrategy:
	# follow players and avoid bullets
	def get_delta_x(self):
		pass

	def get_delta_y(self):
		pass