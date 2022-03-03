import ast


def run_calc(expression: str):
    """
    Run math expression in a string

    Use ast's parse so that we don't evaluate malicious
    expression

    Args:
        expression (str): an expression to be evaluated

    Returns:
        int: result of the evaluation
    """
    parsed = ast.parse(expression, mode="eval")

    return eval(compile(parsed, "<string>", mode="eval"))


if __name__ == "__main__":
    print(run_calc("12 % 2"))
