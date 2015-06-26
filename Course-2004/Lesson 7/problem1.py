from xml.dom.ext.reader.Sax import FromXmlFile
from xml.dom.NodeFilter import NodeFilter

root = FromXmlFile('problem1.xml')

walker = root.createTreeWalker(root.documentElement,
                              NodeFilter.SHOW_ELEMENT, None, 0)

while 1:
    nodeName = walker.currentNode.nodeName

    if nodeName == 'game':
        print("Hey, I found the game tag!")
        
    next = walker.nextNode()
    
    if next is None: break
