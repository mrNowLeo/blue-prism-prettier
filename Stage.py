from Font import Font
from Display import Display
from lxml import etree
import uuid

class Stage:
    """docstring"""
    
    def __init__(self, name, type, narrative="", subsheet="", loginhibit="", display=Display(), font=Font()):
        """Constructor"""
        self.stage_id = str(uuid.uuid4())
        self.name = name
        self.type = type
        self.narrative = narrative
        self.subsheet = subsheet
        self.loginhibit = loginhibit
        self.display = display
        self.font = font
    
    def get_XML(self):
        stageXMLItem= etree.Element('stage')
        stageXMLItem.set('stageid', self.stage_id)
        stageXMLItem.set('name', self.name)
        stageXMLItem.set('type', self.type)

        if self.narrative is not None and self.narrative != '':
            narrative_stageXMLItem = etree.Element('narrative')
            narrative_stageXMLItem.text = self.narrative
            stageXMLItem.append(narrative_stageXMLItem)
        if self.subsheet is not None and self.subsheet != '':
            subsheetid_stageXMLItem = etree.Element('subsheetid')
            subsheetid_stageXMLItem.text = self.subsheet
            stageXMLItem.append(subsheetid_stageXMLItem)

        if self.loginhibit is not None and self.loginhibit != '':
            loginhibit_stageXMLItem = etree.Element('loginhibit')
            loginhibit_stageXMLItem.set('onsuccess', self.loginhibit)
            stageXMLItem.append(loginhibit_stageXMLItem)

        stageXMLItem.append(self.display.get_XML())
        stageXMLItem.append(self.font.get_XML)

        return stageXMLItem