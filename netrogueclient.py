import sys
import os

from networking.client import Client


def printServerData(message):
	print(message)


host = input('Enter server to connect to')

with Client(22345) as client:
	client.registerListener(printServerData)
	client.connect(host)
	client.startListen()

	while True:
		text = input()
		if text == 'q': break

		client.sendData(text)

print('closing down')
