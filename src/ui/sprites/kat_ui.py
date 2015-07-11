import pygame
import pygame.event
from pygame.sprite import Sprite
from backend.sprites.kat import Kat
from backend.util.coords import Coords
from ui.util.helpers import Helpers
from ui.sprites.bullet_ui import BulletUI


class KatUI(Sprite):
	def __init__(self, screen, kat, bullet_group):
		Sprite.__init__(self)
		self.kat = kat
		self.screen = screen
		self.bullet_group = bullet_group
		self.pos = (kat.position.x, kat.position.y) 
		self.image = Helpers.get_image('/img/kat.png')
		self.rect = self.image.get_rect()

	def handle_event(self, event):
		kat_moves_data = [
			[pygame.K_UP, [0, -10]],
			[pygame.K_DOWN, [0, 10]],
			[pygame.K_RIGHT, [10, 0]],
			[pygame.K_LEFT, [-10, 0]]
		]
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				bullet = self.kat.shoot()
				new_bullet_ui = BulletUI(self.screen, bullet)
				self.bullet_group.add(new_bullet_ui)
				return
			for move_data in kat_moves_data:
				if event.key == move_data[0]:
					move_value = move_data[1]
					self.kat.move(move_value[0], move_value[1])
					self.rect.center = (self.kat.position.x, 
						self.kat.position.y)
