def check_number(n):
    return "The number is Positive" if n > 0 else "The number is Negative" if n < 0 else "The number is Zero"
print(check_number(10))   # Expected: Positive
print(check_number(-5))   # Expected: Negative
print(check_number(0))    # Expected: Zero
