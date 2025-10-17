# def ...(...):
def is_palindrome(s):
    return s == s[::-1]   # return ...

# Test
print(is_palindrome("racecar"))  # Expected: True
print(is_palindrome("python"))   # Expected: False
print(is_palindrome("habibah"))  # Expected: True
