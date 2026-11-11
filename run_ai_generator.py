
import ast
import time
from pathlib import Path

from src.ai_model import TestGenAIModel
from src.ai_validator import validate_generated_tests
from src.test_executor import execute_generated_tests


# ==========================================
# SELECT THE SOURCE MODULE
# ==========================================

TARGET_MODULE = "shipping"

source_path = Path(f"data/sample_code/{TARGET_MODULE}.py")
module_import = f"data.sample_code.{TARGET_MODULE}"

# Load source code
source_code = source_path.read_text(encoding="utf-8")

# Identify public functions
tree = ast.parse(source_code)

function_names = [
    node.name
    for node in tree.body
    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
    and not node.name.startswith("_")
]

print("Initialising TestGenAI...")
print("Target module:", TARGET_MODULE)
print("Functions:", function_names)


# ==========================================
# AI TEST GENERATION
# ==========================================

ai_model = TestGenAIModel()

print("\nGenerating AI unit tests...")

generation_start = time.perf_counter()

generated_tests = ai_model.generate_tests(
    source_code,
    module_import
)

generation_time = time.perf_counter() - generation_start

print("Generation time:", round(generation_time, 4), "seconds")


# ==========================================
# DISPLAY GENERATED TESTS
# ==========================================

print("\nAI GENERATED UNIT TESTS")
print("========================")
print(generated_tests)


# ==========================================
# VALIDATE GENERATED TESTS
# ==========================================

print("\nAI TEST VALIDATION")
print("==================")

validation = validate_generated_tests(
    generated_tests,
    module_import,
    function_names,
    source_code
)

for check, result in validation.items():
    print(f"{check}: {result}")


# ==========================================
# EXECUTE GENERATED TESTS
# ==========================================

print("\nAI TEST EXECUTION")
print("=================")

execution = execute_generated_tests(
    generated_tests,
    module_import,
    function_names
)

if execution["success"]:

    print("Execution successful!")
    print("Passed:", execution["passed"])
    print("Failed:", execution["failed"])

    print("\nPERFORMANCE RESULTS")
    print("===================")

    print(
        "AI generation time:",
        round(generation_time, 4),
        "seconds"
    )

    print(
        "Test execution time:",
        execution["execution_time"],
        "seconds"
    )

else:

    print("Execution unsuccessful.")

    if "message" in execution:
        print(execution["message"])

    if "output" in execution:
        print(execution["output"])
