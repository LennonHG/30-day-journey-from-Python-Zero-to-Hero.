#Day 15, Type Error
"""
TypeError
IndexError
keyError
"""
from curses.ascii import isdigit

#Guided Project: Error Investigator

profile = {
    "day": 15,
    "score": 9.5
} #Dictionary
sequence = [1,2,3] # List

# 1. Type Error (Bug: Trying to add a string and a number directly)
print("Current Day: " + str(profile["day"]))

# 2. Key Error (Bug: The key is "Score", not "score")
current_score = (profile["score"])

# 3. Index Error (Bug: List length is 3, highest index is 2)
last_item = sequence[2
]

print(f"Final Check: {profile["day"]}, Current Score: {current_score}, Last Item: {last_item}")


#Self Project: Robust Processors

raw_grades = [10, "9", 8.5, "Error", 9.2, 7, -2, "-2"]

def safe_grade_calculator(lists):
    clean_grades = [] #Defining an empty lists
    for grade in lists: #Loop through the lists
        if isinstance(grade, (int, float)):
            clean_grades.append(grade)
        elif grade.isdigit():
            clean_grades.append(int(grade))
        continue
    safe_average = sum(clean_grades)/len(clean_grades)
    return round(safe_average,2)

print(f"Safe Average: {safe_grade_calculator(raw_grades)}")