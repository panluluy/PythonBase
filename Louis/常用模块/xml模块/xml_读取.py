__author__ = 'Louis-Pan'

import xml.etree.ElementTree as ET

tree = ET.parse('xmltest.xml')
# 获取xml文件的根节点
root = tree.getroot()

# 获取xml文件根节点的标签名
print(root.tag)

# 遍历xml文档
for child in root:
    # 打印子节点的标签，属性名
    print(child.tag,child.attrib)
    for i in child:
        # 打印子标签里面的tag名，和文本值
        print(i.tag,i.text)
    print("====================")

# 只取year节点
for node in root.iter('year'):
    print(node.tag,node.attrib,node.text)