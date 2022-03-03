"""
Check whether a strng is a palindrom
"""
def is_palindrome(string: str):
    reversed_str = reverse_str(string)
    return True if reversed_str == string else False

def reverse_str(string):
    str_list = list(string)
    str_length = len(string)
    half = str_length // 2

    for index in range(half):
        temp = str_list[index]
        str_list[index] = str_list[len(string)-1-index]
        str_list[len(string)-1-index] = temp

    return "".join(str_list)
