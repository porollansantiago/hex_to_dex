from hex_to_decimal import hex_to_decimal

def interfaz_hex_to_decimal(inp):
    inp = str(inp)
    hexa_letters = ('0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F')
    for digit in inp:
        if digit not in hexa_letters:
            return "Disculpe, solo acepto caracteres del sistema hexadecimal"
    return hex_to_decimal(inp)

