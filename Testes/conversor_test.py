import unittest
from fractions import Fraction

# =========================
# CÓDIGO ORIGINAL IMPORTADO
# =========================

from src.conversor import (
    validar,
    decimalparabase,
    baseparadecimal,
    bin_oct_hex,
    oct_hex,
    valores_max
)


# =====================================
# SUÍTE DE TESTES AUTOMATIZADOS (100)
# =====================================

class TestConversoesBases(unittest.TestCase):

    # -----------------------------
    # TESTES DA VALIDAÇÃO (15)
    # -----------------------------

    def test_validar_01(self):
        self.assertTrue(validar("1010", 2))

    def test_validar_02(self):
        self.assertFalse(validar("1020", 2))

    def test_validar_03(self):
        self.assertTrue(validar("777", 8))

    def test_validar_04(self):
        self.assertFalse(validar("89", 8))

    def test_validar_05(self):
        self.assertTrue(validar("ABC", 16))

    def test_validar_06(self):
        self.assertFalse(validar("G", 16))

    def test_validar_07(self):
        self.assertTrue(validar("10.5", 10))

    def test_validar_08(self):
        self.assertFalse(validar("10..5", 10))

    def test_validar_09(self):
        self.assertTrue(validar("FFFF", 16))

    def test_validar_10(self):
        self.assertFalse(validar("FFFFG", 16))

    def test_validar_11(self):
        self.assertTrue(validar("0", 2))

    def test_validar_12(self):
        self.assertTrue(validar("0.0", 10))

    def test_validar_13(self):
        self.assertFalse(validar(".", 10))

    def test_validar_14(self):
        self.assertTrue(validar("1234567", 8))

    def test_validar_15(self):
        self.assertFalse(validar("128", 8))

    # ----------------------------------------
    # DECIMAL -> OUTRAS BASES (25 TESTES)
    # ----------------------------------------

    def test_dec_bin_01(self):
        self.assertEqual(decimalparabase("10", 2), "1010")

    def test_dec_bin_02(self):
        self.assertEqual(decimalparabase("255", 2), "11111111")

    def test_dec_bin_03(self):
        self.assertEqual(decimalparabase("0", 2), "0")

    def test_dec_bin_04(self):
        self.assertEqual(decimalparabase("1", 2), "1")

    def test_dec_bin_05(self):
        self.assertEqual(decimalparabase("2", 2), "10")

    def test_dec_bin_06(self):
        self.assertEqual(decimalparabase("7", 2), "111")

    def test_dec_bin_07(self):
        self.assertEqual(decimalparabase("8", 2), "1000")

    def test_dec_bin_08(self):
        self.assertEqual(decimalparabase("15", 2), "1111")

    def test_dec_bin_09(self):
        self.assertEqual(decimalparabase("16", 2), "10000")

    def test_dec_bin_10(self):
        self.assertEqual(decimalparabase("31", 2), "11111")

    def test_dec_oct_01(self):
        self.assertEqual(decimalparabase("8", 8), "10")

    def test_dec_oct_02(self):
        self.assertEqual(decimalparabase("64", 8), "100")

    def test_dec_oct_03(self):
        self.assertEqual(decimalparabase("511", 8), "777")

    def test_dec_oct_04(self):
        self.assertEqual(decimalparabase("9", 8), "11")

    def test_dec_oct_05(self):
        self.assertEqual(decimalparabase("73", 8), "111")

    def test_dec_hex_01(self):
        self.assertEqual(decimalparabase("15", 16), "F")

    def test_dec_hex_02(self):
        self.assertEqual(decimalparabase("16", 16), "10")

    def test_dec_hex_03(self):
        self.assertEqual(decimalparabase("255", 16), "FF")

    def test_dec_hex_04(self):
        self.assertEqual(decimalparabase("4095", 16), "FFF")

    def test_dec_hex_05(self):
        self.assertEqual(decimalparabase("65535", 16), "FFFF")

    def test_dec_frac_01(self):
        self.assertTrue(decimalparabase("10.5", 2).startswith("1010,1"))

    def test_dec_frac_02(self):
        self.assertTrue(decimalparabase("0.5", 2).startswith("0,1"))

    def test_dec_frac_03(self):
        self.assertTrue(decimalparabase("0.25", 2).startswith("0,01"))

    def test_dec_frac_04(self):
        self.assertTrue(decimalparabase("0.75", 2).startswith("0,11"))

    def test_dec_frac_05(self):
        self.assertTrue(decimalparabase("10.625", 2).startswith("1010,101"))

    # ----------------------------------------
    # OUTRAS BASES -> DECIMAL (25 TESTES)
    # ----------------------------------------

    def test_bin_dec_01(self):
        self.assertEqual(baseparadecimal("1010", 2), "10")

    def test_bin_dec_02(self):
        self.assertEqual(baseparadecimal("11111111", 2), "255")

    def test_bin_dec_03(self):
        self.assertEqual(baseparadecimal("0", 2), "0")

    def test_bin_dec_04(self):
        self.assertEqual(baseparadecimal("1", 2), "1")

    def test_bin_dec_05(self):
        self.assertEqual(baseparadecimal("10000", 2), "16")

    def test_oct_dec_01(self):
        self.assertEqual(baseparadecimal("10", 8), "8")

    def test_oct_dec_02(self):
        self.assertEqual(baseparadecimal("777", 8), "511")

    def test_oct_dec_03(self):
        self.assertEqual(baseparadecimal("11", 8), "9")

    def test_oct_dec_04(self):
        self.assertEqual(baseparadecimal("111", 8), "73")

    def test_oct_dec_05(self):
        self.assertEqual(baseparadecimal("100", 8), "64")

    def test_hex_dec_01(self):
        self.assertEqual(baseparadecimal("F", 16), "15")

    def test_hex_dec_02(self):
        self.assertEqual(baseparadecimal("10", 16), "16")

    def test_hex_dec_03(self):
        self.assertEqual(baseparadecimal("FF", 16), "255")

    def test_hex_dec_04(self):
        self.assertEqual(baseparadecimal("FFF", 16), "4095")

    def test_hex_dec_05(self):
        self.assertEqual(baseparadecimal("FFFF", 16), "65535")

    def test_frac_dec_01(self):
        self.assertTrue(baseparadecimal("1010.1", 2).startswith("10,5"))

    def test_frac_dec_02(self):
        self.assertTrue(baseparadecimal("0.1", 2).startswith("0,5"))

    def test_frac_dec_03(self):
        self.assertTrue(baseparadecimal("0.01", 2).startswith("0,25"))

    def test_frac_dec_04(self):
        self.assertTrue(baseparadecimal("0.11", 2).startswith("0,75"))

    def test_frac_dec_05(self):
        self.assertTrue(baseparadecimal("1010.101", 2).startswith("10,625"))

    def test_frac_hex_01(self):
        self.assertTrue(baseparadecimal("A.8", 16).startswith("10,5"))

    def test_frac_hex_02(self):
        self.assertTrue(baseparadecimal("F.4", 16).startswith("15,25"))

    def test_frac_oct_01(self):
        self.assertTrue(baseparadecimal("7.4", 8).startswith("7,5"))

    def test_frac_oct_02(self):
        self.assertTrue(baseparadecimal("10.2", 8).startswith("8,25"))

    def test_frac_oct_03(self):
        self.assertTrue(baseparadecimal("1.1", 8).startswith("1,125"))

    # ----------------------------------------
    # BINÁRIO <-> OCTAL/HEX (20 TESTES)
    # ----------------------------------------

    def test_bin_oct_01(self):
        self.assertEqual(bin_oct_hex("111", 2, 8), "7")

    def test_bin_oct_02(self):
        self.assertEqual(bin_oct_hex("1000", 2, 8), "10")

    def test_bin_oct_03(self):
        self.assertEqual(bin_oct_hex("111111111", 2, 8), "777")

    def test_oct_bin_01(self):
        self.assertEqual(bin_oct_hex("7", 8, 2), "111")

    def test_oct_bin_02(self):
        self.assertEqual(bin_oct_hex("10", 8, 2), "1000")

    def test_oct_bin_03(self):
        self.assertEqual(bin_oct_hex("777", 8, 2), "111111111")

    def test_bin_hex_01(self):
        self.assertEqual(bin_oct_hex("1111", 2, 16), "F")

    def test_bin_hex_02(self):
        self.assertEqual(bin_oct_hex("11111111", 2, 16), "FF")

    def test_bin_hex_03(self):
        self.assertEqual(bin_oct_hex("10101010", 2, 16), "AA")

    def test_hex_bin_01(self):
        self.assertEqual(bin_oct_hex("F", 16, 2), "1111")

    def test_hex_bin_02(self):
        self.assertEqual(bin_oct_hex("FF", 16, 2), "11111111")

    def test_hex_bin_03(self):
        self.assertEqual(bin_oct_hex("AA", 16, 2), "10101010")

    def test_bin_oct_frac_01(self):
        self.assertEqual(bin_oct_hex("111.111", 2, 8), "7,7")

    def test_bin_hex_frac_01(self):
        self.assertEqual(bin_oct_hex("1111.1111", 2, 16), "F,F")

    def test_oct_bin_frac_01(self):
        self.assertEqual(bin_oct_hex("7.7", 8, 2), "111,111")

    def test_hex_bin_frac_01(self):
        self.assertEqual(bin_oct_hex("F.F", 16, 2), "1111,1111")

    def test_bin_hex_04(self):
        self.assertEqual(bin_oct_hex("0001", 2, 16), "1")

    def test_bin_oct_04(self):
        self.assertEqual(bin_oct_hex("001", 2, 8), "1")

    def test_hex_bin_04(self):
        self.assertEqual(bin_oct_hex("1", 16, 2), "1")

    def test_oct_bin_04(self):
        self.assertEqual(bin_oct_hex("1", 8, 2), "1")

    # ----------------------------------------
    # OCTAL <-> HEXADECIMAL (10 TESTES)
    # ----------------------------------------

    def test_oct_hex_01(self):
        self.assertEqual(oct_hex("10", 8, 16), "8")

    def test_oct_hex_02(self):
        self.assertEqual(oct_hex("17", 8, 16), "F")

    def test_oct_hex_03(self):
        self.assertEqual(oct_hex("377", 8, 16), "FF")

    def test_oct_hex_04(self):
        self.assertEqual(oct_hex("777", 8, 16), "1FF")

    def test_oct_hex_05(self):
        self.assertEqual(oct_hex("20", 8, 16), "10")

    def test_hex_oct_01(self):
        self.assertEqual(oct_hex("8", 16, 8), "10")

    def test_hex_oct_02(self):
        self.assertEqual(oct_hex("F", 16, 8), "17")

    def test_hex_oct_03(self):
        self.assertEqual(oct_hex("FF", 16, 8), "377")

    def test_hex_oct_04(self):
        self.assertEqual(oct_hex("1FF", 16, 8), "777")

    def test_hex_oct_05(self):
        self.assertEqual(oct_hex("10", 16, 8), "20")

    # ----------------------------------------
    # VALORES MÁXIMOS (5 TESTES)
    # ----------------------------------------

    def test_max_01(self):
        # 2**1 - 1 = 1
        self.assertEqual(valores_max(1), (1, "1", "1", "1"))

    def test_max_02(self):
        # 2**4 - 1 = 15
        self.assertEqual(valores_max(4), (15, "1111", "17", "F"))

    def test_max_03(self):
        # 2**8 - 1 = 255
        self.assertEqual(valores_max(8), (255, "11111111", "377", "FF"))

    def test_max_04(self):
        # 2**16 - 1 = 65535
        self.assertEqual(valores_max(16), (65535, "1111111111111111", "177777", "FFFF"))

    def test_max_05(self):
        # 2**32 - 1 = 4294967295
        esperado_32 = (
            4294967295, 
            "11111111111111111111111111111111", 
            "37777777777", 
            "FFFFFFFF"
        )
        self.assertEqual(valores_max(32), esperado_32)
        
# ----------------------------------------
# EXECUÇÃO DOS TESTES
# ----------------------------------------

if __name__ == "__main__":
    unittest.main(verbosity=2)