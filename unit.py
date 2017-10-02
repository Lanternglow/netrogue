import sys, pygame

class Unit:
	"""A moveable unit on the map
	"""
	
	def __init__(self, tilesize, defaultImage):
		self.imageDefault = defaultImage
		self.tilesize = tilesize
		self.image = pygame.image.load(defaultImage)
		self.location = [0, 0]
		
	def setPos(self, x, y):
		self.location = [x, y]
	
	def move(self, dx, dy):
		self.location[0] += dx
		self.location[1] += dy
	
	def drawOn(self, screen):
		pos = [self.location[0] * self.tilesize, self.location[1] * self.tilesize]
		screen.blit(self.image, pos)
