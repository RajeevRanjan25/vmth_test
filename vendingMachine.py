from product import get_price, products, product_money_conversion
from coin import coin_check, money_change_in_cents, money_change

coin_data = {
    'PENNY': {'weight': 2.5, 'diameter': .75, 'thickness': 1.52},
    'NICKEL': {'weight': 5.0, 'diameter': .835, 'thickness': 1.95},
    'DIME': {'weight': 2.268, 'diameter': .705, 'thickness': 1.35},
    'QUARTER': {'weight': 5.670, 'diameter': .955, 'thickness': 1.75}
}


class VendingMachine:
    product_count = 0
    product = ""
    coin_type = ""
    no_of_coins = 0
    amount_in_cents = 0
    return_coin_type = ""
    return_coin = 0
    display = ""

    def __init__(self, product, product_count, coin_type, no_of_coins):
        if coin_check(coin_data[coin_type], coin_type):
            self.product_count = product_count
            self.coin_type = coin_type
            self.no_of_coins = no_of_coins
            self.product = product
            self.amount_in_cents = money_change_in_cents(
                coin_type, no_of_coins)
        else:
            self.return_coin_type = coin_type
            self.return_coin = no_of_coins
            self.display = "INVALID COIN"

    # Returns dictionary of product details
    def product_detail(self):
        return {'product_count': self.product_count, 'product': self.product, 'coin_type': self.coin_type, 'no_of_coins': self.no_of_coins, 'return_coin_type': self.return_coin_type, 'return_coin': self.return_coin, 'display': self.display}

    # Successfull or unseccessfull dispense according to transaction made by user
    def dispense(self):
        if self.display == "INVALID COIN":
            return self.display
        elif self.no_of_coins == 0:
            return "INSERT COIN"
        elif self.check_sufficient_money(self.product):
            self.display = "THANK YOU"
            return self.product_detail()
        else:
            self.display = "Insufficient Money, Your money = {}, Total money required = {}, price_list = {}".format(self.no_of_coins, money_change(
                self.coin_type, self.product_count*get_price(self.product)), product_money_conversion(self.coin_type, products))
            self.return_coin_type = self.coin_type
            self.return_coin = self.no_of_coins
            return {"display": self.display, 'return_coin': self.return_coin, 'return_coin_type': self.return_coin_type}

    # Check for money given by user is sufficient or not
    def check_sufficient_money(self, product_name):
        if self.amount_in_cents >= (self.product_count*get_price(product_name)):
            if self.amount_in_cents != (self.product_count*get_price(product_name)):
                self.return_coin_fun()
            else:
                self.return_coin_type = ""
                self.return_coin = 0
            return True
        else:
            return False

    # Return total remaining coins in cents
    def return_coin_fun(self):
        self.return_coin_type = "cents"
        self.return_coin = self.amount_in_cents - \
            (self.product_count*get_price(self.product))
