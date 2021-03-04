def valid_card(card_number):
    total_sum = 0
    alternate_digit = False

    for i in range(len(card_number)):
        digit = int(card_number[len(card_number)-1-i])
        if alternate_digit:
            digit = 2 * digit
        total_sum += digit // 10
        total_sum += digit % 10
        alternate_digit = False if alternate_digit else True

    if(total_sum % 10 == 0):
        return True
    return False

def card_brand(card_number):
    card_company = { 37: 'american express', 34: 'american express', 60 :'rupay', 6521 :'rupay', 6522 :'rupay',
                    4: 'visa', 6334: 'solo', 6767: 'solo', 1: 'uatp'
    }

    digit = ''
    for i in range(len(card_number)):
        digit += card_number[i]
        if card_company.get(int(digit)) != None:
            return card_company.get(int(digit))
