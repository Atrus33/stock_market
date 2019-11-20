def get_adjusted_price(price, currency):
    if currency == "euro":
        return price * 0.9, '€'
    else:
        return price * 0.77, '£'