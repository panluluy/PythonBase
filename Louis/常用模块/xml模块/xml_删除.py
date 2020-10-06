__author__ = 'Louis-Pan'
import xml.etree.ElementTree as ET

tree = ET.parse('xmltest.xml')
root = tree.getroot()

for country in root.findall('country'):
    rank = int(country.find('rank').text)
    if rank >60:
        root.remove(country)
tree.write('output.xml')