import pygame
from pygame.font import Font

class Helpers:
	@staticmethod
	def get_constants():
		return {
			"size": {
				"display_width": 400,
				"display_height": 600
			},
			"font": {
				"menu_font": Font(None, 50)
			},
			"color": {
				"white": (255, 255, 255),
				"black": (0, 0, 0)
			}
		}

	@staticmethod
	# returns the rect of the text object
	def display_message(screen, msg, x_center_delta=0, y_center_delta=0):
		const = Helpers.get_constants()
		center_x = (const["size"]["display_width"] / 2) + x_center_delta
		center_y = (const["size"]["display_height"] / 2) + y_center_delta
		msg_font =  Font(None, 50)

		screen_text = msg_font.render(msg, True, const["color"]["white"])
		text_rect = screen_text.get_rect()
		text_rect.center = (center_x, center_y)
		screen.blit(screen_text, text_rect)

		return text_rect