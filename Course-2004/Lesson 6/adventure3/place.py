from textwrap import wrap

class Place:
    
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.objects = {}
        self.connections = {}

    def addObject(self, objectName):
        self.objects[objectName] = 1

    def deleteObject(self, objectName):
        del self.objects[objectName]

    def addConnection(self, connectionName):
        self.connections[connectionName] = 1

    def show(self):
        print()
        descLines = wrap(self.description)
        for descLine in descLines:
            print(descLine)
            
        print()
        self.showObjects()

        print()
        self.showConnections()

    def showObjects(self):
        if self.objects:
            print('These objects are here:')
            for object in self.objects:
                print("\t", object)

    def showConnections(self):
        if self.connections:
            print('From here you can go to: ')
            for connection in self.connections:
                print("\t", connection)

