
# TestGenAI – Rule-Based Test Evaluation

## 1. Test Subject

`data/sample_code/calculator.py`

## 2. Testing Approach

The rule-based generator analyses the calculator source code
using Python AST and generates test scenarios.

The generated scenarios are executed using pytest against
the original calculator implementation.

## 3. Generated Scenarios

1. Normal discount
2. Zero discount
3. Full discount
4. Negative price
5. Negative discount
6. Discount above 100%

## 4. Test Results

| Metric | Result |
|---|---:|
| Scenarios generated | 6 |
| Tests passed | 6 |
| Tests failed | 0 |
| Statement coverage | 100% |
| Branch coverage | 100% |
| Missing statements | 0 |
| Partial branches | 0 |
| Execution time | 0.16 seconds |

## 5. Conclusion

The rule-based generator successfully generated and
executed six test scenarios.

The generated tests achieved 100% statement coverage
and 100% branch coverage.

The results match the manually written reference
test suite, while using one fewer test.

## 6. Limitations

The current rule-based generator contains
function-specific logic for `calculate_discount`.

It has not yet been demonstrated to generalise
to arbitrary Python functions.
