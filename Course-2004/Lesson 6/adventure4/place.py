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

    def getLongDescription(self):
        result = "\n" + self.description + "\n\n" + \
            self.getObjectsDescription() + \
            "\n" + self.getConnectionsDescription()
        return result

    def getObjectsDescription(self):
        result = ""
        if self.objects:
            result += 'These objects are here:\n'
            for object in self.objects:
                result += "\t" + object + "\n"
        return result

    def getConnectionsDescription(self):
        result = ""
        if self.connections:
            result += 'From here you can go to:\n'
            for connection in self.connections:
                result += "\t" + connection + "\n"
        return result

