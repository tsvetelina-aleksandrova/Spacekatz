import pygame
from pygame.sprite import Sprite
from backend.sprites.bullet import Bullet
from backend.util.coords import Coords
from ui.util.helpers import Helpers


class BulletUI(Sprite):
	def __init__(self, screen, start_pos, board, strength, from_player):
		Sprite.__init__(self)
		self.pos = (start_pos.x, start_pos.y)
		if from_player:
			self.move_y = -10
			self.image = Helpers.get_image('/img/kat_bullet.png')
		else:
			self.move_y = 10
			self.image = Helpers.get_image('/img/bird_bullet.png')
		self.bullet = Bullet(start_pos, strength, board, from_player)
		self.rect = self.image.get_rect()
		self.rect.center = self.pos
		self.screen = screen

	def update(self, seconds):
		# self.bullet.move(0, -10)
		self.pos = (self.pos[0], self.pos[1] + self.move_y)
		old_rect_x = self.rect.center[0]
		old_rect_y = self.rect.center[1]
		self.rect.center = (old_rect_x, old_rect_y + self.move_y)


