import sys
import os
import pygame
from unit import *

pygame.init()

size = width, height = 800, 600
black = 0,0,0
screen = pygame.display.set_mode(size)

players = set()
enemies = set()

tilesize = 16
me = Unit(tilesize, os.path.join('images', 'units', 'gtk3-demo.png'))
players.add(me)

movements = {
pygame.K_UP: [0,-1],
pygame.K_DOWN: [0,1],
pygame.K_LEFT: [-1,0],
pygame.K_RIGHT: [1,0]}

active = 1
while active:
	screen.fill(black)
	for p in players:
		p.drawOn(screen)
	for e in enemies:
		e.drawOn(screen)
	pygame.display.flip()
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			active = 0
			break
		if event.type == pygame.KEYDOWN:
			inkey = event.key
			if inkey in movements:
				movement = movements[inkey]
				me.move(movement[0], movement[1])
	
	pygame.time.wait(30)

sys.exit()
