def generate_test_scenarios(analysis):

    scenarios = []

    for function in analysis["functions"]:

        function_name = function["name"]
        parameters = function["parameters"]

        if function_name == "calculate_discount":

            scenarios.extend([
                {
                    "name": "normal_discount",
                    "inputs": [100, 20],
                    "expected": 80
                },
                {
                    "name": "zero_discount",
                    "inputs": [100, 0],
                    "expected": 100
                },
                {
                    "name": "full_discount",
                    "inputs": [100, 100],
                    "expected": 0
                },
                {
                    "name": "negative_price",
                    "inputs": [-100, 20],
                    "expected_exception": "ValueError"
                },
                {
                    "name": "negative_discount",
                    "inputs": [100, -10],
                    "expected_exception": "ValueError"
                },
                {
                    "name": "discount_above_100",
                    "inputs": [100, 120],
                    "expected_exception": "ValueError"
                }
            ])

    return scenarios