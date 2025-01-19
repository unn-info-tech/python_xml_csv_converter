
import xml.etree.ElementTree as ET

phones = ET.Element("phones")

iphone6 = ET.SubElement(phones, "phone", name="iPhone 6")
ET.SubElement(iphone6, "company").text = "Apple"
ET.SubElement(iphone6, "price").text = "40000"

galaxys5 = ET.SubElement(phones, "phone", name="Samsung Galaxy S5")
ET.SubElement(galaxys5, "company").text = "Samsung"
ET.SubElement(galaxys5, "price").text = "33000"

tree = ET.ElementTree(phones)
tree.write("phones.xml", encoding="utf-8", xml_declaration=True)
print("XML file 'phones.xml' created successfully.")
