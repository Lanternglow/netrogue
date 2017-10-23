from .command import Command

class Move(Command):

	def __init__(self, unit, movement):
		super().__init__((unit, movement))
	
