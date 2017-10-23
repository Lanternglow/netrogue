import sys
import os
sys.path.append(os.path.abspath('..'))

from commandProcessing.commandprocessor import CommandProcessor
from units.unit import Unit
from units.unitcollection import UnitCollection

from commandProcessing.commands.move import Move

units = UnitCollection()
tilesize = 60

me = Unit(tilesize, os.path.join('..', 'images', 'units', 'fighter.png'))
units.addUnit(me, (1, 1))

enemy = Unit(tilesize, os.path.join('..', 'images', 'units', 'skeleton.png'))
units.addUnit(enemy, (4, 3))

commandProcessor = CommandProcessor(units)

print('before movement')
print(units.positionsUnit)

moveCommand = Move(me, (1, 1))
updateCommand = commandProcessor.processCommand(moveCommand)

print('update command')
print(updateCommand)

print('after movement')
print(units.positionsUnit)
