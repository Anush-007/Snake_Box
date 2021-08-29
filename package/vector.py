class Vector :
	def __init__(self, x, y):
		self.__tup = [x, y]

	@property
	def x(self) :
		return self.__tup[0]
	
	@property
	def y(self) :
		return self.__tup[1]
	

	@x.setter
	def x(self, x):
		self.__tup[0] = x

	@y.setter
	def y(self, y):
		self.__tup[1] = y

	def __add__(self, other) :
		return Vector(self.x + other.x, self.y + other.y)
	
	def __iadd__(self, other) :
		self.x += other.x
		self.y += other.y
		return self
	
	def __neg__(self):
		return Vector(-self.x, -self.y)
	
	def __eq__(self, other):
		return self.x == other.x and self.y == other.y
	
	def __ne__(self, other):
		return self.x != other.x or self.y != other.y

