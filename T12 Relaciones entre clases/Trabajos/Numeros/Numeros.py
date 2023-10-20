"""
Este programa recibe un digito y lo cambia de forma, ej: decimal a binario

"""


class Numero:

    def __init__(self, numero):
        self.set_numero(numero)

    def set_numero(self, numero):
        self.__numero = numero

    def get_numero(self):
        return self.__numero

class Convertir:

    """En este bloque se pasara de Decimal a otros"""


    @staticmethod
    def dec_bin(numero):
        # Decimal a Binario
        res = bin(numero.get_numero())
        return print(res)

    @staticmethod
    def dec_oct(numero):
        # Decimal a Octal
        res = oct(numero.get_numero())
        return print(res)

    @staticmethod
    def dec_hex(numero):
        # Decimal a Hexadecimal
        res = hex(numero.get_numero())
        return print(res)

    """En este bloque se pasara de Binario a otros"""

    @staticmethod
    def bin_dec(numero):
        # Binario a Decimal
        res = int(numero.get_numero())
        return print(res)

    @staticmethod
    def bin_oct(numero):
        # Binario a Octal
        res = oct(int(numero.get_numero()))
        return print(res)

    @staticmethod
    def bin_hex(numero):
        # Binario a Hexadecimal
        res = hex(int(numero.get_numero()))
        return print(res)

    """En este bloque se pasara de Octal a otros"""

    @staticmethod
    def oct_dec(numero):
        # Octal a Decimal
        res = int(numero.get_numero())
        return print(res)

    @staticmethod
    def oct_bin(numero):
        # Octal a Binario
        res = bin(int(numero.get_numero()))
        return print(res)

    @staticmethod
    def oct_hex(numero):
        # Octal a Hexadecimal
        res = hex(int(numero.get_numero()))
        return print(res)

    """En este bloque se pasara de Hexadecimal a otros"""

    @staticmethod
    def hex_dec(numero):
        # Hexadecimal a Decimal
        res = int(numero.get_numero())
        return print(res)

    @staticmethod
    def hex_bin(numero):
        # Hexadecimal a Binario
        res = bin(int(numero.get_numero()))
        return print(res)

    @staticmethod
    def hex_oct(numero):
        # Hexadecimal a Octadecimal
        res = oct(int(numero.get_numero()))
        return print(res)

    """ Este bloque pasa  a Numeros Romanos """

    @staticmethod
    def dec_rom(numero):
        # Decimal a Numeros Romanos
        res = Romano.int_to_roman(numero.get_numero())
        return print(res)

    @staticmethod
    def bin_rom(numero):
        # Binario a Numeros Romanos
        binr = int(numero.get_numero())
        res = Romano.int_to_roman(binr)
        return print(res)

    @staticmethod
    def hex_rom(numero):
        # Hexadecimal a Numeros Romanos
        hexr = int(numero.get_numero())
        res = Romano.int_to_roman(hexr)
        return print(res)

    @staticmethod
    def oct_rom(numero):
        # Octal a Numeros Romanos
        octr = int(numero.get_numero())
        res = Romano.int_to_roman(octr)
        return print(res)

    # Convertir de Numeros Romanos a otros

    @staticmethod
    def rom_dec(numero):
        # Romano a Decimal
        res = Romano.roman_to_int(numero.get_numero())
        return print(res)

    @staticmethod
    def rom_bin(numero):
        # Romano a Binario
        res = Romano.roman_to_int(numero.get_numero())
        binr = bin(res)
        return print(binr)

    @staticmethod
    def rom_oct(numero):
        # Romano a Octal
        res = Romano.roman_to_int(numero.get_numero())
        octr = bin(res)
        return print(octr)

    @staticmethod
    def rom_hex(numero):
        # Romano a Hexadecimal
        res = Romano.roman_to_int(numero.get_numero())
        hexr = bin(res)
        return print(hexr)


""" Esta clase crea los metodos para comvertir a numeros romanos y viseversa """
class Romano:

    @staticmethod
    def int_to_roman(num):
        roman_dict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        roman_num = ''
        for value, symbol in roman_dict.items():
            while num >= value:
                roman_num += symbol
                num -= value
        return roman_num

    @staticmethod
    def roman_to_int(rom):
        roman_dict = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        result = 0
        i = 0
        while i < len(rom):
            if i+1<len(rom) and rom[i:i+2] in roman_dict:
                result+=roman_dict[rom[i:i+2]]
                i+=2
            else:
                result+=roman_dict[rom[i]]
                i+=1
        return result
