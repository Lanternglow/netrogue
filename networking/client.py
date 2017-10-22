import sys
import os
import socket
import threading
import time

from .exceptions import ListenerException

class Client:
	
	def __init__(self, port):
		self.port = port
	
	def __enter__(self):
		return self
	
	def __exit__(self, exc_type, exc_value, traceback):
		self.endListen()
		#print('waiting for listener thread to end')
		self.listenThread.join()
		#print('shutting down socket connection')
		#self.connection.shutdown(socket.SHUT_RDWR)
		#print('closing socket')
		self.connection.close()
		#print('finished closing down')
		
	def connect(self, remoteHost):
		self.connection = socket.create_connection((remoteHost, self.port))
		self.connection.setblocking(False)
		
	def registerListener(self, callback):
		self.notify = callback
		self.listenerRegistered = True
	
	def listen(self):
		if not self.listenerRegistered: raise ListenerException('No listener registered')
		self.listening = True
		while self.listening:
			try:
				data = self.connection.recv(1024)
				if len(data) > 0:
					datastring = data.decode('utf-8')
					self.notify(datastring)
			except BlockingIOError:
				pass
			time.sleep(0.1)
		#print('closing')
		
	def sendData(self, data):
		#print("sending: {}".format(data))
		databytes = bytes(data, 'utf-8')
		dataSent = 0
		datalen = len(databytes)
		while dataSent < datalen:
			dataToSend = databytes[dataSent:]
			dataSent += self.connection.send(dataToSend)
	
	def startListen(self):
		self.listenThread = threading.Thread(target=self.listen)
		self.listenThread.start()
	
	def endListen(self):
		self.listening = False
	
# end class definition
