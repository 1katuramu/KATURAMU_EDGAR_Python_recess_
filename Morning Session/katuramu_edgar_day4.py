# Dictionaries
# Creating and using dictionaries
# Dictionary methods and operations
"""_summary_
Dictionaries in python are collections of keys and values.
-Unordered
-mutable and
-indexed by keys
    """
# Example 1: Create a dictionary
# Create a dictionary for a student persuing software engineering, 
# the key must be your name, age, technology interest and year of study. put
# your own details

student_dict = {
    'name': 'Katuramu Edgar',
    'age': '23',
    'technology': 'AI',
    'course': 'BSSE',
    'year': '3'
}
print(student_dict['age'])
print(student_dict['technology'])

# Access values

# Modify Values:
# Execise 1: Modify age and technology

student_dict = {
    'name': 'Katuramu Edgar',
    'age': '27',
    'technology': 'App Development',
    'course': 'BSSE',
    'year': '3'
}
print(student_dict['age'])
print(student_dict['technology'])

# Example2: adding keys and values
student_dict['email'] = 'edgarkaturamu@gmail.com'
print(student_dict)

#Execrise remove a key and value from the dictionary
del student_dict['age']
print(student_dict)

# Common Dictionary methods
"""_summary_
get() // returns the value for the specified key if the key is in the dictionary. 
if not it returns the default value  

update() // Updates the dictionary with the elements from another dictionary

pop() // Removes the specified key and returns the corresponding value

    """
# Example 3: Use the get method
print(student_dict.get('technology'))

# Exercise 3: use the update method to change value in age
student_dict.update({'age' : '30'})

#pop method
student_dict = {
    'name': 'Katuramu Edgar',
    'age': '27',
    'technology': 'App Development',
    'course': 'BSSE',
    'year': '3'
}

student_dict.pop('age')

print(student_dict)

# Exercise 4: Use the if to check if the key 'age' is present in the dictionary

student_dict = {
    'name': 'Katuramu Edgar',
    'age': '27',
    'technology': 'App Development',
    'course': 'BSSE',
    'year': '3'
}

age_value = student_dict.get('age')
if age_value is not None:
    print("The key 'age' is present in the dictionary and its value is:", age_value)
else:
    print("The key 'age' is not present in the dictionary")
    
#keys(), values() and the items() methods
print(student_dict.keys())
print(student_dict.values())
print(student_dict.items())

"""_summary_
keys() returns a view of objects that displays a list of all keys
values() returns a view of objects that displays a list of all values
items() returns a view of objects that displays a list of dictionary keys and values in tuple pairs
    """
    
# Exrcise Use the update method to change course and add a new key "WhatsApp_Number" to the dictionary
student_dict = {
    'name': 'Katuramu Edgar',
    'age': '27',
    'technology': 'App Development',
    'course': 'BSSE',
    'year': '3'
}

student_dict.update({'course': 'BCS', 'WhatsApp_Number': '0785381550'})

print(student_dict)