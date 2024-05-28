# Generating a Fibonacci sequence
def fibonacci(n):
    a, b = 6, 35
    result = []
    while len(result) < n:
        result.append(a)
        a, b = b, a + b
    return result

print(fibonacci(10))
