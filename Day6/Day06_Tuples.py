#Day 6, 15 October 2025, 
#Tuples - Immutable Data Structure
#Tuples are immutable, ordered

"""
Tuples support indexing (accessing single items) and slicing (accessing a range).
They support basic built-in functions like len().
They have only two primary methods: .count(item) and .index(item).
"""

#Guided Project: Configuration Setter
"""
# 1. Define an immutable configuration of Tuples

file_config = ("/data/logs/app.log", 1024, "READ_ONLY", "HIGH")
print(f"Original Config: {file_config}")
print(f"File Path is: {file_config[0]}")
print(f"Total Elements: {len(file_config)}")

# 2. Type error

try:
    file_config[1] = 2024 # will cause a TypeError since tuples are immutable
    print("Configuration updated succesfully")
except TypeError:
    print("Tuples are immutable") 

#3. Tuples Methods
status_count = file_config.count("HIGH")
security_index = file_config.index("HIGH")
print(f"Status 'High' count: {status_count}")
print(f"Security Level Index: {security_index}")

#4. Tuple Unpacking 
path, max_size, status, security = file_config
print(f"Unpacked Variables: Status is {status}, Max Size is {max_size}")

"""

# Self Project: Immutable-Profile

# 1. Define Tuples
fixed_info = ("Lennon G", "Gemini", 6, 30)
print(f"My Fixed Info: {fixed_info}")

# 2. Unpacking Tuples
name, mentor, day, total_day = fixed_info
print(f"My name: {name}, My Mentor: {mentor}, current day: {day}, total number of days: {total_day}, Days remaining: {total_day - day}")

# 3. Converting Tuples to List() function
my_list = list(fixed_info)
print(f"My List: {my_list}")

# 4. List Conversion
my_list[1] = "GEMINI (AI)"
print(f"Updated Item: {my_list[1]}")
print(f"New Updated List: {my_list}")

# 5. Convert the list back into a tuple
updated_info = tuple(my_list)
print(f"Updated info tuple: {updated_info}")

# 6. Output

print(f"Fixed Info: {fixed_info}")
print(f"First two items of updated tuples: {updated_info[:2]}") #Not including index 2
print(f"Data type of new updated tuple: {type(updated_info)}")

