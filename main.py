import sys
from vendingMachine import VendingMachine

"""
python3 main.py <product_name> <product_count> <coin_type> <no_of_coin>
"""
prod = VendingMachine(sys.argv[1], int(
    sys.argv[2]), sys.argv[3].upper(), int(sys.argv[4]))
print(prod.dispense())
