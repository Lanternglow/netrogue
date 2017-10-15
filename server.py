import sys
import os
from unit import *
import socket
import threading
import time

class Server:
	
	def __init__(self, port):
		self.netsocket = socket.socket()
		self.port = port
		self.netsocket.bind(('', self.port))
		self.players = {}
		self.listening = {}
	
	def __enter__(self):
		return self
	
	def __exit__(self, exc_type, exc_value, traceback):
		for connection in self.players.values():
			#connection.shutdown(socket.SHUT_RDWR)
			connection.close()
		#self.netsocket.shutdown(socket.SHUT_RDWR)
		self.netsocket.close()
	
	def acceptPlayer(self, slotNum):
		self.netsocket.listen(1)
		connection, address = self.netsocket.accept()
		if slotNum in self.players: raise Exception('player slot already taken')
		self.players[slotNum] = connection
		
	def sendPlayerData(self, slot, data):
		print("sending to player {}: {}".format(slot, data))
		databytes = bytes(data, 'utf-8')
		connection = self.players[slot]
		bytesSent = 0
		datalen = len(databytes)
		while bytesSent < datalen:
			dataToSend = databytes[bytesSent:]
			bytesSent += connection.send(dataToSend)
	
	def printSocket(self, slot):
		self.listening[slot] = True
		connection = self.players[slot]
		while self.listening[slot]:
			data = connection.recv(32)
			if len(data) > 0:
				datastring = data.decode('utf-8')
				print("read from {}: {}".format(slot, datastring))
			time.sleep(0.1)
	
	def listenOn(self, slot):
		self.listenThread = threading.Thread(target = self.printSocket, args = (slot,))
		self.listenThread.start()
	
	def endListen(self, slot):
		self.listening[slot] = False
	
# end class definition

if __name__ == "__main__":
	if len(sys.argv) < 2:
		print('Need number of clients')
		sys.exit(1)
	maxClients = sys.argv[1]
	
	with Server(22345) as server:
		for slot in range(1, maxClients + 1):
			server.acceptPlayer(slot)
			server.listenOn(slot)
			server.sendPlayerData("You are client {}".format(slot))
		
		unread = True
		while unread or text != 'q':
			unread = False
			text = input()
			for slot in server.players.keys():
				server.sendPlayerData(slot, text)
	print('closing down')
	