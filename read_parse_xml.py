import xml.etree.ElementTree as ET

tree = ET.parse("phones.xml")
root = tree.getroot()

for phone in root.findall("phone"):
    name = phone.get("name")
    company = phone.find("company").text
    price = phone.find("price").text
    print(f"Smartphone: {name}\nCompany: {company}\nPrice: {price}\n")
