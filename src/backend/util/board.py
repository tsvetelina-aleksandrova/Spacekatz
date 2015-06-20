class Board:
	def __init__(self, width, height):
		self.matrix = [[0 for x in range(width)] for x in range(height)]
		self. width = width
		self.height = height

	def set_enemies(self, enemies):
		self.enemies = enemies
		self.sprites.extend(enemies)

	def set_players(self, players):
		self.players = players

	# should also care about size
	def refresh(self):
		self.enemies = [enemy for enemy in self.enemies if not enemy.is_dead]
		self.players = [player for player in self.players if not player.is_dead]

		for row in self.height:
			for col in self.width:
				matrix[row][col] = "."
				for enemy in self.enemies:
					if sprite.position.x == row and sprite.position.y == col:
						matrix[row][col] = "*"
				for player in self.players:
					if sprite.position.x == row and sprite.position.y == col:
						matrix[row][col] = "^"

	def get_kat_on_pos(self, x, y):
		for player in self.players:
			if player.position.x == x and player.position.y == y:
				return player

	def get_bird_on_pos(self, x, y):
		for enemy in self.enemies:
			if enemy.position.x == x and enemy.position.y == y:
				return enemy

	def clear(self):
		self.enemies = []
		self.players = []