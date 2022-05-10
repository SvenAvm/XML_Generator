from values_generator import times, cc_list, amounts
from datetime import date
import xml.etree.ElementTree as xml
import random

date = date.today()


def generate_xml(filename):
    root = xml.Element("XML_LOG")
    c1 = xml.Element("LOG")
    root.append(c1)
    date1 = xml.SubElement(c1, "DATE")
    date1.text = f"{date}"
    time1 = xml.SubElement(c1, "TIME")
    time1.text = f"{random.choice(times)}"
    cc1 = xml.SubElement(c1, "CC")
    cc1.text = f"{random.choice(cc_list)}"
    amount1 = xml.SubElement(c1, "AMOUNT")
    amount1.text = f"{random.choice(amounts)}"
