import sys
import os
from unit import *
import socket

class Server:
	
	def __init__(self, port):
		self.netsocket = socket.socket()
		self.hostname = socket.gethostname()
		self.port = port
		self.netsocket.bind((self.hostname, self.port))
		self.players = {}
	
	def __enter__(self):
		return self
	
	def __exit__(self, exc_type, exc_value, traceback):
		for connection in self.players.values():
			connection.shutdown(socket.SHUT_RDWR)
			connection.close()
		self.netsocket.shutdown(socket.SHUT_RDWR)
		self.netsocket.close()
	
	def acceptPlayer(self, slotNum):
		self.netsocket.listen(1)
		connection, address = self.netsocket.accept()
		if slotNum in self.players: raise Exception('player slot already taken')
		self.players[slotNum] = connection
		
	def sendPlayerSlot(self, slotNum):
		connection = self.players[slotNum]
		slotNumStr = "slot: {}".format(slotNum)
		self.sendPlayerData(slotNum, slotNumStr)
	
	def sendPlayerData(self, slot, data):
		databytes = bytes(data, 'utf-8')
		print("sending to player {}: {}".format(slot, databytes))
		connection = self.players[slot]
		bytesSent = 0
		datalen = len(databytes)
		while bytesSent < datalen:
			dataToSend = databytes[bytesSent:]
			bytesSent += connection.send(dataToSend)
	
# end class definition

if __name__ == "__main__":
	with Server(22345) as server:
		server.acceptPlayer(1)
		server.sendPlayerSlot(1)
		message = input("message: ")
		server.sendPlayerData(1, message)
	