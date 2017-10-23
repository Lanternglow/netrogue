
class Update:
	
	def __init__(self):
		self.updates = []
	
	def addUpdate(self, command, arguments):
		self.updates.append((command, arguments))
	