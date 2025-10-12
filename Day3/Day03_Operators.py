# Day 3 - Operators
# 9 October 2025
"""
| + | Addition | 5+2 | 7 |
| - | Subtraction | 5−2 | 3 |
| * | Multiplication | 5∗2 | 10 |
| / | Division | 5/2 | 2.5 (Always returns a float) |
| // | Floor Division | 5//2 | 2 (Returns the integer part) |
| % | Modulo | 5%2 | 1 (Remainder after division) |
| ** | Exponentiation | 5∗∗2 | 25 |
==: Equal to
!=: Not equal to
>: Greater than
<: Less than
>=: Greater than or equal to
<=: Less than or equal to
"""
#----
"""
# Budget Calculator 

#Def Variables

initial_budget = float(input("Enter initial Budget: "))
expense_food = float(input("Enter food expense: "))
expense_travel = float(input("Enter travel expenses: "))

remaining_budget = initial_budget - expense_food - expense_travel

# Using floor division and modulo

ten_dollar_notes = remaining_budget // 10 # to check how many 10 dollar notes remanining
change_left = remaining_budget % 10 # returns the reminder after dividing by 10

print(f"Remaning Budget: ${remaining_budget}")
print(f"You have {ten_dollar_notes} ten dollars notes and ${change_left} change.")

# Comparison and Logical Operators

is_sufficient = remaining_budget > 100
is_safe_spending = (expense_food < 200) and (expense_travel < 250)

print(f"\nIs remanining budget sufficient (>100)? {is_sufficient}")
print(f"Was spending safe? {is_safe_spending}")
"""

#Operator Status Report 
#Self Project - Automated Progress Calculation and Status

total_days = 30
current_day = 3
score_today = 9
passing_score = 7
target_avg = 8

percent_complete = (current_day / total_days) * 100
days_remaining = total_days - current_day

average_score_required = (target_avg * total_days - score_today) / days_remaining

day_passed = score_today >= passing_score
is_on_track = (day_passed) and (percent_complete < 10)

print(f"Day Passed: {day_passed} and currently is on track: {is_on_track}")