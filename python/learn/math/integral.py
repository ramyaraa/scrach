import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the function
f = x**3 - 3*x**2 + x + 5

# Compute the indefinite integral (antiderivative)
indefinite_integral = sp.integrate(f, x)

# Compute the definite integral from x=0 to x=1
definite_integral = sp.integrate(f, (x, 0, 1))

print("Function:", f)
print("Indefinite Integral (Antiderivative):", indefinite_integral)
print("Definite Integral from x=0 to x=1:", definite_integral)
