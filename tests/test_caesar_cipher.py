import unittest
from caesar_cipher import encrypt1, encrypt2

# To run from terminal use `python -m tests.test_caesar_cipher` from infosec101/ directory


class TestCaesarCipher(unittest.TestCase):

    def test_no_shift(self):
        self.assertEqual('hello', encrypt1('hello', 0))
        self.assertEqual('hello', encrypt2('hello', 0))

    def test_simple_shift(self):
        self.assertEqual(encrypt1("hello", 3), encrypt2("hello", 3))

    def test_negative_shift(self):
        self.assertEqual(encrypt1("hello",-8), encrypt2("hello", -8))

    def test_invalid_input(self):
        self.assertRaisesRegex(ValueError, "non-alphabet found in plaintext", encrypt2, "h3ll0", 5)

    def test_secret_alphabet(self):
        secret_alphabet = "The quick brown fox jumps over the lazy dog".lower().replace(" ","")
        secret_plaintext = "somethingsecret"
        print(encrypt2(secret_plaintext, 3, secret_alphabet))
        print(encrypt1(secret_plaintext, 3))
        self.assertFalse(encrypt1(secret_plaintext, 3) == encrypt2(secret_plaintext, 3, secret_alphabet))


if __name__ == "__main__":
    unittest.main()
