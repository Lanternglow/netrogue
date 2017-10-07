import sys
import os
import pygame
from unit import *
from mapwindow import *
from inputhandler import *

class Engine:
	
	def __init__(self, screen, mapview):
		pygame.init()
		self.requestQuit = False
		
		self.background = 0, 0, 0
		
		self.screen = screen
		self.mapview = mapview
		self.maplocation = self.mapview.get_rect().move([20, 20])
		self.units = set()
		self.inputHandler = InputHandler(self, self.mapview)
	
	def runFrame(self):
		self.screen.fill(self.background)
		self.mapview.render(None, self.units, self.screen, self.maplocation)
		pygame.display.flip()
	
	def addUnit(self, unit):
		self.units.add(unit)
	
	def quit(self):
		self.requestQuit = True

# ---- End Engine class ---- #
tilesize = 16
screen = pygame.display.set_mode((800, 600))
mapview = MapWindow((500, 500), tilesize)
engine = Engine(screen, mapview)

me = Unit(tilesize, os.path.join('images', 'units', 'gtk3-demo.png'))
engine.addUnit(me)
inputHandler = InputHandler(engine, mapview)
inputHandler.linkUnit(me)

while engine.requestQuit != True:
	engine.runFrame()
	inputHandler.handleInput()
	pygame.time.wait(60)

sys.exit()
