# Day 5
# 11 October 2025
# List and List methods - Mutable
"""
.append(item): Adds a single item to the end of the list.

.insert(index, item): Adds an item at a specific position.

.remove(item): Removes the first occurrence of a specified value.

.pop(index): Removes and returns the item at a specific index (or the last item if no index is given).

.sort(): Sorts the list in place.

"""

#Guided Project  - Task Manager
"""
def print_list():
    print(f"Initial List: {todo_lists}")

#1. Initial Task 
todo_lists = ["Compete Day 4 Project", "Review Strings Theory", "Plan Day 5"]
#print(f"Initial List: {todo_lists}")
print_list()

#2. Add Task
todo_lists.append("Start Day 5 Self-Project")
todo_lists.insert(0, "Daily Standup")
print_list()

#3. Demo Mutability
todo_lists[2] = "Review Strings Theory (Done)"
print_list()

#4. Remove task (using pop() to 'complete' the last task)

completed_task = todo_lists.pop()
print(f"Completed Task (Remove): {completed_task}")
print(f"Final List: {todo_lists}")
"""


# Self Project - Skills Trackers

#1. Initializing List
core_skills = ["Variables", "Operators", "Strings", "Lists"]
future_skills = ["AI Agents", "Web Scraping", "API"]
full_curriculum = core_skills + future_skills
full_curriculum.append("Functions")
full_curriculum.sort()

print(f"{full_curriculum}")

#2. Modifying List
"""
updated_core_skills = core_skills[2]
updated_core_skills = updated_core_skills + " " + "(MASTERED)"
core_skills[2] = updated_core_skills
"""
core_skills.insert(2, "MASTERED")
remove_skill = core_skills.pop(0) #removing the first item
remove_skill = "Mastered Skills"

print(f"Full Curiculum List: {full_curriculum}")
print(f"Last two Skills: {full_curriculum[-2:]}")


