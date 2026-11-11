
import ast
import re
import ollama


class TestGenAIModel:

    def __init__(self):
        self.model_name = "qwen2.5-coder:1.5b"

    def generate_tests(self, source_code, module_import):

        # Identify functions in the supplied source code
        tree = ast.parse(source_code)

        function_names = [
            node.name
            for node in tree.body
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef))
            and not node.name.startswith("_")
        ]

        if not function_names:
            raise ValueError("No public functions found in source code.")

        function_list = ", ".join(function_names)

        # Build the required import automatically
        function_import = (
            f"from {module_import} import {function_list}"
        )

        system_prompt = """
        You are an experienced Python software testing engineer.

        Generate accurate pytest unit tests for the supplied source code.

        STRICT RULES:

        1. Test the original functions.
        2. Never redefine original functions.
        3. Generate separate test functions.
        4. Test normal inputs and boundary values.
        5. Test invalid inputs and expected exceptions.
        6. Understand the actual implementation before choosing expected results.
        7. Never invent expected behaviour.
        8. Test all important branches.
        9. Return Python code only.
        10. Never call pytest.main().

        EXCEPTION HANDLING EXAMPLES:

        CORRECT:
        def test_invalid_weight():
            with pytest.raises(ValueError):
                calculate_shipping(0, "domestic")

        INCORRECT:
        def test_invalid_weight():
            assert calculate_shipping(0, "domestic") == pytest.raises(ValueError)

        IMPORTANT FUNCTION SIGNATURES:

        Read every function signature before generating tests.

        calculate_shipping(weight, destination, express=False)

        is_free_shipping(weight, destination)

        Never pass express to is_free_shipping.

        IMPORTANT BUSINESS RULES:

        - Domestic shipping costs 5 for weight <= 5.
        - Domestic shipping costs 10 for weight > 5.
        - International shipping costs 15 for weight <= 5.
        - International shipping costs 25 for weight > 5.
        - Express shipping adds 10 to the shipping cost.
        - Pickup costs 0.
        - Pickup is free shipping.
        - Domestic and international shipping are not free.
        - Weight must be positive.
        - Invalid destinations raise ValueError.

        Use these rules to verify expected values against the source code.
        """

        user_prompt = f"""
        Generate a comprehensive pytest test module.

        Functions to test:
        {function_list}

        The following imports will be provided by the TestGenAI scaffold:
        {function_import}
        import pytest

        REQUIREMENTS:

        - Generate separate test functions.
        - Test every listed public function.
        - Test normal inputs.
        - Test boundary values.
        - Test invalid inputs.
        - Test expected exceptions.
        - Test nested conditions.
        - Test optional parameters.
        - Verify expected return values against the source code.

        EXCEPTION TEST EXAMPLE:

        def test_invalid_input():
            with pytest.raises(ValueError):
                function_name(invalid_input)

        Never compare a function call with pytest.raises().

        Do not assume that a valid input raises an exception.
        Do not invent business rules.
        Do not redefine original functions.
        Do not implement the original business logic again.
        Do not call pytest.main().

        ORIGINAL SOURCE CODE:

        {source_code}

        Study the source code carefully before generating the tests.
        Return only Python test code.
        """

        response = ollama.chat(
            model=self.model_name,
            messages=[
                {
                    "role": "system",
                    "content": system_prompt
                },
                {
                    "role": "user",
                    "content": user_prompt
                }
            ],
            options={
                "temperature": 0,
                "num_predict": 1200
            }
        )

        content = response["message"]["content"]

        # Extract Python code from Markdown fences
        match = re.search(
            r"```(?:python)?\s*(.*?)```",
            content,
            re.DOTALL
        )

        if match:
            content = match.group(1).strip()
        else:
            content = content.strip()

        # Add required imports through the TestGenAI scaffold
        required_imports = []

        if "import pytest" not in content:
            required_imports.append("import pytest")

        if function_import not in content:
            required_imports.append(function_import)

        if required_imports:
            content = (
                "\n".join(required_imports)
                + "\n\n"
                + content
            )

        return content
