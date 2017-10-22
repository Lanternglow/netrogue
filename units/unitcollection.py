import sys
import os

from .unitExceptions import UnitException

class UnitCollection:
	
	def __init__(self):
		self.unitsPosition = dict() # unit => position
		self.positionsUnit = dict() # position => unit
		
	def addUnit(self, unit, position):
		if position in self.positionsUnit:
			raise UnitException('Cannot overwrite unit')
		if unit in self.unitsPosition:
			raise UnitException('Unit already exists')
		self.unitsPosition[unit] = position
		self.positionsUnit[position] = unit
	
	def positionAfterMovement(self, unit, movement):
		position = self.unitsPosition[unit]
		return (position[0] + movement[0], position[1] + movement[1])
	
	def moveUnit(self, unit, movement):
		position = self.unitsPosition[unit]
		newPosition = self.positionAfterMovement(unit, movement)
		if newPosition in self.positionsUnit:
			raise UnitException('Unit already at that location')
		self.unitsPosition[unit] = newPosition
		del self.positionsUnit[position]
		self.positionsUnit[newPosition] = unit
	
	def setUnitPosition(self, unit, position):
		oldPosition = self.unitsPosition[unit]
		if position in self.positionsUnit:
			raise UnitException('Unit already at that location')
		self.unitsPosition[unit] = position
		del self.positionsUnit[oldPosition]
		self.positionsUnit[position] = unit
	
# --- End class definition ---
