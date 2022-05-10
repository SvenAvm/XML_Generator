import xml.etree.ElementTree as ET
from values_generator import times, cc_list, amounts
from datetime import date

current_date = date.today()


def create_xml():
    # we make root element
    log = ET.Element("LOG")

    # create sub element
    log = ET.SubElement(log, "log")

    # insert list element into sub elements
    for x in times:
        time = ET.SubElement(log, "TIME")
        time.text = str(times[x])

        # insert list element into sub elements
    for x in cc_list:
        cc = ET.SubElement(log, "CC")
        cc.text = str(cc_list[x])

        # insert list element into sub elements
    for x in amounts:
        amount = ET.SubElement(log, "AMOUNT")
        amount.text = str(amounts[x])

    date = ET.SubElement(log, "DATE")
    date.text = str(current_date)

    tree = ET.ElementTree(log)

    # write the tree into an XML file
    tree.write("Output.xml", encoding='utf-8', xml_declaration=True)


create_xml()