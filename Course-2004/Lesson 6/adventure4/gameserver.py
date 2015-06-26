import socket
from gamexml import GameXml 

places = {}
gameXml = GameXml("game.xml", places)

servSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servSock.bind(('', int(gameXml.serverPort)))
servSock.listen(1)

while 1:
    print('Game server waiting for connection')
    
    (clientSock, clientAddr) = servSock.accept()
    print('How exciting! A connection from', clientAddr)

    while 1:
        data = clientSock.recv(100)
        if not data:
            break
        print(clientAddr, data)

    print('Bye bye,', clientAddr)
    clientSock.close()

servSock.close()
