__author__ = 'Louis-Pan'

import xml.etree.ElementTree as ET

tree = ET.parse('xmltest.xml')
root = tree.getroot()

# 遍历根节点下的所有year标签
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    # 往year节点添加新的属性update=yes
    node.set('update','yes')
tree.write('xmltest.xml')