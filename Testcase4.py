# def ...(...):
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)   # return ...

# Test
print(factorial(5))  # Expected: 120
print(factorial(0))  # Expected: 1
