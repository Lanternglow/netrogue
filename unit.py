import sys, pygame

class Unit:
	"""A moveable unit on the map
	"""
	
	def __init__(self, tilesize, defaultImage):
		self.imageDefault = defaultImage
		self.tilesize = tilesize
		self.image = pygame.image.load(defaultImage)
		self.location = [0, 0]
		
	def setPos(self, position):
		self.location = position
	
	def move(self, movement):
		self.location[0] += movement[0]
		self.location[1] += movement[1]
	
	def getImage(self):
		return self.image
	