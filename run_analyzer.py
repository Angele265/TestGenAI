from pathlib import Path

from src.code_analyzer import analyse_code
from src.test_generator import generate_test_scenarios


source_path = Path("data/sample_code/calculator.py")

source_code = source_path.read_text(encoding="utf-8")

analysis = analyse_code(source_code)

scenarios = generate_test_scenarios(analysis)


print("\nCODE ANALYSIS")
print("====================")

print(analysis)


print("\nGENERATED TEST SCENARIOS")
print("====================")

for scenario in scenarios:

    print(f"\nTest: {scenario['name']}")
    print(f"Inputs: {scenario['inputs']}")

    if "expected" in scenario:
        print(f"Expected result: {scenario['expected']}")

    if "expected_exception" in scenario:
        print(f"Expected exception: {scenario['expected_exception']}")