from asyncio import run_coroutine_threadsafe
from unittest import result
from stack.stack import Stack


def convert_to_postfix(infix_expr: str):
    """
    Convert from infix (1*2*3) to postfix(12*3*)

    Args:
        infix_expr (str): infix expression

    Returns:
        str: postfix formatted expression
    """
    precedence = {"*": 2, "/": 2, "+": 1, "-": 1}
    operators = {"*", "/", "+", "-"}

    postfix_expr = ""
    characters = [c.strip() for c in list(infix_expr)]

    stack = Stack(len(characters))

    for ch in characters:
        if ch not in operators:
            postfix_expr += ch
        else:
            if stack.is_empty():
                stack.push(ch)
            else:
                char_precendence = precedence.get(ch)
                stack_precedence = precedence.get(stack.peek(1))

                if char_precendence > stack_precedence:
                    stack.push(ch)
                elif char_precendence <= stack_precedence:
                    top = stack.pop()
                    postfix_expr += top
                    stack.push(ch)

    if not stack.is_empty():
        for _ in range(0, stack.top + 1):
            postfix_expr += stack.pop()

    return postfix_expr


def evaluate_postfix(postfix_expr: str) -> int:
    """
    Evalate postfix expression

    Args:
        postfix_expr (str): postfix expression

    Returns:
        int: evaluation
    """
    characters = [c.strip() for c in list(postfix_expr)]
    operators = {"*", "/", "+", "-"}
    print(f"characters: {characters}")

    stack = Stack(len(characters))
    result = 0

    for ch in characters:
        if ch not in operators:
            stack.push(ch)
        else:
            second_operand = stack.pop()
            first_operand = stack.pop()
            expr_result = eval(f"{first_operand}{ch}{second_operand}")
            stack.push(expr_result)

    result = stack.pop()

    return result


if __name__ == "__main__":
    for input in [
        "1+2+3",
        "1/2+1",
        "1+2*3-1",
        "1+2*3",
        "1*2*3*4",
        "1*2*3-1",
        "1-2*3*4",
    ]:
        postfix = convert_to_postfix(input)
        res = evaluate_postfix(postfix)

        printed = f"""
        expression: {input}
        postfix: {postfix}
        result: {res}
        """
        print(printed)
