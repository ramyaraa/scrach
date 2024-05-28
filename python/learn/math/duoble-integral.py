from scipy import integrate
import numpy as np

# Define the function
def f(x, y):
    return x**2 + y**2

# Set up the limits for y: from 0 to 3
y_bounds = (0, 3)

# Set up the limits for x: from 0 to 2
x_bounds = (0, 2)

# Compute the double integral
result, error = integrate.dblquad(f, x_bounds[0], x_bounds[1], lambda x: y_bounds[0], lambda x: y_bounds[1])

print("Double Integral over the region [0, 2]x[0, 3]:", result)
print("Error estimate:", error)
