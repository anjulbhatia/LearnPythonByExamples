# This program calculates the simple interest based on user inputs.
# It introduces the use of basic mathematical operations.

p = float(input("Enter Principal Amount (P): "))
r = float(input("Enter Rate of Interest (R): "))
t = float(input("Enter Time (T) in years: "))

print('''
Formula: 
          P * R * T
    SI = -----------
             100      
''')

si = (p * r * t) / 100

print("Simple Interest (SI) =", si)
print("Total Amount (Principal + SI) =", p + si)