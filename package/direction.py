# from enum import Enum
from .vector import Vector
from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN


# class KeyMap(Enum):
# 	left = K_LEFT
# 	right = K_RIGHT
# 	up = K_UP
# 	down = K_DOWN



# class Direction(Enum):
# 	left = Vector(-1, 0)
# 	right = Vector(1, 0)
# 	up = Vector(0, -1)
# 	down = Vector(0, 1)

# 	def __neg__(self):
# 		return Direction(-self.value)


key2Vec = {
	K_LEFT : Vector(-1, 0),
	K_RIGHT : Vector(1, 0),
	K_UP : Vector(0, -1),
	K_DOWN : Vector(0, 1)
}
