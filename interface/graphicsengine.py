import sys
import os
import pygame

class GraphicsEngine:
	
	def __init__(self, screen, mapview, units):
		self.requestQuit = False
		
		self.background = 0, 0, 0
		
		self.screen = screen
		self.mapview = mapview
		self.maplocation = self.mapview.get_rect().move([20, 20])
		self.units = units
	
	def runFrame(self):
		self.screen.fill(self.background)
		self.mapview.render(None, self.units.unitsPosition, self.screen, self.maplocation)
		pygame.display.flip()
	
	def quit(self):
		self.requestQuit = True

# ---- End Engine class ---- #

