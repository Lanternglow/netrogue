import sys
import os
from unit import *
import socket

class Server:
	
	def __init__(self, port):
		self.netsocket = socket.socket()
		hostname = socket.gethostname()
		self.netsocket.bind(hostname, port)
	
	