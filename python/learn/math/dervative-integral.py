import sympy as sp

# Define the symbol
x = sp.symbols('x')

# Define the function
f = sp.sin(x**2)

# Compute the first derivative
f_prime = sp.diff(f, x)

# Compute the indefinite integral
indefinite_integral = sp.integrate(f, x)

# Solve for x where the derivative is zero
critical_points = sp.solveset(f_prime, x, domain=sp.S.Reals)

print("Function:", f)
print("First Derivative:", f_prime)
print("Indefinite Integral (Antiderivative):", indefinite_integral)
print("Critical Points (f'(x) = 0):", critical_points)
