import socket

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind(('', 5000))
serverSocket.listen(1)

while True:
    print('Game server waiting for connection')
    
    (clientSocket, clientAddr) = serverSocket.accept()
    print('How exciting! A connection from', clientAddr)
    clientSocket.send("Hi there\n".encode())

    while True:
        line = clientSocket.recv(100).decode().strip()
        if not line:
            break
        print(clientAddr, line)

    print('Bye bye,', clientAddr)
    clientSocket.close()

serverSocket.close()
