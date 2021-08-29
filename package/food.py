from .vector import Vector
from .constants import bwidth, bheight, size

from random import randint
from pygame.draw import rect
from pygame import Rect

class Food(Vector):
	color = (171,219,227)

	def __init__(self):
		super().__init__(randint(0, bwidth - 1), randint(0, bheight - 1))
	
	def draw(self, win):
		rect(win, self.color, Rect(size * self.x, size * self.y, size, size))