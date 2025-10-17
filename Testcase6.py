# def ...(...):
def is_armstrong(n):
    return n == sum(int(d)**len(str(n)) for d in str(n))   # return ...

# Test
print(is_armstrong(153))  # Expected: True
print(is_armstrong(370))  # Expected: True
print(is_armstrong(123))  # Expected: False
