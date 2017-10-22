import sys
import os
import socket
import threading
import time

from .exceptions import ListenerException

class Server:
	
	def __init__(self, port):
		self.netsocket = socket.socket()
		self.port = port
		self.netsocket.bind(('', self.port))
		self.players = {}
		self.listening = {}
		self.listenThreads = {}
	
	def __enter__(self):
		return self
	
	def __exit__(self, exc_type, exc_value, traceback):
		for slot, connection in self.players.items():
			self.endListen(slot)
			self.listenThreads[slot].join()
			#connection.shutdown(socket.SHUT_RDWR)
			connection.close()
		#self.netsocket.shutdown(socket.SHUT_RDWR)
		self.netsocket.close()
	
	def acceptPlayer(self, slotNum):
		if slotNum in self.players: raise Exception('player slot already taken')
		self.netsocket.listen(1)
		connection, address = self.netsocket.accept()
		connection.setblocking(False)
		self.players[slotNum] = connection
	
	def sendPlayerData(self, slot, data):
		#print("sending to player {}: {}".format(slot, data))
		databytes = bytes(data, 'utf-8')
		connection = self.players[slot]
		bytesSent = 0
		datalen = len(databytes)
		while bytesSent < datalen:
			dataToSend = databytes[bytesSent:]
			bytesSent += connection.send(dataToSend)
	
	def registerListener(self, callback):
		self.notify = callback
		self.listenerRegistered = True
	
	def notifyListener(self, slot):
		if not self.listenerRegistered: raise ListenerException('No listener registered')
		self.listening[slot] = True
		connection = self.players[slot]
		while self.listening[slot]:
			try:
				data = connection.recv(32)
				if len(data) > 0:
					datastring = data.decode('utf-8')
					self.notify(datastring)
			except BlockingIOError:
				pass
			time.sleep(0.1)
	
	def listenOn(self, slot):
		self.listenThreads[slot] = threading.Thread(target = self.notifyListener, args = (slot,))
		self.listenThreads[slot].start()
	
	def endListen(self, slot):
		self.listening[slot] = False
	
# end class definition
