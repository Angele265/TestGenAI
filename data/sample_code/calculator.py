def calculate_discount(price, discount):

    if price < 0:
        raise ValueError("Invalid price")

    if discount < 0 or discount > 100:
        raise ValueError("Invalid discount")

    return price - (price * discount / 100)