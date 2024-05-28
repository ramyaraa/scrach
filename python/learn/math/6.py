#################   derivative   #############################

import sympy as sp


x = sp.symbols('x')

# f = int(input("what is your function: "))
f = x**3 - 3*x**6 + x + 5


f_prime = sp.diff(f, x)

print("Function:", f)
print("Derivative:", f_prime)



#################   integral   #############################


x = sp.symbols('x')

# f = int(input("what is your function: "))
f = x**3 - 3*x**2 + x + 5


indefinite_integral = sp.integrate(f, x)

definite_integral = sp.integrate(f, (x, 0, 1))

print("Function:", f)
print("Indefinite Integral (Antiderivative):", indefinite_integral)
print("Definite Integral from x=0 to x=1:", definite_integral)



#################   both   #############################

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

#################   limit   #############################



# Define the symbol
x = sp.symbols('x')

# Define the function
f = sp.sin(x) / x

# Compute the limit as x approaches 0
limit_at_zero = sp.limit(f, x, 0)

print("Function:", f)
print("Limit as x approaches 0:", limit_at_zero)

#################   double integral   #############################



# Define the function
def f(x, y):
    return x**2 + y**2

# Set up the limits for y: from 0 to 3
y_bounds = (0, 3)

# Set up the limits for x: from 0 to 2
x_bounds = (0, 2)

# Compute the double integral
result, error = sp.integrate.dblquad(f, x_bounds[0], x_bounds[1], lambda x: y_bounds[0], lambda x: y_bounds[1])

print("Double Integral over the region [0, 2]x[0, 3]:", result)
print("Error estimate:", error)
