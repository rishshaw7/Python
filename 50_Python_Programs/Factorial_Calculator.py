def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example: Calculate the factorial of 5
result = factorial(5)
print(result)  # Output: 120
