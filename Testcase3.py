# def ...(str1, str2):
def is_anagram(str1, str2):
    return sorted(str1) == sorted(str2)   # return ...

# Test
print(is_anagram("listen", "silent"))  # Expected: True
print(is_anagram("hello", "world"))    # Expected: False