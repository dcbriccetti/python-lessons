import socket
import turtle
from turtle import Turtle
from threading import Thread, Event, current_thread
from port import PORT

serverSocket = None
move_event = Event()

class Move:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y

move_cmd = None
turtles = {
    'all': Turtle()
}  # Client name -> turtle

def handle_client(client_socket, address):
    global move_cmd
    print('handle_client on ' + current_thread().name)
    client_socket.send("Hi there\n".encode())
    while True:
        line = client_socket.recv(1024).decode()
        parts = line.split('\t')
        if len(parts) == 3:
            move_cmd = Move(parts[0], int(parts[1]), int(parts[2]))
            move_event.set()
            print(address, line)
            client_socket.send('Thanks for that\n'.encode())


def listen_thread():
    global serverSocket
    print('listen_thread on ' + current_thread().name)
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', PORT))
    serverSocket.listen(1)

    while True:
        print('Game server waiting for connection')
        (client_socket, address) = serverSocket.accept()
        print('How exciting! A connection from', address)
        Thread(target=handle_client, args=(client_socket, address)).start()

Thread(target=listen_thread).start()

try:
    turtle.setup(600, 600)
    turtle.ht()
    while True:
        move_event.wait()
        move_event.clear()
        turtles['all'].goto(move_cmd.x, move_cmd.y)
except KeyboardInterrupt:
    print('Stopping server')
    serverSocket.close()
