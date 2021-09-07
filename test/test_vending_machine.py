import unittest
from parameterized import parameterized
from vendingMachine import VendingMachine


class TestVendingMachine(unittest.TestCase):
    @parameterized.expand([['cola', 1, 'NICKEL', 100]])
    def test_for_successful_dispense_for_1_product(self, product, product_count, coin_type, no_of_coins):
        vm = VendingMachine(product, product_count, coin_type, no_of_coins)
        response = vm.dispense()
        assert response == {'product_count': 1, 'product': 'cola', 'coin_type': 'NICKEL',
                            'no_of_coins': 100, 'return_coin_type': 'cents', 'return_coin': 480.0, 'display': 'THANK YOU'}

    @parameterized.expand([['cola', 2, 'NICKEL', 20]])
    def test_for_successful_dispense_for_2_product(self, product, product_count, coin_type, no_of_coins):
        vm = VendingMachine(product, product_count, coin_type, no_of_coins)
        response = vm.dispense()
        assert response == {'product_count': 2, 'product': 'cola', 'coin_type': 'NICKEL',
                            'no_of_coins': 20, 'return_coin_type': 'cents', 'return_coin': 60.0, 'display': 'THANK YOU'}

    @parameterized.expand([['cola', 2, 'NICKEL', 10]])
    def test_fails_for_less_coin_given(self, product, product_count, coin_type, no_of_coins):
        vm = VendingMachine(product, product_count, coin_type, no_of_coins)
        response = vm.dispense()
        assert response == {'display': "Insufficient Money, Your money = 10, Total money required = 40.0, price_list = {'cola': 20.0, 'chips': 10.0, 'candy': 13.0}",
                            'return_coin': 10, 'return_coin_type': 'NICKEL'}

    @parameterized.expand([['cola', 2, 'NICKEL', 0]])
    def test_fails_for_no_coin_given(self, product, product_count, coin_type, no_of_coins):
        vm = VendingMachine(product, product_count, coin_type, no_of_coins)
        response = vm.dispense()
        assert response == "INSERT COIN"

    @parameterized.expand([['cola', 2, 'PENNY', 10]])
    def test_fails_for_invalid_coin(self, product, product_count, coin_type, no_of_coins):
        vm = VendingMachine(product, product_count, coin_type, no_of_coins)
        response = vm.dispense()
        assert response == "INVALID COIN"


if __name__ == '__main__':
    unittest.main()
