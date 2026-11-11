
import builtins
from pathlib import Path

import pytest

from data.sample_code.calculator import calculate_discount
from src.code_analyzer import analyse_code
from src.test_generator import generate_test_scenarios


# Locate the original calculator source code
PROJECT_ROOT = Path(__file__).resolve().parents[1]

SOURCE_FILE = PROJECT_ROOT / "data" / "sample_code" / "calculator.py"

source_code = SOURCE_FILE.read_text(encoding="utf-8")


# Analyse the source code
analysis = analyse_code(source_code)


# Generate scenarios using TestGenAI
SCENARIOS = generate_test_scenarios(analysis)


# Execute every generated scenario
@pytest.mark.parametrize(
    "scenario",
    SCENARIOS,
    ids=lambda scenario: scenario["name"]
)
def test_generated_scenario(scenario):

    inputs = scenario["inputs"]

    if "expected_exception" in scenario:

        exception_name = scenario["expected_exception"]
        exception_type = getattr(builtins, exception_name)

        with pytest.raises(exception_type):
            calculate_discount(*inputs)

    else:

        result = calculate_discount(*inputs)

        assert result == scenario["expected"]
