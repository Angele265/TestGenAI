
# TestGenAI – AI-Generated Test Coverage

## 1. Test Subject

`data/sample_code/calculator.py`

## 2. AI Model

- Model: Qwen 2.5 Coder
- Version: 1.5B parameters
- Runtime: Ollama
- Language: Python 3.12
- Framework: pytest

## 3. Testing Approach

The AI model generated seven pytest test functions.

TestGenAI automatically supplied the required imports
before validating and executing the generated code.

The generated tests were also saved in:

`tests/test_calculator_ai_generated.py`

## 4. Test Scenarios

1. Normal discount
2. Zero discount
3. Full discount
4. Zero price
5. Negative price
6. Negative discount
7. Discount above 100%

## 5. Coverage Results

| Metric | Result |
|---|---:|
| Tests executed | 7 |
| Tests passed | 7 |
| Tests failed | 0 |
| Statement coverage | 100% |
| Branch coverage | 100% |
| Missing statements | 0 |
| Partial branches | 0 |
| Pytest execution time | 0.17 seconds |

## 6. Conclusion

The AI-generated test suite successfully executed
all seven test cases.

It achieved 100% statement coverage and
100% branch coverage.

The result demonstrates that the AI-assisted
generation pipeline can produce executable
unit tests for the selected calculator function.

## 7. Limitations

The model initially omitted required imports
and generated an incorrect exception expectation.

TestGenAI supplied the missing imports through
its code scaffold.

The result is based on one relatively simple
calculator function and does not establish
generalisation to arbitrary Python programs.


# Shipping AI Test Coverage Evaluation

## Objective
Evaluate the code coverage achieved by AI-derived unit tests
against manually written reference tests.

## Results

| Metric | Reference tests | AI-derived tests |
|---|---:|---:|
| Test cases | 12 | 14 |
| Statements | 20 | 20 |
| Missed statements | 0 | 0 |
| Branches | 14 | 14 |
| Partial branches | 0 | 0 |
| Statement coverage | 100% | 100% |
| Branch coverage | 100% | 100% |

## Analysis

Both test suites achieved 100% statement coverage and
100% branch coverage for shipping.py.

The AI-derived test suite covered all measured execution
paths after manual review and correction.

The AI model's original output contained errors, including
incorrect exception assertions and invalid function calls.
Therefore, these results represent a manually reviewed
AI-derived test suite, not fully autonomous AI performance.

## Conclusion

AI-derived test scenarios can achieve complete code
coverage on this example when reviewed and corrected.

However, code coverage alone does not establish test
correctness or effectiveness. Further evaluation using
mutation testing and independent expected-value checks
is necessary.
