import sys
import os
import pygame

from units.unit import Unit

class MapWindow:
	
	def __init__(self, dimensions, gridwidth):
		self.screen = pygame.Surface(dimensions)
		self.dimensions = dimensions
		self.gridwidth = gridwidth
		self.origin = [0, 0]
	
	def pan(self, delta):
		self.origin[0] += delta[0]
		self.origin[1] += delta[1]
	
	def prepareDraw(self, map):
		self.screen.fill((10, 10, 10))
		self.drawMap(map)
	
	def drawMap(self, map):
		pass
	
	def drawUnit(self, unit, location):
		x, y = location
		unitDimensions = unit.getImage().get_rect()
		spot = unitDimensions.move([ (x - self.origin[0]) * self.gridwidth, (y - self.origin[1]) * self.gridwidth ])
		self.screen.blit(unit.getImage(), spot)
	
	def drawDisplay(self, window, location):
		window.blit(self.screen, location)
	
	def get_rect(self):
		return self.screen.get_rect()
	
	def render(self, map, units, window, location):
		self.prepareDraw(map)
		for unit, position in units.items():
			self.drawUnit(unit, position)
		self.drawDisplay(window, location)
	