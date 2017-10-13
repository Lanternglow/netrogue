import sys
import os
from unit import *
from unitcollection import *

class DataEngine:
	
	def __init__(self):
		self.requestQuit = False
		self.units = UnitCollection()
	
	def moveValid(self, unit, movement):
		newPosition = self.units.positionAfterMovement(unit, movement)
		unitCollision = newPosition in self.units.positionsUnit
		return !unitCollision
	
	