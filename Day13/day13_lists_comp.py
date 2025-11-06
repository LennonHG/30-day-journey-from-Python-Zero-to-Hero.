# Day 13, 30 October 2025, List Comprehensions (LCs)

# [expression for item in list if condition]

# Guided Project: Unit Converter

#Input list
mile_distance = [5, 10, 13.1, 26.2]

#1 mile = 1.61km


#Declare New List
new_km_list = []
# Traditional For Loop
for mile in mile_distance:
    new_km_list.append(round(mile * 1.61, 1))
print(f"New Converted List in KM: {new_km_list}")
print(f"Old list: {mile_distance}")

# List Comprehension

new_lc_km_list = [round(mile * 1.61, 2) for mile in mile_distance]
print(f"New KM list with LC: {new_lc_km_list}")

# Self Project: Topic Filter
#Def a dictionary
day_scores = {
    "Strings": 10,
    "Lists": 9,
    "Tuples": 10,
    "Sets": 8
}

unpack_score = day_scores.items()
print(unpack_score)

#Core 1: Transformation
all_score = [value + 1 for key, value in unpack_score]

#Core 2: Filtering
review_topics = [key for key, value in unpack_score if (value < 9) ]


#output
print(f"All Scores List: {all_score}")
print(f"Review Topics: {review_topics}")
print(f"You can do it!! You have only {len(review_topics)} topic to review")