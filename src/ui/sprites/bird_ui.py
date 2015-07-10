import pygame
from pygame.sprite import Sprite
from backend.sprites.bird import Bird
from backend.util.coords import Coords
from ui.util.helpers import Helpers
from ui.sprites.bullet_ui import BulletUI
from random import uniform


class BirdUI(Sprite):
	def __init__(self, screen, start_pos, move_strategy, board, bullet_group):
		Sprite.__init__(self)
		self.pos = (start_pos.x, start_pos.y)  
		self.image = Helpers.get_image('/img/bird.png')
		# self.bird = Bird(start_pos, strength, board)
		self.rect = self.image.get_rect()
		self.screen = screen
		self.bullet_group = bullet_group
		self.move_strategy = move_strategy
		self.board = board

	def update(self, seconds):
		# self.bird.move(0, -10)
		old_rect_x = self.rect.center[0]
		old_rect_y = self.rect.center[1]
		self.rect.center = (old_rect_x + self.move_strategy.get_delta_x(),
			old_rect_y + self.move_strategy.get_delta_y())
		if uniform(0, 10) > 9.9:
			bullet_coords = Coords(self.rect.center[0],
				self.rect.center[1])
			new_bullet = BulletUI(self.screen, bullet_coords, 
				self.board, 3, False)
			self.bullet_group.add(new_bullet)
