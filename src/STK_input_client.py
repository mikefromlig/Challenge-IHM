#!/usr/bin/env python3
#Michael ORTEGA - 09 jan 2018

###############################################################################
## Global libs
import socket
import sys
import select
from time import sleep

address = ('localhost', 6006)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sleep(3)
data = b'rLEFT'
client_socket.sendto(data, address)
sleep(3)
data = b'pLEFT'
client_socket.sendto(data, address)
sleep(3)
data = b'STOPSERVEUR'
client_socket.sendto(data, address)
