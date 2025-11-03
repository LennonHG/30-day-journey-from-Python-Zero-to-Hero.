# Self Project
# Converting JSON data to readable python dict/objects

import json

try:
    import json
    print("JSON imported")
except ImportError:
    print("JSON Failed to Import")
 
file_name = 'other_projects/sheets.json'


with open(file_name, 'r') as file:
    data_from_file = json.load(file)

#Getting the total number of ffedback, 13 total Feedback
total_feedback = len(data_from_file) 

#Identifying the available keys
initial_item_keys = list(data_from_file[0].keys())

def add_to_promptext(list):
    prompt_text = "" #Initial Starting point for the promptText
    for key, value in list:
        #print(f"{key}: {value}")
        prompt_text += key + ": " + str(value) + "\n"
    return prompt_text

promp_text = "Overall Feedback\n"

for index, item in enumerate(data_from_file, start=0):
    promp_text += str(f"Feedback {index+1}:\n") + add_to_promptext(item.items())
print(promp_text)






    

    











