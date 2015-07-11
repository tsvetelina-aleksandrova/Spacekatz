import pygame
from pygame.sprite import Sprite
from backend.sprites.bird import Bird
from backend.util.coords import Coords
from ui.util.helpers import Helpers
from ui.sprites.bullet_ui import BulletUI


class BirdUI(Sprite):
	def __init__(self, screen, bird, bullet_group):
		Sprite.__init__(self)
		self.bird = bird
		self.pos = (bird.position.x, bird.position.y)  
		self.screen = screen
		self.bullet_group = bullet_group
		self.image = Helpers.get_image('/img/bird.png')
		self.rect = self.image.get_rect()

	def update(self, seconds):
		# add collision checks
		#
		self.bird.move()
		# bird's position has changed
		self.rect.center = (self.bird.position.x, self.bird.position.y)
		# shoot sometimes
		bullet = self.bird.shoot()
		if bullet is not None:
			new_bullet_ui = BulletUI(self.screen, bullet)
			self.bullet_group.add(new_bullet_ui)
