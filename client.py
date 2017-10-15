import sys
import os
import socket
import threading
import time

class Client:
	
	def __init__(self, port):
		self.port = port
	
	def __enter__(self):
		return self
	
	def __exit__(self, exc_type, exc_value, traceback):
		self.listening = False
		self.listenThread.join()
		#self.connection.shutdown(socket.SHUT_RDWR)
		self.connection.close()
		
	def connect(self, remoteHost):
		self.connection = socket.create_connection((remoteHost, self.port))
		
	def printSocket(self):
		self.listening = True
		while self.listening:
			data = self.connection.recv(32)
			if len(data) > 0:
				datastring = data.decode('utf-8')
				print("read: {}".format(datastring))
			time.sleep(0.1)
	
	def sendData(self, data):
		print("sending: {}".format(data))
		databytes = bytes(data, 'utf-8')
		dataSent = 0
		datalen = len(databytes)
		while dataSent < datalen:
			dataToSend = databytes[dataSent:]
			dataSent += self.connection.send(dataToSend)
	
	def listen(self):
		self.listenThread = threading.Thread(target=self.printSocket)
		self.listenThread.start()
	
	def endListen(self):
		self.listening = False
	
# end class definition

if __name__ == "__main__":
	print(sys.argv)
	if len(sys.argv) < 2:
		print('Need to give a computer to connect to')
		sys.exit(1)
	host = sys.argv[1]
	
	with Client(22345) as client:
		client.connect(host)
		client.listen()
		
		unread = True
		while unread or text != 'q':
			unread = False
			text = input()
			client.sendData(text)
	print('closing down')
	