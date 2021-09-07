coin = {
    'PENNY': {'weight': 2.5, 'diameter': .75, 'thickness': 1.52, 'value_in_cents': 1, 'valid': False},
    'NICKEL': {'weight': 5.0, 'diameter': .835, 'thickness': 1.95, 'value_in_cents': 5, 'valid': True},
    'DIME': {'weight': 2.268, 'diameter': .705, 'thickness': 1.35, 'value_in_cents': 10, 'valid': True},
    'QUARTER': {'weight': 5.670, 'diameter': .955, 'thickness': 1.75, 'value_in_cents': 25, 'valid': True}
}

# Checking for valid coin
def coin_check(prop, coin_name):
    return (coin[coin_name]['weight'] == prop['weight'] and coin[coin_name]['diameter'] == prop['diameter'] and coin[coin_name]['thickness'] == prop['thickness'] and coin[coin_name]['valid'] == True)

# Conversion from coin type to cents
def money_change_in_cents(coin_name, value):
    return value*coin[coin_name]['value_in_cents']

# Conversion from cents to coin type
def money_change(coin_name, value):
    return value/coin[coin_name]['value_in_cents']
