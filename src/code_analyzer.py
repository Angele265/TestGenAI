import ast


def analyse_code(source_code):

    # convert python code into an AST
    tree = ast.parse(source_code)

    analysis = {
        "functions": [],
        "conditions": [],
        "returns": 0,
        "exceptions": []
    }

    for node in ast.walk(tree):

        # Identify functions
        if isinstance(node, ast.FunctionDef):

            function_info = {
                "name": node.name,
                "parameters": [
                    arg.arg for arg in node.args.args
                ]
            }

            analysis["functions"].append(function_info)

        # Identify conditional statements
        elif isinstance(node, ast.If):

            condition = ast.unparse(node.test)

            analysis["conditions"].append(condition)

        # Identify return statements
        elif isinstance(node, ast.Return):

            analysis["returns"] += 1

        # Identify raised exceptions
        elif isinstance(node, ast.Raise):

            if node.exc:
                exception = ast.unparse(node.exc)
                analysis["exceptions"].append(exception)

    return analysis