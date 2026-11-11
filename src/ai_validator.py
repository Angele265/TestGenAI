
import ast


def validate_generated_tests(
    generated_code,
    module_import="data.sample_code.calculator",
    function_names=None,
    source_code=None
):
    if function_names is None:
        function_names = ["calculate_discount"]

    results = {
        "valid_python": False,
        "contains_test_functions": False,
        "redefines_original_function": False,
        "contains_pytest": False,
        "contains_pytest_main": False,
        "has_exception_assertions": False,
        "correct_exception_handling": False,
        "valid_function_calls": True,
        "imports_original_function": False,
        "safe_to_execute": False
    }

    cleaned_code = generated_code.replace("```python", "")
    cleaned_code = cleaned_code.replace("```", "").strip()

    try:
        tree = ast.parse(cleaned_code)
        results["valid_python"] = True

        imported_functions = set()
        pytest_raises_in_with = set()
        pytest_raises_calls = set()
        function_signatures = {}

        # Read original function signatures
        if source_code:
            source_tree = ast.parse(source_code)

            for node in source_tree.body:
                if isinstance(node, ast.FunctionDef):
                    function_signatures[node.name] = {
                        "positional": [
                            arg.arg for arg in node.args.posonlyargs
                        ] + [
                            arg.arg for arg in node.args.args
                        ],
                        "keyword_only": [
                            arg.arg for arg in node.args.kwonlyargs
                        ],
                        "defaults": len(node.args.defaults),
                        "vararg": node.args.vararg is not None,
                        "kwarg": node.args.kwarg is not None
                    }

        # Inspect generated tests
        for node in ast.walk(tree):

            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                if node.name.startswith("test_"):
                    results["contains_test_functions"] = True

                if node.name in function_names:
                    results["redefines_original_function"] = True

            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name == "pytest":
                        results["contains_pytest"] = True

            elif isinstance(node, ast.ImportFrom):
                if node.module == "pytest":
                    results["contains_pytest"] = True

                if node.module == module_import:
                    for alias in node.names:
                        imported_functions.add(alias.name)

            if isinstance(node, ast.Call):
                if (
                    isinstance(node.func, ast.Attribute)
                    and isinstance(node.func.value, ast.Name)
                    and node.func.value.id == "pytest"
                ):
                    if node.func.attr == "main":
                        results["contains_pytest_main"] = True

                    if node.func.attr == "raises":
                        results["has_exception_assertions"] = True
                        pytest_raises_calls.add(id(node))

                # Check calls to original functions
                if isinstance(node.func, ast.Name):
                    function_name = node.func.id

                    if function_name in function_signatures:
                        signature = function_signatures[function_name]

                        positional_names = signature["positional"]
                        keyword_only_names = signature["keyword_only"]

                        allowed_names = set(
                            positional_names + keyword_only_names
                        )

                        required_count = (
                            len(positional_names)
                            - signature["defaults"]
                        )

                        if not signature["vararg"]:
                            if len(node.args) > len(positional_names):
                                results["valid_function_calls"] = False

                        if len(node.args) < required_count:
                            results["valid_function_calls"] = False

                        if not signature["kwarg"]:
                            for keyword in node.keywords:
                                if (
                                    keyword.arg is not None
                                    and keyword.arg not in allowed_names
                                ):
                                    results["valid_function_calls"] = False

                        used_keywords = [
                            keyword.arg
                            for keyword in node.keywords
                            if keyword.arg is not None
                        ]

                        if len(used_keywords) != len(set(used_keywords)):
                            results["valid_function_calls"] = False

                        positional_used = positional_names[:len(node.args)]

                        if any(name in positional_used for name in used_keywords):
                            results["valid_function_calls"] = False

            if isinstance(node, (ast.With, ast.AsyncWith)):
                for item in node.items:
                    context = item.context_expr

                    if (
                        isinstance(context, ast.Call)
                        and isinstance(context.func, ast.Attribute)
                        and isinstance(context.func.value, ast.Name)
                        and context.func.value.id == "pytest"
                        and context.func.attr == "raises"
                    ):
                        pytest_raises_in_with.add(id(context))

        results["imports_original_function"] = (
            set(function_names).issubset(imported_functions)
        )

        results["correct_exception_handling"] = (
            pytest_raises_calls.issubset(pytest_raises_in_with)
        )

    except SyntaxError:
        pass

    results["safe_to_execute"] = (
        results["valid_python"]
        and results["contains_test_functions"]
        and results["contains_pytest"]
        and results["imports_original_function"]
        and results["correct_exception_handling"]
        and results["valid_function_calls"]
        and not results["redefines_original_function"]
        and not results["contains_pytest_main"]
    )

    return results
