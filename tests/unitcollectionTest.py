import sys
import os
sys.path.append(os.path.abspath('..'))

from units.unitcollection import UnitCollection
from units.unit import Unit

unit1 = Unit(60, os.path.join('..', 'images', 'units', 'fighter.png'))
unit2 = Unit(60, os.path.join('..', 'images', 'units', 'gtk3-demo.png'))
unit3 = Unit(60, os.path.join('..', 'images', 'units', 'fighter.png'))

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
