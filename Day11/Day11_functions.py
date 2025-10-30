# Day 11, 30 October 2025 - Functions

"""
Definition: Functions are created using the keyword def, followed by the function name, and parentheses ().

Parameters: Variables listed inside the parentheses are the inputs the function accepts.

return: The return statement sends a value (or values) back to the calling code. If a function doesn't explicitly return a value, it implicitly returns None.

Call: Code executes only when the function is called (invoked by its name).
"""
"""
# Guided Project: The Simple Calculator
# Defining a function
def calculator_weekly_score(daily_score):
    #calculate score
    weekly_total = daily_score * 5
    return weekly_total

day_11_score = 10

#Calling the fucntion
total_score_this_week = calculator_weekly_score(day_11_score)

# Using the returned value for further computation
status_check = total_score_this_week >= 40 #boolean type

print(f"Daily Score: {day_11_score}")
print(f"Total Weekly Score (Returned Sum): {total_score_this_week}")
print(f"Met Target: {status_check}")
"""

# Self Project: Profile Generator 

# Defining the funciton 
def generate_status_line(user_name, days_complete, total_days):
    percent_completion = round((days_complete/total_days) * 100, 2) # round(number, ndigits)
    status_line = f"{user_name} is a Python Hero in Training: Day {days_complete} of {total_days} ({percent_completion}% completion)"
    return status_line

my_status = generate_status_line("Lennon G", 11, 30)

print(my_status)