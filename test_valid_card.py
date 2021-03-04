import pytest
from validate_card import valid_card, card_brand

def test_card():
    assert valid_card("340000000000009") == True
    assert valid_card("4111111111111112") == False
    assert valid_card("4111111111111111") == True
    assert valid_card("6522111111111119") == True

def test_card_brand():
    assert card_brand("340000000000009") == "american express"
    assert card_brand("4111111111111111") == "visa"
    assert card_brand("6522111111111119") == "rupay"
