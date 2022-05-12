import xml.etree.ElementTree as ET
from values_generator import times, cc_list, amounts
from datetime import date


current_date = date.today()
log_iterations_list = []
iterations_required = 10000
log_iterations_counter = 0
while len(log_iterations_list) < 10000:
    log_iterations_counter += 1
    log_iterations_list.append(log_iterations_counter)


def create_xml():
    function_iterations_counter = 0
    with open('logs.xml', 'a', encoding='utf-8') as xml_file:

        while function_iterations_counter < 10000:
            # we make root element
            log = ET.Element("LOG")

            # create sub element
            log = ET.SubElement(log, "log")

            date = ET.SubElement(log, "DATE")
            date.text = str(current_date)

            time = ET.SubElement(log, "TIME")
            time.text = str(times[function_iterations_counter])

            cc = ET.SubElement(log, "CC")
            cc.text = str(cc_list[function_iterations_counter])

            amount = ET.SubElement(log, "AMOUNT")
            amount.text = str(amounts[function_iterations_counter])

            tree = ET.ElementTree(log)
            function_iterations_counter += 1

            tree.write(xml_file, encoding='unicode', xml_declaration=True)


# Create a list of formatted credit cards using the full card numbers as input, list is called "formatted_cards"

def hide_card_details():
    formatted_cards = []
    for cc in cc_list:
        formatted_cards.append(f"**** **** **** {str(cc)[-4:]}")


create_xml()

hide_card_details()

with open("logs.xml") as file:
    for line in file:
        print(line)



