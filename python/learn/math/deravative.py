import sympy as sp


x = sp.symbols('x')

# f = int(input("what is your function: "))
f = x**3 - 3*x**6 + x + 5


f_prime = sp.diff(f, x)

print("Function:", f)
print("Derivative:", f_prime)