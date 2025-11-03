#Converting JSON to Dictionaries in Python
# JSON vs. Python Dictionaries
"""
JSON (JavaScript Object Notation) and Python Dictionaries are 
both ways to store data in a structured, key-value pair format.
"""

"""
Available Key Functions with JSON

jsom.dumps() Dictionary -> JSON String # Converts a python(py) dictionary/object into a JSON formatted String
json.load() JSON File -> Dictionary # Reads a JSON doc from a file-like object (like and open file) and converts it into dictionary
json.loads() JSON String -> Dictionary # Parses a JSON formatted Sstring and converts it into a python dictionary/object
json.dump() Dictionary -> JSON File # Write python dict/object into JSON formatter file
"""

import json
# Check if JSON is imported

try:
    import json
    print("Imported")
except ImportError:
    print("Not imported")

# Convert Dictionary to JSON String (Encode)
data_dict = {'user_id': 101, 'user_name': 'physcis', 'active':True, 'url': "Google"}
json_string = json.dumps(data_dict, indent=4) #use indent for pretty-printing

print("\n--- Dictionary to String -- ")
print(f"\n{type(json_string)}")
print(f"\n{json_string}")

# JSON String to Dictionary (Decoding)

new_dict = json.loads(json_string)

print(type(new_dict))
print(new_dict)
print(new_dict['user_name']) #access data like normally in a dictionary
print(new_dict['active'])
print(new_dict['user_id'])

# Reading/Writing to a file
# Creates the variable which will store the filename
file_name = 'config.json'

#Writing to file (dump)
# With Statement ensures the files closes after block finishes (even with errors)
with open(file_name, 'w') as file: #open(fila_name, 'w') in write mode, if file does not exist, creates, if exists, overwrites, as File, assigned the file object to 'file'
    json.dump(data_dict, file, indent=4) #Converts the dict into JSON text and writes it directly into the FILE with indent 4.

# Reading from a file
with open(file_name, 'r') as file:  #'r' open the file in read mode
    data_from_file = json.load(file) #Load the file JS

print(data_from_file)
print(f"URL:{data_from_file['url']}")

#Data Manipulation

complex_data = {
    'employess': [{'name': 'Jane', 'dept': 'HR'}, {'name': 'Jake', 'dept': 'Operations'}],
    'office':{'city': 'New York'}
}

jane = complex_data['employess'][0]
current_office = complex_data['office']['city']
print(f"Name: {jane['name']}, Dept: {jane['dept']}")
print(f"Current Office: {current_office}")

# Modifying data

complex_data['office']['city'] = 'Kuala Lumpur'
current_office = complex_data['office']['city']
print(f"Current Office: {current_office}")


#Adding a new top-level-key
complex_data['date'] = '2025-11-23'
print(complex_data['date'])

#Adding a new key to an employee
complex_data['employess'][0]['salary'] = 90000
print(complex_data['employess'])