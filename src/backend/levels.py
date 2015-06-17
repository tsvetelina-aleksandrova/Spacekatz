class Level:
	def __init__(self, board, lvl):
		if lvl < 0:
			lvl = 0
		if lvl > 5:
			lvl = 5
		self.lvl = lvl
		self.enemy_strategies = [
			InPlaceStrategy(),
			DiagonalStrategy(DiagonalStrategy.get_available_directions()[2]),
			DiagonalStrategy(DiagonalStrategy.get_available_directions()[1]),
			BlockStrategy(),
			BossStrategy()
		]
		self.enemy_nums = [30, 20, 20, 30, 1]
		# iterators that provide init. positions for enemies
		# start from somewhere and move in to take a certain position ?
		self.enemy_init_pos = [
			InitPos(),
			InitPos(),
			InitPos(),
			InitPos(),
			InitPos()
		] 
		self.board = board
		self.is_paused = False

	def start(self):
		self.enemies = []
		self.strategy = self.enemy_strategies[lvl]
		for i in range(self.enemy_nums[self.lvl]):
			self.enemies.append(Bird(self.enemy_init_pos[i].get_position(), self.enemy_strategies[i]))
		self.play()
		
	def play(self):
		while not self.is_paused:
			for enemy in self.enemies:
				enemy.shoot()
				enemy.move()
				# if player is hit by bullet or enemy--> lower health / die
				# if enemy is shot--> remove enemy
			self.board.show(enemies)

	def pause(self):
		self.is_paused = True