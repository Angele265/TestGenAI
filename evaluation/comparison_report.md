
# TestGenAI – Experimental Comparison Report

## 1. Project Objective

Evaluate three approaches for generating unit tests
for an existing Python calculator function:

1. Manual test development
2. Rule-based test generation
3. AI-assisted test generation

## 2. Experimental Environment

- Operating system: Windows
- Python: 3.12.10
- Testing framework: pytest 9.2.0
- AI runtime: Ollama
- AI model: Qwen 2.5 Coder
- Project language: Python

## 3. Test Coverage Comparison

| Metric | Manual | Rule-based | AI-generated |
|---|---:|---:|---:|
| Tests generated/written | 7 | 6 | 7 |
| Tests passed | 7 | 6 | 7 |
| Tests failed | 0 | 0 | 0 |
| Statement coverage | 100% | 100% | 100% |
| Branch coverage | 100% | 100% | 100% |

## 4. Execution Performance

| Metric | Manual | Rule-based | AI-generated |
|---|---:|---:|---:|
| Test execution time | 0.12 s | 0.16 s | 0.7709 s |
| Generation time | N/A | Not measured | 21.3193 s |

Note: Execution times were obtained from separate
pytest runs and are indicative, not controlled
benchmark measurements.

The AI generation time measures the Ollama response
time, not just test execution.

## 5. AI Validation Results

The AI-generated code was checked for:

- Valid Python syntax
- Presence of pytest test functions
- Correct pytest import
- Import of the original calculator function
- No redefinition of the original function
- No unnecessary pytest.main() invocation
- Presence of exception assertions

The final generated output passed all structural
validation checks.

## 6. Experimental Observations

### Manual testing

The manually written reference suite achieved
100% statement and branch coverage with seven tests.

### Rule-based generation

The rule-based generator generated six scenarios
and achieved the same coverage.

Its current implementation contains function-specific
logic for the calculator example.

### AI-assisted generation

The AI-assisted approach generated seven test
functions, which passed execution and achieved
100% statement and branch coverage.

The model initially omitted required imports and
produced an incorrect exception expectation.

TestGenAI supplied the required imports through
its code scaffold.

The final generation took 21.3193 seconds.

## 7. Limitations

- Evaluation uses only one relatively simple Python function.
- Full coverage does not guarantee that all possible
  defects will be detected.
- The rule-based generator is currently specialised
  for calculate_discount.
- The AI model may generate incorrect or incomplete tests.
- Execution times were not collected under controlled
  benchmarking conditions.
- The executor is not a security sandbox.

## 8. Conclusion

All three approaches achieved 100% statement
and branch coverage on the selected calculator function.

The rule-based approach generated the smallest test
suite, while the AI-assisted approach successfully
generated executable tests after structural validation
and import scaffolding.

The experiment demonstrates the feasibility of combining
static code analysis, AI-assisted test generation,
structural validation and automated test execution.

Further evaluation using more complex functions,
additional datasets and repeated performance measurements
is required to assess generalisation and reliability.
