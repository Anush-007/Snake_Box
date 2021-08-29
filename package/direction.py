from .vector import Vector
from pygame import K_LEFT, K_RIGHT, K_UP, K_DOWN


key2Vec = {
	K_LEFT : Vector(-1, 0),
	K_RIGHT : Vector(1, 0),
	K_UP : Vector(0, -1),
	K_DOWN : Vector(0, 1)
}
