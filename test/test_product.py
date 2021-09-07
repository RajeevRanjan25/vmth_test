import unittest
from product import get_price


class ProductTest(unittest.TestCase):
    def test_for_cola(self):
        product_price = get_price('cola')

        assert product_price == 100

    def test_for_chips(self):
        product_price = get_price('chips')

        assert product_price == 50

    def test_for_candy(self):
        product_price = get_price('candy')

        assert product_price == 65


if __name__ == '__main__':
    unittest.main()
