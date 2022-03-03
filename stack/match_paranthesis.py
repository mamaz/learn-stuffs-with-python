from stack.stack import Stack


def is_match_paranthesis(expression: str) -> bool:
    stack = Stack(len(expression))

    try:
        have_parenthesis = False
        for char in expression:
            if char == "(":
                have_parenthesis = True
                stack.push(char)

            if char == ")":
                stack.pop()

        return stack.is_empty() and have_parenthesis
    except:
        return False


if __name__ == "__main__":
    print(is_match_paranthesis("(a+b)*c - d)"))
    print(is_match_paranthesis("a+b*c-d"))
    print(is_match_paranthesis("(a+b)*c - d))"))
    print(is_match_paranthesis("((a+b)*c - d)"))
    print(is_match_paranthesis("((a+b)*c - d"))
    print(is_match_paranthesis("("))
    print(is_match_paranthesis(")"))
