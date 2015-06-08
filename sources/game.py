import pygame
from sources.backgr import StarField

def play():
	pygame.init()
	screen = pygame.display.set_mode((640,480))
	pygame.display.set_caption("Parallax Starfield Simulation")
	clock = pygame.time.Clock()

	star_field = StarField(screen, 250)

	while True:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		screen.fill((0,0,0))
		star_field.redraw_stars()
		pygame.display.flip()