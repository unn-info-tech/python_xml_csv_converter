# export_to_csv.py
import xml.etree.ElementTree as ET
import pandas as pd

tree = ET.parse("phones_updated.xml")
root = tree.getroot()

data = []
for phone in root.findall("phone"):
    name = phone.get("name")
    company = phone.find("company").text
    price = phone.find("price").text
    data.append({"Name": name, "Company": company, "Price": price})

df = pd.DataFrame(data)

df.to_csv("phones.csv", index=False)
print("Data exported to 'phones.csv' successfully.")
