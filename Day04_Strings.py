#Day 4
#10 October 2025
#Strings - Manipulating Text Data
"""
#1. Messy input quote
messy_quoate = "  Mastering Python is 30 days of consistent effort.  "

#2. Cleaning the string
cleaned_quoate = messy_quoate.strip()
print(f"Cleaned Quoate: '{cleaned_quoate}' ")

#3. Slicing and Indexing
first_five = cleaned_quoate[0:5] #Extracting Maste
last_five = cleaned_quoate[-6:-1] #Extracting ffort

print(f"First 5 chars: {first_five}")
print(f"Last 5 chars: {last_five}")

# 4. Using split() and accessing the first word
words = cleaned_quoate.split(' ')
print(words)
first_word = words[0].upper()
print(f"First Words (UPPERCASE): {first_word}")
print(f"Total Words: {len(words)}")
"""

#Credentials Generator

user_full_name = "Lennon Ginibun"
primary_goal = "To master Python in 30 days and buil AI Agents, and Web scrapping."

goal_id = primary_goal.upper().replace(" ", "_")
first_two_ch = user_full_name[0:2] #le
last_two_ch = user_full_name[-2:] # G

username = first_two_ch + last_two_ch + str(len(primary_goal.split(' ')))
print(f"GOAL_ID: {goal_id}")
print(f"User ID: {username}")
print(f"user full name: {user_full_name.title()}")