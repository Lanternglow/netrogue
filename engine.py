import sys
import os
import pygame
from unit import *
from mapwindow import *

pygame.init()

tilesize = 16
size = width, height = 800, 600
black = 0,0,0
screen = pygame.display.set_mode(size)
mapview = MapWindow((500, 500), tilesize)
mapLocation = mapview.get_rect().move([20, 20])

units = set()

me = Unit(tilesize, os.path.join('images', 'units', 'gtk3-demo.png'))
units.add(me)

panning = {
pygame.K_UP: [0,-1],
pygame.K_DOWN: [0,1],
pygame.K_LEFT: [-1,0],
pygame.K_RIGHT: [1,0]
}

movements = {
pygame.K_KP1: [-1, 1],
pygame.K_KP2: [0,1],
pygame.K_KP3: [1, 1],
pygame.K_KP4: [-1,0],
pygame.K_KP6: [1,0],
pygame.K_KP7: [-1, -1],
pygame.K_KP8: [0,-1],
pygame.K_KP9: [1, -1]
}

active = 1
while active:
	screen.fill(black)
	mapview.render(None, units, screen, mapLocation)
	pygame.display.flip()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			active = 0
			break
		if event.type == pygame.KEYDOWN:
			inkey = event.key
			if inkey in movements:
				movement = movements[inkey]
				me.move(movement)
			if inkey in panning:
				pan = panning[inkey]
				mapview.pan(pan)
	
	pygame.time.wait(30)

sys.exit()
