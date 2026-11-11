
# TestGenAI – Reference Test Coverage

## 1. Test Subject

Calculator discount function:
`data/sample_code/calculator.py`

## 2. Testing Approach

Seven manually written pytest unit tests were used as the reference test suite.

The tests cover:
- Normal discount calculation
- Zero discount
- Full discount
- Zero price
- Negative price
- Negative discount
- Discount above 100%

## 3. Test Results

| Metric | Result |
|---|---:|
| Tests executed | 7 |
| Tests passed | 7 |
| Tests failed | 0 |
| Statement coverage | 100% |
| Branch coverage | 100% |
| Missing statements | 0 |
| Partial branches | 0 |

## 4. Coverage Command

```powershell
pytest tests/test_calculator_reference.py --cov=data.sample_code.calculator --cov-branch --cov-report=term-missing
```

## 5. Conclusion

The manually written reference test suite achieved
100% statement coverage and 100% branch coverage.

All six executable statements and all four measured
branches were covered.

These results establish a reference baseline for
evaluating the rule-based and AI-generated test suites.

**Note:** These coverage results belong to the manually
written reference tests, not the AI-generated tests.
