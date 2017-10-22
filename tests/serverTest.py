import sys
import os
sys.path.append(os.path.abspath('..'))

from networking.server import Server
if len(sys.argv) < 2:
	print('Need number of clients')
	sys.exit(1)
maxClients = int(sys.argv[1])

def printMessage(message):
	print(message)

with Server(22345) as server:
	for slot in range(1, maxClients + 1):
		server.registerListener(printMessage)
		server.acceptPlayer(slot)
		server.listenOn(slot)
		server.sendPlayerData(slot, "You are client {}".format(slot))
	
	while True:
		text = input()
		if text == 'q': break
		
		for slot in server.players.keys():
			server.sendPlayerData(slot, text)
print('closing down')
