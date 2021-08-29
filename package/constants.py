def singleton(_cls):
	instances = {}
	def getinstance(*args, **kwargs):
		if _cls not in instances:
			instances[_cls] = _cls(*args, **kwargs)
		return instances[_cls]
	return getinstance

#screen
width = 1280
height = 720

title = "Snake Game"

# block
size = 20

# block map
bwidth = width / size
bheight = height / size

# Colors
screenfill = (0, 0, 0)

# game
fps = 60
