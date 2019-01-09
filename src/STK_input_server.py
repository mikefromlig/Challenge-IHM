#!/usr/bin/env python3
#Michael ORTEGA - 09 jan 2018

###############################################################################
## Global libs
import sys
import socket
import keyboard

###############################################################################
## Global vars
GREEN       = '\033[92m'
WHITE       = '\x1b[0m'
BLUE        = '\033[94m'
YELLOW      = '\033[93m'
RED         = '\033[91m'

stop        = False
DEBUG       = False

address     = ('localhost', 6006)
sock        = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(address)


###############################################################################
## Main
if len(sys.argv) > 1:
    # Reading command line
    for i in range(1, len(sys.argv)):
        if sys.argv[i] == '-d':
            DEBUG = True

print()
print('STK input server started ', end='')
if DEBUG:
    print(GREEN+'(Debug mode)'+WHITE)
else:
    print()

commands    = [ 'UP', 'DOWN', 'LEFT', 'RIGHT', 'SELECT', 'CANCEL', 'BACK', 'ACCELERATE', 'BRAKE',
                'FIRE', 'NITRO', 'SKIDDING', 'LOOKBACK', 'RESCUE', 'PAUSE']
keys        = ['up', 'down', 'left', 'right', 'enter', 'backspace', 'backspace', 'up', 'down',
                'space', 'n', 'v', 'b', 'backspace', 'escape']

while (not stop):
    data, addr = sock.recvfrom(1024)
    if type(data) is bytes:
        data = data.decode("utf-8")

    if data == 'STOPSERVEUR':
        stop = True
    else:
        comm = data[1:]
        func = data[0]
        if comm in commands:
            if DEBUG: print(YELLOW+'\t'+data+WHITE)
            if func == 'p':
                keyboard.press(keys[commands.index(comm)])
            else:
                keyboard.release(keys[commands.index(comm)])
        else:
            if DEBUG: print(RED+'\t'+data+WHITE+' (Unknown)')

print('STK input server stopped')
