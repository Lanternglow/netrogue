import sys
import os
sys.path.append(os.path.abspath('..'))

from networking.client import Client

if len(sys.argv) < 2:
	print('Need to give a computer to connect to')
	sys.exit(1)
host = sys.argv[1]

def printServerData(message):
	print(message)

with Client(22345) as client:
	client.registerListener(printServerData)
	client.connect(host)
	client.startListen()
	
	while True:
		text = input()
		if text == 'q': break
		
		client.sendData(text)
print('closing down')
