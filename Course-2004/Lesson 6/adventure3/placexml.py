from xml.dom.ext.reader.Sax import FromXmlFile
from xml.dom.NodeFilter import NodeFilter
from place import Place

class PlaceXml:

    def __init__(self, filename, places):

        root = FromXmlFile(filename)

        walker = root.createTreeWalker(root.documentElement,
                                      NodeFilter.SHOW_ELEMENT, None, 0)

        while 1:
            nodeName = walker.currentNode.nodeName
            attribs = walker.currentNode.attributes

            if nodeName == 'game':
                self.startingPlace = attribs['startingPlace'].value
                
            elif nodeName == 'place':
                placeName = attribs['name'].value
                desc = attribs['description'].value
                currentPlace = Place(placeName, desc)
                places[placeName] = currentPlace

            elif nodeName == 'object':
                currentPlace.addObject(attribs['name'].value)

            elif nodeName == 'connection':
                currentPlace.addConnection(attribs['place'].value)

            next = walker.nextNode()
            
            if next is None: break
