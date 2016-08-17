from threading import Thread, current_thread, local
from random import randint, random, choice
from time import sleep
from socket import socket, AF_INET, SOCK_STREAM
from port import PORT


def rc():
    return randint(-300, 300)


colors = ('red', 'blue', 'yellow', 'brown', 'green', 'gray', 'purple')


def draw(color):
    tl = local()
    tl.color = color
    tl.socket = socket(AF_INET, SOCK_STREAM)
    tl.socket.connect(('127.0.0.1', PORT))

    name = 'client%f' % random()
    try:
        for i in range(100):
            print('Socket file %i, %s sending' % (tl.socket.fileno(), current_thread().name))
            tl.socket.send(('%s\t%i\t%i\t%s' % (name, rc(), rc(), tl.color)).encode())
            sleep(0.5 + random())
    except KeyboardInterrupt:
        pass

    tl.socket.close()

for color in colors:
    Thread(target=draw, args=(color,)).start()
