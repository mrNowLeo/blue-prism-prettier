from lxml import etree

class Display:
    """docstring"""
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.w = 60
        self.h = 30

    def __init__(self, x, y, w, h):
        """Constructor"""
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def get_XML(self):
        display_stageXMLItem = etree.Element('display')
        display_stageXMLItem.set('x', self.x)
        display_stageXMLItem.set('y', self.y)
        display_stageXMLItem.set('w', self.w)
        display_stageXMLItem.set('h', self.h)
        return display_stageXMLItem