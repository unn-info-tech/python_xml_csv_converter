# query_modify_xml.py
import xml.etree.ElementTree as ET

tree = ET.parse("phones.xml")
root = tree.getroot()

for phone in root.findall("phone"):
    if phone.get("name") == "Samsung Galaxy S5":
        phone.find("price").text = "31000"

for phone in root.findall("phone"):
    if phone.get("name") == "iPhone 6":
        root.remove(phone)

new_phone = ET.SubElement(root, "phone", name="Nokia Lumia 930")
ET.SubElement(new_phone, "company").text = "Nokia"
ET.SubElement(new_phone, "price").text = "19500"

tree.write("phones_updated.xml", encoding="utf-8", xml_declaration=True)
print("Modified XML file 'phones_updated.xml' saved successfully.")
