# -*- coding: utf-8 -*-

import sys
import os

from networking.server import Server


def printMessage(message):
    print(message)


numClients = 0
while not (1 < numClients < 7):
    clientEntry = input('Enter the number of clients: ')
    numClients = int(clientEntry)

with Server(22345) as server:
    for slot in range(1, numClients + 1):
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
