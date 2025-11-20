#Day 14, High Order Functions
#8th November 2025

# E.g map() or filter()
#HOF - takes functions as param or return function as parameters

"""
#map(function, iterable)
applies the function to every item in iterable and returns a 
a map (usually converts to a list)

use case: Transforming data (e.g convert all to uppercase)
"""
"""
#filter(function, iterable)
returns a filtered object containing only the item that returns True

use case: Selecting a subset of data (e.g finding only positive number)
"""

"""
#Lambda - No definition (Anonymous function)
use immediately as a HOF
# Lambda: input x, output is x * 2

"""

# Defining a list
raw_numbers = [2,5,8,11,15,20]

# 1. Map with Lambda (Transformation)
# Lambda: input x, output is x * 2
doubled_numbers = list(map(lambda x: x*2, raw_numbers)) 
# map(expression, iterable), lambda input: expression
print(f"Mapped (Doubled): {doubled_numbers}")

# 2. Filter with Lambda (Selection)
# Lambda input x: output is True if x > 15, False otherwise
high_scores = list(filter(lambda x: x > 15, doubled_numbers))
print(f"Filtered (>15): {high_scores}")

# Self Project: hof scorer

scores = [10,9,10,8]
# Task 1 - Transformation
bonus_score = list(map(lambda x: round(x * 1.1,2), scores))
print(f" Bonus Score (10%): {bonus_score}")

# Task 2 - Filter
needed_improvmenet = list(filter(lambda x:x<10, scores))
print(f"Scores needing improvement: {needed_improvmenet}")

