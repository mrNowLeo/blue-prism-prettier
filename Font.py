from lxml import etree

class Font:
    """docstring"""

    def __init__(self, family='Segoe UI', size='10', style='Regular', color='000000'):
        self.family = family
        self.size = size
        self.style = style
        self.color = color
    
    def get_XML(self):
        font_stageXMLItem = etree.Element('font')
        font_stageXMLItem.set('family', self.family)
        font_stageXMLItem.set('size', self.size)
        font_stageXMLItem.set('style', self.style)
        font_stageXMLItem.set('color', self.color)
        return font_stageXMLItem