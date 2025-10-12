#Day 2, 9 october 2025
# Variables and Built in Functions
# Python standard when delcaring variable is snake_case e.g snake_case
# len() and type()

#studen profile
"""
name = "Lennon"
age = 29
status = True #True or False start with a capital letter

name_length = len(name)
age_type = type(age)
status_type = type(status)

print(age)
print(age_type)

print(f"Name: {name}, (Length: {name_length}) ")
print(f"current age: {age}, (age tyep: {age_type})")
print(f"currently learning Pything? {status}, (status type: {status_type})")
"""

# Self Project: progress_report

curriculum_name = "30 Day Python"
days_completed = 2
percent_complete = 6.67
"""
#Refactored code for percent complete
days_completed = 2
total_days = 30 # New variable for clarity
percent_complete = (days_completed / total_days) * 100 # Calculation using operators!
"""
status_emoji = "✅"

curriculum_name_length = len(curriculum_name)
percent_complete_type = type(percent_complete)

# Display variables

print(f"--- {curriculum_name} Progress --")
print(f"Days Completed {days_completed}/30 {status_emoji}")
print(f"Progress {percent_complete}% completed")
print(f"\n{curriculum_name} Length: {curriculum_name_length} ")
print(f"Type of 'percent_complete: {type(percent_complete)}")