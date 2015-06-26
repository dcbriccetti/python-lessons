from xml.dom.ext.reader.Sax import FromXmlFile
from xml.dom.NodeFilter import NodeFilter

root = FromXmlFile('problem2.xml')
walker = root.createTreeWalker(root.documentElement,
                              NodeFilter.SHOW_ELEMENT, None, 0)

while 1:
    print(walker.currentNode)
    print(walker.currentNode.attributes)
    next = walker.nextNode()
    if next is None: break
