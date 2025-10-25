# Day 8, 25 October 2025 
# Dictionaries - Key-Value Pairs

"""
A Dictionary is an unordered, changeable collection of data values that stores data in 
key: value pairs. It is Python's most powerful way to model real-world entities 
(like a user profile, a database record, or a configuration file).
"""
"""
Methods
.keys(): Returns a list-like view of all keys.
.values(): Returns a list-like view of all values.
.items(): Returns a list-like view of (key, value) tuples.
.pop(key): Removes the item with the specified key.

Accesing data
my_dict["Key"] #if key is not found, it will raise a keyError
.get(key, default) # returns none or default if not found

my_dict["Keys"] = new_value # Updating values

"""

# Guided Project: "User Profile Manager"

# 1. Initialze user profile
"""
user_profile = {
    "username": "lennon g",
    "status": "Hero-in-training",
    "days_completed": 7,
    "last_topic": "Sets"
}

print(f"Initial Keys: {user_profile.keys()}")

# 2. Accessing Values
current_status = user_profile["status"]
print(f"Current Status: {current_status}")

# 3. Modification and Addition
user_profile["days_completed"] = 8 # updating days completed to 8
user_profile["programming_language"] = "Python"
print(f"\n3. Modification and Addition")
print(f"Updated profile: {user_profile}")

# 4. Removal

removed_topic = user_profile.pop("last_topic")
print(f"Removed Topic: {removed_topic}")
print(f"Keys after removal: {user_profile.keys()}")
"""

# Self-Project Zero to Hero Topic Picker 

# 1. Initialize Dictionary
day_scores = {
    "Strings": 10,
    "Lists": 9,
    "Tuples": 10,
    "Sets": 9
}

# 2. Manipulation

day_scores["Dictionaries"] = 0
day_scores["Strings"] = 10

# 3. Removal/ Extraction

new_list = list(day_scores.keys()) # Convert the keys found in day_score into a list using list() method
print(f"New List: {new_list}")

# 4. Output

print(f"Final Dictionary: {day_scores}")
print(f"Last item in the list: {new_list[-1:]}")
print(f"Tuples Score: {day_scores.get("Tuples", "Not found")}")