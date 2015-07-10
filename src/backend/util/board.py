class Board:
	def __init__(self, size):
		self.width = size[0]
		self.height = size[1]
		self.matrix = [
			[0 for x in range(self.width)] 
			for x in range(self.height)
		]

	def set_enemies(self, enemies):
		self.enemies = enemies
		self.sprites.extend(enemies)

	def set_players(self, players):
		self.players = players

	def refresh(self):
		self.enemies = [enemy for enemy in self.enemies 
			if not enemy.is_dead]
		self.players = [player for player in self.players 
			if not player.is_dead]

		for row in self.height:
			for col in self.width:
				matrix[row][col] = "."
				for enemy in self.enemies:
					if self.__check_sprite_in_cell(enemy, row, col):
						matrix[row][col] = "*"
				for player in self.players:
					if self.__check_sprite_in_cell(player, row, col):
						matrix[row][col] = "^"

	def __check_sprite_in_cell(self, sprite, row, col):
			# position refers to the center of the sprite rect
		# rect is 100x100
		if row in range(sprite.position.x - 50, 
				sprite.position.x + 50 + 1):
			if col in range(sprite.position.y - 50, 
					sprite.position.y + 50 + 1):
				return True
		return False

	def get_kat_on_pos(self, x, y):
		for player in self.players:
			if self.__check_sprite_in_cell(player, x, y):
				return player

	def get_bird_on_pos(self, x, y):
		for enemy in self.enemies:
			if self.__check_sprite_in_cell(enemy, x, y):
				return enemy

	def clear(self):
		# game end
		self.enemies = []
		self.players = []
		