import socket
from queue import Queue
import turtle
from turtle import Turtle
from threading import Thread, current_thread
from port import PORT

serverSocket = None
cmd_queue = Queue()

class Move:
    def __init__(self, parts):
        self.name = parts[0]
        self.x = int(parts[1])
        self.y = int(parts[2])
        self.color = parts[3]

turtles = {}  # Client name -> turtle

def handle_client(client_socket, address):
    print('handle_client on ' + current_thread().name)
    client_socket.send("Hi there\n".encode())
    while True:
        line = client_socket.recv(1024).decode()
        parts = line.split('\t')
        if len(parts) == 4:
            cmd_queue.put(Move(parts))
            print(address, line)
            client_socket.send('Thanks for that\n'.encode())


def listen_thread():
    global serverSocket
    print('listen_thread on ' + current_thread().name)
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind(('', PORT))
    serverSocket.listen(100)

    while True:
        print('Game server waiting for connection')
        (client_socket, address) = serverSocket.accept()
        print('How exciting! A connection from', address)
        Thread(target=handle_client, args=(client_socket, address)).start()

Thread(target=listen_thread).start()

turtle_shapes = ('arrow', 'circle', 'square', 'triangle', 'classic', 'turtle')


def add_turtle(name):
    t = Turtle()
    t.speed('fast')
    #t.penup()
    t.shape(turtle_shapes[len(turtles) % len(turtle_shapes)])
    turtles[name] = t
    t.setheading(90)  # Point up
    return t

try:
    turtle.setup(650, 650)
    turtle.hideturtle()
    for n in range(100000):
        cmd = cmd_queue.get()
        client_turtle = turtles.get(cmd.name) or add_turtle(cmd.name)
        if n % 50 == 0:  # Clear all turtles periodically
            for turtle in turtles.values():
                turtle.clear()
        client_turtle.pencolor(cmd.color)
        client_turtle.goto(cmd.x, cmd.y)
except KeyboardInterrupt:
    print('Stopping server')
    serverSocket.close()
