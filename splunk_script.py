import random
from random import randrange
import xml.etree.ElementTree as Elem_tree
from datetime import date


times, cc_list, amounts, cc_iterations, time_iterations, amounts_iterations = [], [], [], 0, 0, 0
current_date = date.today()
log_iterations_list = []
iterations_required = 10000
log_iterations_counter = 0
while len(log_iterations_list) < 10000:
    log_iterations_counter += 1
    log_iterations_list.append(log_iterations_counter)


# filling up the cc list
while cc_iterations < 10000:
    cc_list.append(randrange(1000000000000000, 10000000000000000))
    cc_iterations += 1

# filling up the times list
while time_iterations < 10000:
    times.append(f"{randrange(24):02}{randrange(60):02}{randrange(60):02}")
    time_iterations += 1

# filling the amounts list
while amounts_iterations < 10000:
    amounts.append(round(random.uniform(1.01, 9999.99), 2))
    amounts_iterations += 1

# filling up the times list
while time_iterations < 10000:
    times.append(f"{randrange(24):02}{randrange(60):02}{randrange(60):02}")
    time_iterations += 1


def create_xml():
    function_iterations_counter = 0
    with open('logs.xml', 'a', encoding='utf-8') as xml_file:

        while function_iterations_counter < 10000:
            # we make root element
            log = Elem_tree.Element("LOG")

            # create sub element
            log = Elem_tree.SubElement(log, "log")

            date_used = Elem_tree.SubElement(log, "DATE")
            date_used.text = str(current_date)

            time = Elem_tree.SubElement(log, "TIME")
            time.text = str(times[function_iterations_counter])

            cc = Elem_tree.SubElement(log, "CC")
            cc.text = str(cc_list[function_iterations_counter])

            amount = Elem_tree.SubElement(log, "AMOUNT")
            amount.text = str(amounts[function_iterations_counter])

            tree = Elem_tree.ElementTree(log)
            function_iterations_counter += 1

            tree.write(xml_file, encoding='unicode', xml_declaration=True)


def hide_card_details():
    formatted_cards = []
    for cc in cc_list:
        formatted_cards.append(f"**** **** **** {str(cc)[-4:]}")


create_xml()
