
def calculate_shipping(weight, destination, express=False):

    if weight <= 0:
        raise ValueError("Weight must be positive")

    if destination not in ["domestic", "international", "pickup"]:
        raise ValueError("Invalid destination")

    if destination == "pickup":
        cost = 0

    elif destination == "domestic":

        if weight <= 5:
            cost = 5
        else:
            cost = 10

    else:  # international

        if weight <= 5:
            cost = 15
        else:
            cost = 25

    if express and destination != "pickup":
        cost += 10

    return cost


def is_free_shipping(weight, destination):

    shipping_cost = calculate_shipping(weight, destination)

    return shipping_cost == 0

