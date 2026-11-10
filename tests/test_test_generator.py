from src.code_analyzer import analyse_code
from src.test_generator import generate_test_scenarios


def test_generate_discount_scenarios():

    code = """
def calculate_discount(price, discount):

    if price < 0:
        raise ValueError("Invalid price")

    if discount < 0 or discount > 100:
        raise ValueError("Invalid discount")

    return price - (price * discount / 100)
"""

    analysis = analyse_code(code)

    scenarios = generate_test_scenarios(analysis)

    assert len(scenarios) == 6


def test_normal_discount_scenario():

    code = """
def calculate_discount(price, discount):
    return price - (price * discount / 100)
"""

    analysis = analyse_code(code)

    scenarios = generate_test_scenarios(analysis)

    normal_test = scenarios[0]

    assert normal_test["inputs"] == [100, 20]
    assert normal_test["expected"] == 80


def test_negative_price_scenario():

    code = """
def calculate_discount(price, discount):
    return price - (price * discount / 100)
"""

    analysis = analyse_code(code)

    scenarios = generate_test_scenarios(analysis)

    negative_test = scenarios[3]

    assert negative_test["expected_exception"] == "ValueError"