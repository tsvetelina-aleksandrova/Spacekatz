import pygame
import os
from pygame.font import Font

class Helpers:
	const = {
			"size": {
				"display_width": 400,
				"display_height": 600
			},
			"font": {
				#"menu_font": Font(None, 50)
			},
			"color": {
				"white": (255, 255, 255),
				"black": (0, 0, 0)
			}
		}

	_image_library = {}

	@staticmethod
	# returns the rect of the text object
	def display_message(screen, msg, x_center_delta=0, y_center_delta=0):
		center_x = (Helpers.const["size"]["display_width"] / 2) + x_center_delta
		center_y = (Helpers.const["size"]["display_height"] / 2) + y_center_delta
		msg_font =  Font(None, 30)

		screen_text = msg_font.render(msg, True, Helpers.const["color"]["white"])
		text_rect = screen_text.get_rect()
		text_rect.center = (center_x, center_y)
		
		screen.blit(screen_text, text_rect)
		pygame.display.update(text_rect)
		return text_rect

	@staticmethod
	def ask(screen, question, init_input="", x_center_delta=0, y_center_delta=0):
		answer = list(init_input)
		Helpers.display_message(screen, question + ": " + "".join(answer), 
			x_center_delta, y_center_delta)
		for event in pygame.event.get():
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_BACKSPACE:
				  	answer = answer[0:-1]
				elif event.key == pygame.K_RETURN:
				  	break
				elif event.key == pygame.K_MINUS:
				  	answer.append("_")
				elif event.key <= 127:
				  	answer.append(chr(event.key))
		Helpers.display_message(screen, question + ": " + "".join(answer),
			x_center_delta, y_center_delta)
		return "".join(answer)

	@staticmethod
	def get_mouse_click_pos():
		mouse_pos = 0
		if pygame.mouse.get_pressed()[0] == 1:
			mouse_pos = pygame.mouse.get_pos()
		return mouse_pos

	@staticmethod
	def get_image(path):
		image = Helpers._image_library.get(path)
		if image == None:
			sub_path = path.replace('/', os.sep).replace('\\', os.sep)
			canonicalized_path = os.getcwd() + sub_path
			print(canonicalized_path)
			image = pygame.image.load(canonicalized_path).convert()
			Helpers._image_library[path] = image
		return image
		