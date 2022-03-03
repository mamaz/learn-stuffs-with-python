from palindrome import is_palindrome

def test_palindrome_true():
    assert is_palindrome("kasurusak") == True

def test_palindrome_madam():
    assert is_palindrome("madam") == True

def test_palindrome_racecar():
    assert is_palindrome("racecar") == True

def test_palindrome_empty():
    assert is_palindrome("") == True

def test_palindrome_single_letter():
    assert is_palindrome("a") == True

def test_palindrome_false():
    assert is_palindrome("anatabaka") == False
