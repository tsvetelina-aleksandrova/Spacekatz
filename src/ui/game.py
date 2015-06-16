import pygame
from sources.util.starfield import StarField

def play():
	pygame.init()
	display_width = 600
	display_height = 800
	screen = pygame.display.set_mode((display_width, display_height))
	pygame.display.set_caption("Spacekatz")
	
	clock = pygame.time.Clock()
	star_field = StarField(screen, 250)
	game_exit = False

	while not game_exit:
		clock.tick(60)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True
		screen.fill((0,0,0))
		star_field.redraw_stars()
		pygame.display.update()