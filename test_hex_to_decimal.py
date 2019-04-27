import unittest
from interfaz_hex_to_decimal import interfaz_hex_to_decimal

class Test_hex_to_decimal(unittest.TestCase):
    def test_5(self):
        value = interfaz_hex_to_decimal(5)
        self.assertEqual(5,value)
    def test_A(self):
        value = interfaz_hex_to_decimal('A')
        self.assertEqual(10,value)
    def test_Hola(self):
        value = interfaz_hex_to_decimal('HoLA')
        self.assertEqual('Disculpe, solo acepto caracteres del sistema hexadecimal',value)
    def test_11(self):
        value = interfaz_hex_to_decimal(11)
        self.assertEqual(17,value)
    def test_10(self):
        value = interfaz_hex_to_decimal(10)
        self.assertEqual(16,value)
    def test_FFF(self):
        value = interfaz_hex_to_decimal('FFF')
        self.assertEqual(4095,value)
    def test_4D2(self):
        value = interfaz_hex_to_decimal('4D2')
        self.assertEqual(1234,value)
    def test_EA(self):
        value = interfaz_hex_to_decimal('EA')
        self.assertEqual(234,value)

if __name__ == '__main__':
    unittest.main()