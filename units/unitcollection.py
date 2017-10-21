import sys
import os
from exceptions import *

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

if __name__ == "__main__":
	from .unit import Unit
	
	unit1 = Unit(60, os.path.join('images', 'units', 'fighter.png'))
	unit2 = Unit(60, os.path.join('images', 'units', 'gtk3-demo.png'))
	unit3 = Unit(60, os.path.join('images', 'units', 'fighter.png'))
	
	units = UnitCollection()
	units.addUnit(unit1, (0, 3))
	units.addUnit(unit2, (2, 2))
	
	try: units.addUnit(unit1, (1, 5)); print('failed to fail')
	except: print('successfully failed')
	
	try: units.addUnit(unit3, (2, 2)); print('failed to fail')
	except: print('successfully failed')
	
	units.addUnit(unit3, (1, 2))
	
	try: units.moveUnit(unit3, (-1, 1)); print('failed to fail')
	except: print('successfully failed')
	
	try: units.setUnitPosition(unit2, (0, 3)); print('failed to fail')
	except: print('successfully failed')
