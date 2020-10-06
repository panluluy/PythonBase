__author__ = 'Louis-Pan'

import xml.etree.ElementTree as ET

# 创建根节点classinfo
new_xml = ET.Element("classinfo")

# 创建子节点person
person1 = ET.SubElement(new_xml,'person',attrib={"name":'Jerry'})
# 创建子节点sex
sex = ET.SubElement(person1,'sex',attrib={"default":'man'})
# 创建子节点age
age = ET.SubElement(person1,'age',attrib={'birthday':'2010'})
# 设置子节点的值10
age.text = '10'

person2 = ET.SubElement(new_xml,'person',attrib={"name":'Tom'})
sex2 = ET.SubElement(person2,'sex',attrib={"default":'man'})
age2 = ET.SubElement(person2,'age',attrib={'birthday':'2015'})
age2.text = '5'

# 写节点
et = ET.ElementTree(new_xml)
# 写xml文档中的第一行
et.write("test.xml",encoding='utf-8',xml_declaration=True)
# 提交文档
ET.dump(new_xml)