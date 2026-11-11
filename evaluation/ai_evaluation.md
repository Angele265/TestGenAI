
# TestGenAI – AI Model Evaluation

## 1. AI Model

- Model: Qwen 2.5 Coder
- Model size: 0.5B parameters
- Runtime: Ollama
- Execution environment: Python 3.12
- Hardware: CPU

## 2. Evaluation Objective

Evaluate whether the AI model can generate
executable pytest unit tests for an existing
Python function.

## 3. Evaluation Criteria

The generated code is checked for:

- Valid Python syntax
- Presence of pytest test functions
- Import of the original function
- No redefinition of the original function
- No pytest.main() invocation
- Appropriate exception assertions

## 4. Observed Results

The AI model generated Python code, but the
output did not satisfy the structural validation
requirements.

| Validation criterion | Result |
|---|---|
| Valid Python syntax | Passed |
| Contains test functions | Passed |
| Contains pytest import | Passed |
| Imports original function | Failed |
| Redefines original function | Failed |
| Contains pytest.main() | Failed |
| Contains exception assertions | Failed |
| Accepted by validator | No |

## 5. Execution Results

- Generated output: Rejected
- Test execution: Not performed
- Statement coverage: Not measured
- Branch coverage: Not measured

## 6. Observed Limitations

The model reproduced the original calculator
implementation instead of importing and testing it.

It also used incorrect exception assertions
and included an unnecessary pytest.main() call.

## 7. Conclusion

The Qwen 2.5 Coder 0.5B model was able to produce
Python code, but its output did not meet the
project's structural requirements for executable
pytest tests.

The validation component correctly rejected
the generated output before execution.

Further evaluation with a stronger model or
improved generation strategy is required.


## Experiment 4 – Semantic Validation

**Model:** qwen2.5-coder:1.5b  
**Target module:** shipping.py  
**Generation time:** 59.1472 seconds

### Validation results

| Check | Result |
|---|---|
| Valid Python | True |
| Contains test functions | True |
| Correct exception handling | False |
| Valid function calls | False |
| Imports original functions | True |
| Safe to execute | False |

### Observations

The AI generated incorrect exception assertions using
pytest.raises() inside equality comparisons.

It also passed the unsupported express=True argument
to is_free_shipping().

The improved validator detected both problems and
prevented execution of the generated tests.

### Conclusion

Semantic validation improves the reliability of
AI-generated unit tests by identifying certain
structural errors before execution.

However, expected return values and business rules
still require additional validation.
