import pygame
from pygame.sprite import Sprite

class Bird(Sprite):
	def __init__(self, start_pos):
	pygame.sprite.Sprite.__init__(self, self.groups)
	self.pos = start_pos 
	self.image = kat_img = Helpers.get_image('/img/bird.png')   