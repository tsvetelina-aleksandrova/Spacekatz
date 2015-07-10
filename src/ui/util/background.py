import pygame
from random import randrange, choice

class StarField:
  def __init__(self, screen, stars_num):
    self.screen = screen
    self.stars = []
    # create the starfield
    for i in range(stars_num):
        # A star is represented as a list with this format: [X,Y,speed]
        star = [randrange(0, self.screen.get_width() - 1),
              randrange(0, self.screen.get_height() - 1),
              choice([1,2,3])]
        self.stars.append(star)
   
  def redraw_stars(self):
    # move and draw the stars in the given screen
    for star in self.stars:
        star[1] += star[2]
        # If the star hit the bottom border then we reposition
        # it in the top of the screen with a random X coordinate.
        if star[1] >= self.screen.get_height():
            star[1] = 0
            star[0] = randrange(0, 639)
            star[2] = choice([1, 2, 3])

      # Adjust the star color acording to the speed.
      # The slower the star, the darker should be its color.
        if star[2] == 1:
            color = (0, 245, 255)
        elif star[2] == 2:
            color = (0, 127, 255)
        elif star[2] == 3:
            color = (171, 130, 255)

        # Draw the star as a rectangle.
        # The star size is proportional to its speed.
        self.screen.fill(color, (star[0], star[1], star[2], star[2]))
