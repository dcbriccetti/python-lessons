from random import randint
from time import sleep
from socket import socket, AF_INET, SOCK_STREAM
from port import PORT

socket = socket(AF_INET, SOCK_STREAM)
socket.connect(('127.0.0.1', PORT))


def rc():
    return randint(-300, 300)

try:
    for n in range(100):
        socket.send(('Dave\t%i\t%i\tblue' % (rc(), rc())).encode())
        sleep(2)
except KeyboardInterrupt:
    pass

socket.close()
