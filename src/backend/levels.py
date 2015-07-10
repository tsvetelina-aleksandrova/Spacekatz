from backend.util.board import Board
from backend.sprites.bird_move_strategies import *
from backend.sprites.bird_init_pos import *
from ui.sprites.bird_ui import BirdUI


class Level:
	def __init__(self, board, lvl):
		if lvl < 0:
			lvl = 0
		if lvl > 5:
			lvl = 5
		self.lvl = lvl

		self.board = board
		self.is_paused = False

	def start(self, screen=None, bullet_group=None, bird_group=None):
		diag_dirs = [
			DiagonalStrategy.directions[2],
			DiagonalStrategy.directions[1]
		]
		self.enemy_strategies = [
			InPlaceStrategy(),
			DiagonalStrategy(diag_dirs[0]),
			DiagonalStrategy(diag_dirs[1]),
			BlockStrategy(),
			BossStrategy()
		]
		self.enemy_nums = [30, 20, 20, 30, 1]
		self.enemy_init_pos = [
			SingleBlockInitPos(),
			DiagInitPos(20, diag_dirs[0]),
			DiagInitPos(20, diag_dirs[1]),
			BlockInitPos(),
			SingleInitPos()
		]

		self.enemies = []
		print("here")
		self.strategy = self.enemy_strategies[self.lvl]
		for i in range(self.enemy_nums[self.lvl]):
			new_bird = BirdUI(screen, next(self.enemy_init_pos[self.lvl]), 
				self.enemy_strategies[self.lvl], self.board, bullet_group)
			self.enemies.append(new_bird)
			new_bird.add(bird_group)
			print(new_bird.pos)
		print("Level", self.lvl, "started")
		# self.play()
		
	def play(self):
		while not self.is_paused:
			for enemy in self.enemies:
				enemy.shoot()
				enemy.move()

	def pause(self):
		self.is_paused = True