# This program asks the user to input the radius of a circle and calculates its area.
# We will use math.pi here for a more precise value of π.

import math

radius = float(input('Enter radius of circle: '))
area = round(math.pi * radius**2, 2)

print('Area of a circle with radius', radius, 'is', area)