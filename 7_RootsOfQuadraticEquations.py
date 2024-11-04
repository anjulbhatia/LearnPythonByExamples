# This program asks the user to enter the values of a, b, and c for a quadratic equation.
# It calculates the discriminant and finds the roots based on its value.
# We'll use if-else statements to check the nature of the roots.

import math

# Get coefficients from the user
a = float(input("Enter the coefficient of x^2 (a): "))
b = float(input("Enter the coefficient of x (b): "))
c = float(input("Enter the constant term (c): "))

# Display the equation in standard form
sign_b = '+' if b >= 0 else ''
sign_c = '+' if c >= 0 else ''
print(f"Equation: {a}x^2 {sign_b} {b}x {sign_c} {c} = 0")

# Calculate the discriminant
D = b**2 - 4*a*c

# Display the formula used
print('''
Formula:
      a * x^2 + b * x + c = 0

      D = b^2 - 4 * a * c

      Roots:
            -b ± sqrt(D)
      x =  ------------
              2 * a
''')

# Check the nature of the discriminant and calculate roots
if D > 0:
    # Two real and distinct roots
    root1 = (-b + math.sqrt(D)) / (2 * a)
    root2 = (-b - math.sqrt(D)) / (2 * a)
    print("The equation has two real and distinct roots:")
    print("Root 1 =", root1)
    print("Root 2 =", root2)
elif D == 0:
    # One real root (repeated)
    root = -b / (2 * a)
    print("The equation has one real repeated root:")
    print("Root =", root)
else:
    # Complex roots
    real_part = -b / (2 * a)
    imaginary_part = math.sqrt(-D) / (2 * a)
    print("The equation has two complex roots:")
    print("Root 1 =", real_part, "+", imaginary_part, "i")
    print("Root 2 =", real_part, "-", imaginary_part, "i")
