import sys
import os
sys.path.append(os.path.abspath('..'))

import pygame

from units.unit import Unit
from units.unitcollection import UnitCollection
from interface.inputhandler import InputHandler
from interface.mapwindow import MapWindow
from interface.graphicsengine import GraphicsEngine

pygame.init()

tilesize = 60
screen = pygame.display.set_mode((800, 600))
mapview = MapWindow((500, 500), tilesize)
units = UnitCollection()
engine = GraphicsEngine(screen, mapview, units)

me = Unit(tilesize, os.path.join('..', 'images', 'units', 'fighter.png'))
units.addUnit(me, (1, 1))
inputHandler = InputHandler(engine, mapview, units)
inputHandler.linkUnit(me)

enemy = Unit(tilesize, os.path.join('..', 'images', 'units', 'skeleton.png'))
units.addUnit(enemy, (4, 3))

while engine.requestQuit != True:
	engine.runFrame()
	inputHandler.handleInput()
	pygame.time.wait(60)

sys.exit()
