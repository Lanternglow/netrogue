import sys, pygame

class Unit:
	"""A moveable unit on the map
	"""
	
	def __init__(self, tilesize, defaultImage):
		self.imageDefault = defaultImage
		self.tilesize = tilesize
		self.image = pygame.image.load(defaultImage)
		
	def getImage(self):
		return self.image
	