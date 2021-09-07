from coin import money_change
products = {
    'cola': 100,
    'chips': 50,
    'candy': 65
}

# Return price of the product by their name
def get_price(prod_name):
    return products[prod_name]

# Conversion of money for product according to money given by user
def product_money_conversion(coin_type, data):
    for i in data.keys():
        data[i] = money_change(coin_type, data[i])
    return data
