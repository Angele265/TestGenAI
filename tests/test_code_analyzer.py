from src.code_analyzer import analyse_code


def test_function_detection():

    code = """
def add(a, b):
    return a + b
"""

    result = analyse_code(code)

    assert len(result["functions"]) == 1
    assert result["functions"][0]["name"] == "add"


def test_parameter_detection():

    code = """
def multiply(a, b):
    return a * b
"""

    result = analyse_code(code)

    assert result["functions"][0]["parameters"] == ["a", "b"]


def test_condition_detection():

    code = """
def check_age(age):
    if age < 18:
        return False
    return True
"""

    result = analyse_code(code)

    assert "age < 18" in result["conditions"]


def test_exception_detection():

    code = """
def validate(value):
    if value < 0:
        raise ValueError("Invalid")
"""

    result = analyse_code(code)

    assert len(result["exceptions"]) == 1
    assert "ValueError" in result["exceptions"][0]