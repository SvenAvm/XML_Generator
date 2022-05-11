def hide_cards(card_numbers):
    formatted_cards = []
    for card_number in card_numbers:
        last_four = card_number[-4:]
        formatted_card = f"**** **** **** {last_four}"
        formatted_cards.append(formatted_card)