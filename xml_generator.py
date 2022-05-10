from values_generator import times, cc_list, amounts
from datetime import date
import xml.etree.ElementTree as xml
import random

date = date.today()


def generate_xml(filename):
    root = xml.Element("LOG")
    root.append(root)

    date1 = xml.SubElement(root, "DATE")
    date1.text = f"{date}"

    time1 = xml.SubElement(root, "TIME")
    time1.text = f"{random.choice(times)}"

    cc1 = xml.SubElement(root, "CC")
    cc1.text = f"{random.choice(cc_list)}"

    amount1 = xml.SubElement(root, "AMOUNT")
    amount1.text = f"{random.choice(amounts)}"

    tree = xml.ElementTree(root)
    with open(filename, "wb") as files:
        tree.write(files)


if __name__ == "__main__":
    generate_xml("test.xml")
