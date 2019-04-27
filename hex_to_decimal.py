
def hex_to_decimal(word):
    word = reversed(word)
    decimal = 0
    for idx,letter in enumerate(word):
        digit = letter_to_decimal(letter) * (16**idx)
        decimal = digit+decimal
    return decimal

def letter_to_decimal(letter):
    if letter == 'A':
        return 10
    if letter == 'B':
        return 11
    if letter =='C':
        return 12
    if letter == 'D':
        return 13
    if letter == 'E':
        return 14
    if letter == 'F':
        return 15
    else:
        return int(letter)

