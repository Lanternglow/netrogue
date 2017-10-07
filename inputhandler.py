import pygame

class InputHandler:
	
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
	
	def __init__(self, engine, mapview):
		self.engine = engine
		self.mapview = mapview
	
	def linkUnit(self, unit):
		self.unit = unit
	
	def handleInput(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				self.engine.quit()
			if event.type == pygame.KEYDOWN:
				inkey = event.key
				if inkey in self.movements:
					movement = self.movements[inkey]
					self.unit.move(movement)
				if inkey in self.panning:
					pan = self.panning[inkey]
					self.mapview.pan(pan)