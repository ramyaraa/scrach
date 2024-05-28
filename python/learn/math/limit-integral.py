import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the function
f = sp.sin(x) / x

# Compute the limit as x approaches 0
limit_at_zero = sp.limit(f, x, 0)

print("Function:", f)
print("Limit as x approaches 0:", limit_at_zero)
