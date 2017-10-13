import sys
import os
import pygame
from unit import *
from unitcollection import *
from mapwindow import *
from inputhandler import *

class GraphicsEngine:
	
	def __init__(self, screen, mapview, units):
		pygame.init()
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

tilesize = 60
screen = pygame.display.set_mode((800, 600))
mapview = MapWindow((500, 500), tilesize)
units = UnitCollection()
engine = GraphicsEngine(screen, mapview, units)

me = Unit(tilesize, os.path.join('images', 'units', 'fighter.png'))
units.addUnit(me, (1, 1))
inputHandler = InputHandler(engine, mapview, units)
inputHandler.linkUnit(me)

enemy = Unit(tilesize, os.path.join('images', 'units', 'skeleton.png'))
units.addUnit(enemy, (4, 3))

while engine.requestQuit != True:
	engine.runFrame()
	inputHandler.handleInput()
	pygame.time.wait(60)

sys.exit()
