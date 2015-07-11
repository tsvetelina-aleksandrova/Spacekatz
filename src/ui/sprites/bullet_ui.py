import pygame
from pygame.sprite import Sprite
from backend.sprites.bullet import Bullet
from backend.util.coords import Coords
from ui.util.helpers import Helpers


class BulletUI(Sprite):
	def __init__(self, screen, bullet):
		Sprite.__init__(self)
		self.screen = screen
		self.bullet = bullet
		self.pos = (bullet.position.x, bullet.position.y)
		if self.bullet.from_player:
			self.image = Helpers.get_image('/img/kat_bullet.png')
		else:
			self.image = Helpers.get_image('/img/bird_bullet.png')
		self.rect = self.image.get_rect()
		self.rect.center = self.pos

	def update(self, seconds):
		self.bullet.move()
		self.pos = (self.bullet.position.x, self.bullet.position.y)
		self.rect.center = self.pos
