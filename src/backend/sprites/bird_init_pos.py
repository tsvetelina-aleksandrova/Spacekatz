# iterators that provide init. positions for enemies

class SingleBlockInitPos():
	def __init__(self, row_num=5, col_num=6):
		self.current_row = 0
		self.current_col = 0
		self.row_num = row_num
		self.col_num = col_num

	def __iter__(self):
		return self
	def __next__ (self): 
		if self.current_row == self.row_num and
				self.current_col == self.col_num:
			raise StopIteration
		if self.current_col == self.col_num:
			self.current_col = 0
			self.current_row += 1
		new_coords = Coords(self.current_col + 10, self.current_row + 10)
		self.current_col += 1
		return new_coords


class DiagInitPos():
	def __init__(self, enemy_num, direction):
		self.current_row = 0
		self.current_col = 0
		self.row_num = row_num
		self.col_num = col_num
		self.direction = direction

	def __iter__(self):
		return self

	def __next__ (self): 
		if self.current_row == self.row_num and
				self.current_col == self.col_num:
			raise StopIteration
		if self.current_col == self.col_num:
			self.current_col = 0
			self.current_row += 1
		new_coords = Coords(self.current_col + 10, self.current_row + 10)
		self.current_col += 1
		return new_coords


class BlockInitPos():
	def __init__(self, block_num=5, block_enemy_num=4):
		self.current_block = 0
		self.current_enemy = 0
		self.block_num = block_num
		self.block_enemy_num = block_enemy_num

	def __iter__(self):
		return self

	def __next__ (self): 
		if self.current_row == self.row_num and
				self.current_col == self.col_num:
			raise StopIteration
		if self.current_col == self.col_num:
			self.current_col = 0
			self.current_row += 1
		new_coords = Coords(self.current_col + 10, self.current_row + 10)
		self.current_col += 1
		return new_coords

		
class SingleInitPos():
	def __init__(self):
		self.current = 0
		self.max_enemies = 1

	def __iter__(self):
		return self

	def __next__ (self): 
		if self.current == self.max_enemies:
			raise StopIteration
		return Coords(40, 40)