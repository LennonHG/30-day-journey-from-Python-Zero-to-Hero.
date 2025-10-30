# Day 12, 30 october 2025, Modules

"""
A Module is essentially a Python file (.py) containing reusable code—functions, classes, and variables. 
Modules allow you to leverage Python's vast Standard Library (pre-installed tools) and third-party libraries
"""
# Python's Built in module
# math, random, os

# Guided Project: Math Utility, find the area of a circle TTr2 = 169

import math # import the standardize math library
import random #Import the standardize random library

# Declare Variables
"""
area_of_square = 169
radius = 4 

# 1. Using math.sqrt() to get the square root

side_length = math.sqrt(area_of_square)

# 2. Calculating Area of a circle, Area=π×r2

area_of_circle = math.pi * (radius ** 2) 

print(f"Side length of a square with area {area_of_square}: {side_length}")
print(f"Area of a circle with {radius}: {round(area_of_circle, 2)}")
"""

#Self Project: Random ID Generator

def generate_unique_id(status_code):
    base_string = "LG_D12"
    random_integer = random.randint(1000, 9000)
    random_status_code = random.choice(status_code)
    unique_id = f"{base_string}-{random_integer}-{random_status_code}"
    return unique_id

status_code_list = ["STABLE", "BETA", "ALPHA", "TESTING"]
print(f"Returned ID: {generate_unique_id(status_code_list)}")