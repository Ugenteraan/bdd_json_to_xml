import xml.etree.ElementTree as xml
import json



f = open('example.json')

json_data = json.load(f)

import xml.etree.ElementTree as xml

filename = "./test_xml.xml"
root = xml.Element("Users")
userelement = xml.Element("user")
root.append(userelement)

uid = xml.SubElement(userelement, "uid")
uid.text = "1"

tree = xml.ElementTree(root)
with open(filename, "wb") as fh:
    tree.write(fh)