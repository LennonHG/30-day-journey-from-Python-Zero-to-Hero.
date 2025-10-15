#Day 7, 15 October 2025, Sets
"""
A Set is an unordered collection of unique, immutable objects. 
Their primary strength lies in ensuring that no duplicate elements exist and performing efficient 
membership testing and mathematical set operations.

2. Essential Set Operations (The Math)
Sets are often used to perform comparisons between two groups of data:
.union(other_set) or |: Returns a set containing all items from both sets.
.intersection(other_set) or &: Returns a set containing only the items present in both sets.
.difference(other_set) or -: Returns a set containing items from the first set that are not in the second set.

3. Set Methods (Adding and Removing)
Sets are mutable, meaning you can add or remove items:
.add(item): Adds a single item.
.remove(item): Removes a specified item. Raises a KeyError if the item is not found.
.discard(item): Removes a specified item. Does not raise an error if the item is not found (safer).
"""

#Guided Project: Data Sanitizer
"""
# 1. Definite a raw list with duplicates
raw_skills = ["Python", "Flask", "Python", "SQL", "SQL", "Data Science", "Flask"]
print(f"Original Items Count: {len(raw_skills)}")
print(f"List Items: \n{raw_skills}")

# 2. Converting raw_skills (list) into sets to remove duplicates
unique_skills = set(raw_skills)
print(f"Unique Skills: {unique_skills}")
print(f"Total number of unique Skills: {len(unique_skills)}")

# 3. Defining a 2nd set of skills
validated_skills = {"Python", "SQL", "Git"}

# 4. Sets operations
# Check which skils are not in the validated list

unvalidated_skills = unique_skills.difference(validated_skills) #Basically means unique skills - validates = return what left
print(f"Skills need validating: {unvalidated_skills}")

# Skills that we have 
common_skills = unique_skills.intersection(validated_skills) #When intersect, returns which has the same value in common between sets
print(f"Common SKills: {common_skills}")
                    
"""

# Self Project: Topic Manager
"""
Your independent assignment is to manage and compare the topics from the 30-day curriculum 
against an external list of popular tech topics.
"""
# 1. Define Sets
hero_topics = {"Dictionaries", "Conditionals", "Loops"}
popular_tech = {"AI Agents", "DevOps", "Docker", "Loops", "Big Data"}
mastered_topics = set()

# 2. Manipulation
def add_topics(topics_to_add):
    for topics in topics_to_add:
        mastered_topics.add(topics)


add_topics(["Lists", "Tuples", "Strings"])
print(f"{mastered_topics}")

# 3. Intersection between Hero Topics and Popular Tech

overlap = hero_topics.intersection(popular_tech)
print(f"The overlap between hero and tech: {overlap}\n")
future_focus = hero_topics.union(popular_tech)
print(f"Total unique areas of focus: {future_focus}\n")

# 4. Output

print(f"{mastered_topics}")
print(f"Lenght of Mastered Topics: {len(mastered_topics)}")
print(f"Union: {overlap}")



