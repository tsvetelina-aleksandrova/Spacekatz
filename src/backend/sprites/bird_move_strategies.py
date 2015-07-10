class InPlaceStrategy():
	def get_delta_x(self):
		return 0

	def get_delta_y(self):
		return 0

class DiagonalStrategy():
	# bl, br, tl, tr 
	# bottom left, bottom right, top left, top right
	directions = ["bl", "br", "tl", "tr"]
	
	# pass diagonally across screen
	def __init__(self, direction='tl'):
		self.direction = direction

	def get_delta_x(self):
		return 0

	def get_delta_y(self):
		return 0


class BlockStrategy():
	# move in tiny blocks down accross screen
	def get_delta_x(self):
		return 0

	def get_delta_y(self):
		return 10

class BossStrategy():
	# follow players and avoid bullets
	def get_delta_x(self):
		return 0

	def get_delta_y(self):
		return 0