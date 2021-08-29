from pygame.draw import rect
from pygame import Rect
# from .direction import Direction, KeyMap
from .direction import key2Vec
from .constants import bheight, bwidth, size

from random import choice

class Snake():
	color = (233, 90, 114)
	def __init__(self, body):
		self.body = list()
		self.body.append(body)
		self.len = 3
		self.dir = choice(list(key2Vec.values()))

	
	@property
	def head(self):
		return self.body[0]

	def turn(self, direc):
		vec = key2Vec.get(direc, -self.dir)
		if vec != -self.dir:
			self.dir = vec

	def update(self) -> bool:
		head = self.body[0] + self.dir
		if head.x >= bwidth or head.x < 0:
			head.x %= bwidth
		
		if head.y >= bheight or head.y < 0:
			head.y %= bheight
		
		if head in self.body:
			return False
		
		self.body.insert(0, head)

		if (len(self.body) > self.len):
			self.body.pop()
		
		return True
	
	def draw(self, win):
		for block in self.body:
			rect(win, self.color, Rect(size * block.x, size * block.y, size, size))

	def eat(self):
		self.len += 1