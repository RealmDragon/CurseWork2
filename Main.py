import json
from datetime import datetime


def mask_card_number(card_number):
    """Маскирует номер карты."""
    return f"XXXX XX** **** {card_number[-4:]}"


