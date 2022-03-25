from lxml import etree
from Stage import Stage
from Display import Display
from Font import Font

tree = etree.parse('ObjOld.xml')
root = tree.getroot()

def get_child_array(element, tag):
    arr = []
    for child in element:
        if child.tag == tag:
            for child_inputs in child:
                arr.append([child_inputs.get('stage'), child_inputs.get('narrative')])
    return arr

def beautify_BP_code():
    inputs = []
    outputs = []
    min_x = 1000
    process_info_x = 0
    process_info_y = 0
    subsheet_id = ""

    for event, elem in etree.iterparse("ObjOld.xml"):

        if elem.tag == 'subsheetid':
            subsheet_id = elem.text
        # Получение списка входящих параметров
        if elem.get('name') == "Start":
            inputs = get_child_array(elem, "inputs")
        # Получение списка исходящих параметров
        if elem.get('name') == "End":
            outputs = get_child_array(elem, "outputs")
        # Получение Х координаты Описания процесса, для правильного позиционирования блоков с переменными
        if elem.get('type') == "ProcessInfo" or elem.get('type') == "SubSheetInfo":
            for item in elem:
                if item.tag == 'display':
                    process_info_x = int(item.get('x'))
                    process_info_y = int(item.get('y'))
        # Получение Х координаты самого левого элемента, чтобы относительно его позиционировать Описание процесса и переменные
        if elem.tag == "stage":
            for item in elem:
                if (item.tag == 'display' and int(item.get('x')) > min_x and elem.get('type') != "ProcessInfo"):
                    min_x = int(item.get('x'))

    for elem in root:
        for i in range(len(inputs)):
            if elem.get('name') in inputs[i]:
                for item in elem:
                    if item.tag == 'display':
                        item.set('x', str(process_info_x - 255))
                        item.set('y', str(process_info_y + i * 30 + 90))
                root.append(Stage(
                    name = inputs[i][0] + '_Note', 
                    type = 'Note', 
                    narrative = inputs[i][1], 
                    subsheet = subsheet_id,
                    display = Display(
                        x = str(process_info_x - 165), 
                        y = str(process_info_y + i * 30 + 90), 
                        w = '90', 
                        h = '30')
                    ).get_XML()
                )
         
        for i in range(len(outputs)):
            if elem.get('name') in outputs[i]:
                for item in elem:
                    if item.tag == 'display':
                        item.set('x', str(process_info_x - 45))
                        item.set('y', str(process_info_y + i * 30 + 90))
                root.append(Stage(outputs[i][0] + '_Note', 'Note', outputs[i][1], subsheet_id, '', Display(str(process_info_x + 45), str(process_info_y + i * 30 + 90), '90', '30')).get_XML())
            
    if len(inputs) > 0:
        # Создание блока для входящих параметров
        root.append(Stage('Input', 'Block', '', subsheet_id, 'true', Display(str(process_info_x - 300), str(process_info_y + 60), '195', str((len(inputs) + 1) * 30)), Font(color='008000')).get_XML())

    if len(outputs) > 0:
        # Создание блока для исходящих параметров
        root.append(Stage('Output', 'Block', '', subsheet_id, 'true', Display(str(process_info_x - 90), str(process_info_y + 60), '195', str((len(outputs) + 1) * 30)), Font(color='FF9900')).get_XML())

    tree.write('ObjNew.xml')

if __name__ == '__main__':
    beautify_BP_code()