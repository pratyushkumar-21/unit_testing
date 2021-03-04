import unittest
from validate_card import valid_card, card_brand

class TestCard(unittest.TestCase):

    def test_card(self):
        self.assertEqual(valid_card("340000000000009"), True)
        self.assertEqual(valid_card("4111111111111112"), False)
        self.assertEqual(valid_card("4111111111111111"), True)
        self.assertEqual(valid_card("6522111111111119"), True)

    def test_card_brand(self):
        self.assertEqual(card_brand("340000000000009"), "american express")
        self.assertEqual(card_brand("4111111111111111"), "visa")
        self.assertEqual(card_brand("4111111111111111"), "visa")
        self.assertEqual(card_brand("6522111111111119"), "rupay")

if __name__ == '__main__':
    unittest.main()
