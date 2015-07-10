import pygame
import pygame.event
from pygame.sprite import Sprite
from backend.sprites.kat import Kat
from backend.util.coords import Coords
from ui.util.helpers import Helpers
from ui.sprites.bullet_ui import BulletUI


class KatUI(Sprite):
	def __init__(self, screen, start_pos, name, board, bullet_group):
		Sprite.__init__(self)
		self.kat = Kat(start_pos, name, board)
		self.pos = (start_pos.x, start_pos.y) 
		self.image = Helpers.get_image('/img/kat.png')
		self.rect = self.image.get_rect()
		self.screen = screen
		self.bullet_group = bullet_group

	def handle_event(self, event):
		kat_moves_data = [
			[pygame.K_UP, [0, -10]],
			[pygame.K_DOWN, [0, 10]],
			[pygame.K_RIGHT, [10, 0]],
			[pygame.K_LEFT, [-10, 0]]
			]
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_SPACE:
				self.kat.shoot()
				bullet_coords = Coords(self.rect.center[0],
					self.rect.center[1])
				new_bullet = BulletUI(self.screen, bullet_coords, 
					self.kat.board, self.kat.strength, True)
				self.bullet_group.add(new_bullet)
				return
			for move_data in kat_moves_data:
				if event.key == move_data[0]:
					move_value = move_data[1]
					self.kat.move(move_value[0], move_value[1])
					self.pos = (self.pos[0] + move_value[0], self.pos[1] + move_value[1])
					old_rect_x = self.rect.center[0]
					old_rect_y = self.rect.center[1]
					self.rect.center = (old_rect_x + move_value[0], old_rect_y + move_value[1])
