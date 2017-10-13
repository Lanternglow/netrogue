import sys
import os
import socket
import threading

class Client:
	
	def __init__(self, port):
		self.port = port
	
	def __enter__(self):
		return self
	
	def __exit__(self, exc_type, exc_value, traceback):
		self.connection.shutdown(socket.SHUT_RDWR)
		self.connection.close()
		
	def connect(self, remoteHost):
		self.connection = socket.create_connection((remoteHost, self.port))
		
	def printSocket(self):
		data = self.connection.recv(32)
		datastring = data.decode('utf-8')
		print("read: {}".format(datastring))
	
	def sendData(self, data):
		databytes = bytes(data, 'utf-8')
		dataSent = 0
		datalen = len(databytes)
		while dataSent < datalen:
			dataToSend = data[dataSent:]
			self.connection.send(dataToSend)
	
# end class definition

if __name__ == "__main__":
	with Client(22345) as client:
		client.connect('localhost')
		client.printSocket()
	