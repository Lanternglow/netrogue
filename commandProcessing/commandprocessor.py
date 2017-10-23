from .update import Update

class CommandProcessor:

	def __init__(self, unitCollection):
		self.unitCollection = unitCollection
		self.commandTypes = {
			'Move': self.move
		}

	def processCommand(self, command):
		commandName = command.__class__.__name__
		commandArguments = command.getArguments()
		return self.commandTypes[commandName](*commandArguments)

	def move(self, sourceUnit, movement):
		updateCommand = Update()
		updateCommand.addUpdate('move', (sourceUnit, movement))
		
		self.unitCollection.applyUpdate(updateCommand)
		return updateCommand
	
