#Day 17, Exception Handling, 29 November 2025

#Theory
#try , except, else and finally

"""
An Exception is an error that occurs during the execution of a program. 
Exception handling allows you to manage these errors gracefully.
try: The block of code that might raise an exception is placed here.
except [ErrorType]: The block of code that executes if the specified ErrorType occurs in the try block. 
You can catch specific errors (e.g., ZeroDivisionError) or all errors.
else: The block of code that executes only if the try block completes successfully (i.e., no exception was raised).
finally: The block of code that always executes, 
regardless of whether an exception occurred or not (often used for cleanup, like closing files).
"""

#Basic Structure
from typing import Type

"""
#user_input = int(input("Please input a number: "))
try: 
    #code that might cause an error
    result = 10 / 0
except ZeroDivisionError:
    #code to execute if ia ZeroDivisionError
    result = 0
    print("Error: Cannot divide by 0")
else:
    # Executes only if the try block was successful
    print("Calculation was succesful")
finally: 
    # Always executes (for cleanup, logging)
    print("Execution attempt complete")

# Guided Project: "Safe Divider"

def safe_divide(numerator, denominator):
    try:
        result = numerator / denominator
    except ZeroDivisionError:
        # Handles the specific error gracefully:
        print("Operation failed: Division by zero is not allowed")
        return None
    except TypeError:
        print("Operation Failed: Both input must be numbers")
        return None
    else:
        print("Division Successful")
        return result

#Test Cases
print(f"Result 1 (Success): {safe_divide(10,2)}")
print(f"--" * 20)
print(f"Results 2 (ZeroDivisionError): {safe_divide(10, 0)}")
print(f"--" * 20)
print(f"Results 3 TypeError: {safe_divide(3, "f")}")
"""

# Self Project: The Zero-to-Hero Profile Updater

#1.  Definin a dictionary
user_profile = {
    "name": "Lennon",
    "score": 9,
    "days": 17
}

#2. Defining update score function
def update_score (profile_dict, new_score_input):
    try:
        current_score = profile_dict["score"]
        profile_dict["score"] = int(new_score_input)
    except ValueError:
        print("Error: Score must be a numberical digit (0-10)")
    except KeyError:
        print(f"Fatal: The {new_score_input} key is missing from the profile dictionary")
    else:
        print(f"Score was updated to {new_score_input}")

update_score(user_profile, "10")
update_score(user_profile, "ten")

test_profile = user_profile.copy()
test_profile.pop('score')

update_score(test_profile, "10")

print(user_profile)