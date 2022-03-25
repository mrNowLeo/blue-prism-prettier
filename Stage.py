from Font import Font
from Display import Display
from lxml import etree
import uuid

class Stage:
    """docstring"""
    
    def __init__(self, name, type, narrative="", subsheet="", loginhibit="", display=Display(x=0, y=0, w=60, h=30), font=Font()):
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
        stage_XML_item= etree.Element('stage')
        stage_XML_item.set('stageid', self.stage_id)
        stage_XML_item.set('name', self.name)
        stage_XML_item.set('type', self.type)

        if self.narrative is not None and self.narrative != '':
            narrative_stage_XML_item = etree.Element('narrative')
            narrative_stage_XML_item.text = self.narrative
            stage_XML_item.append(narrative_stage_XML_item)
        if self.subsheet is not None and self.subsheet != '':
            subsheetid_stage_XML_item = etree.Element('subsheetid')
            subsheetid_stage_XML_item.text = self.subsheet
            stage_XML_item.append(subsheetid_stage_XML_item)

        if self.loginhibit is not None and self.loginhibit != '':
            loginhibit_stage_XML_item = etree.Element('loginhibit')
            loginhibit_stage_XML_item.set('onsuccess', self.loginhibit)
            stage_XML_item.append(loginhibit_stage_XML_item)

        stage_XML_item.append(self.display.get_XML())
        stage_XML_item.append(self.font.get_XML())

        return stage_XML_item