import unittest
from coin import coin_check


class CoinTest(unittest.TestCase):
    def test_for_quartar(self):
        coin = coin_check({'weight': 5.670, 'diameter': .955,
                           'thickness': 1.75}, 'QUARTER')

        assert coin == True

    def test_for_penny(self):
        coin = coin_check({'weight': 2.5, 'diameter': .75,
                           'thickness': 1.52}, 'PENNY')

        assert coin == False

    def test_for_nickel(self):
        coin = coin_check({'weight': 5.0, 'diameter': .835,
                           'thickness': 1.95}, 'NICKEL')

        assert coin == True

    def test_for_dime(self):
        coin = coin_check(
            {'weight': 2.268, 'diameter': .705, 'thickness': 1.35}, 'DIME')

        assert coin == True


if __name__ == '__main__':
    unittest.main()
