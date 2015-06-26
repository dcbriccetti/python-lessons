# Dave's Exciting Text Adventure Game, Version 4

# Dedicated to my students Ethan, Eric, Chris, Kurt, and Sam.
# May they turn it into something that someone might actually
# want to play. :-)

from place import Place
from gamexml import GameXml
from commandline import CommandLine
from tkinter import *
import socket

class GameUI(Frame):

    def showDirections(self):
        self.messages.set('''
Welcome to Dave's Exciting Text Adventure Game, now with XML.
(The X is for eXtra fun!!!)

Commands:
    go "place"
    get "object"
    quit
''')
    
    def getItemsDescription(self):
        result = ""
        if self.collectedItems:
            result += 'You have collected these items:\n'
            for item in self.collectedItems:
                result += "\t" + item + '\n'
        return result

    def endGame(self):
        if self.serverConn:
            self.serverConn.close()
        self.quit()
        
    def updateScene(self):
        self.sceneDescription.set(self.place.getLongDescription() +
            '\n' + self.getItemsDescription())

    def alertServer(self, msg):
        if self.serverConn:
            self.serverConn.send(msg)
        
    def execute(self):
        self.commandLine.set(self.command.get())

        # "Go" command
        if self.commandLine.cmd == 'go':
            newPlace = self.commandLine.args
            if newPlace in self.place.connections:
                # The requested place is valid. "Move" to it.
                self.place = self.places[newPlace]
                self.messages.set('')
                self.updateScene()
                self.alertServer('Arrived: ' + newPlace)
            else:
                self.messages.set('There\'s no place called "%s," now, is there?' %
                                  newPlace)
                
        # "Get" command
        elif self.commandLine.cmd == 'get':
            requestedItem = self.commandLine.args
            if requestedItem in self.place.objects:
                self.messages.set('You got the ' + requestedItem)
                self.collectedItems.append(requestedItem)
                self.place.deleteObject(requestedItem)
                self.updateScene()
                self.alertServer('Got: ' + requestedItem)
            else:
                self.messages.set('There\'s no object called "%s," and everyone knows it.' %
                                  requestedItem)

        else:
            self.messages.set('Why would you type something like, "%s"?' % (rawLine))
    
    def createWidgets(self):
        self.messages = StringVar()
        self.messagesLabel = Label(self,
            textvariable = self.messages,
            justify = 'left', wraplength = 400)
        self.messagesLabel.grid(row = 1, column = 1, columnspan = 2,
            padx = 0, pady = 0)

        self.sceneDescription = StringVar()
        self.sceneDescriptionLabel = Label(self,
            textvariable = self.sceneDescription,
            justify = 'left', wraplength = 400)
        self.sceneDescriptionLabel.grid(row = 2, column = 1, columnspan = 2,
            padx = 10, pady = 10)
        
        self.command = StringVar()
        self.commandEntry = Entry(self, textvariable = self.command)
        self.commandEntry.grid(row = 3, column = 1, columnspan = 2,
            padx = 10, pady = 10)
        
        self.executeButton = Button(self, text = 'Execute',
            command = self.execute)
        self.executeButton.grid(row = 4, column = 1, padx = 5, pady = 5)

        self.quitButton = Button(self, text = 'Quit', command = self.endGame)
        self.quitButton.grid(row = 4, column = 2, padx = 5, pady = 5)

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.createWidgets()

        # Load all the places from the XML file into the places hash
        self.places = {}
        gameXml = GameXml("game.xml", self.places)

        # Set the starting place, from an attribute in the XML file
        self.place = self.places[gameXml.startingPlace]

        # Set the initial description
        self.sceneDescription.set(self.place.getLongDescription())
        
        # Keep our collected items in a list
        self.collectedItems = []

        # Create one of these to parse our command lines
        self.commandLine = CommandLine()

        self.showDirections()

        if gameXml.serverHost and gameXml.serverPort:
            try:
                self.serverConn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.serverConn.connect((gameXml.serverHost,
                    int(gameXml.serverPort)))
            except Exception:
                print("oh")

gameUI = GameUI()
gameUI.master.title("Dave's Exciting Text Adventure, Version 4")
gameUI.mainloop()
