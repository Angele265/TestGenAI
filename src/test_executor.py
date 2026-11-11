
import re
import sys
import time
import tempfile
import subprocess

from pathlib import Path

from src.ai_validator import validate_generated_tests
from tests.test_calculator_rule_based import source_code


def execute_generated_tests(
    generated_code,
    module_import="data.sample_code.calculator",
    function_names=None,
    timeout_seconds=10,
    source_code=None
):

    project_root = Path(__file__).resolve().parent.parent

    # Keep compatibility with existing calculator tests
    if function_names is None:
        function_names = ["calculate_discount"]

    # Validate generated code before execution
    validation = validate_generated_tests(
        generated_code,
        module_import,
        function_names,
        source_code
    )

    if not validation["safe_to_execute"]:
        return {
            "success": False,
            "message": "Generated tests failed validation.",
            "validation": validation
        }

    # Remove Markdown code fences
    cleaned_code = generated_code.replace("```python", "")
    cleaned_code = cleaned_code.replace("```", "")
    cleaned_code = cleaned_code.strip()

    test_file_path = None

    try:

        # Create temporary test file inside project root
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            suffix=".py",
            prefix="test_ai_generated_",
            dir=project_root,
            delete=False
        ) as temporary_file:

            temporary_file.write(cleaned_code)
            test_file_path = Path(temporary_file.name)

        # Execute pytest in a separate process
        start_time = time.perf_counter()

        result = subprocess.run(
            [
                sys.executable,
                "-m",
                "pytest",
                "-q",
                "--tb=short",
                str(test_file_path)
            ],
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=timeout_seconds
        )

        execution_time = time.perf_counter() - start_time

        output = result.stdout + result.stderr

        # Extract test summary
        summary = re.search(
            r"(\d+) passed(?:, (\d+) failed)?",
            output
        )

        passed = int(summary.group(1)) if summary else 0
        failed = int(summary.group(2)) if summary and summary.group(2) else 0

        return {
            "success": result.returncode == 0,
            "passed": passed,
            "failed": failed,
            "execution_time": round(execution_time, 4),
            "exit_code": result.returncode,
            "output": output
        }

    except subprocess.TimeoutExpired:

        return {
            "success": False,
            "message": f"Execution timed out after {timeout_seconds} seconds."
        }

    except Exception as error:

        return {
            "success": False,
            "message": str(error)
        }

    finally:

        # Delete temporary test file
        if test_file_path and test_file_path.exists():
            test_file_path.unlink()
