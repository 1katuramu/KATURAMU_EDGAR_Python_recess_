# Create a list of names with 5 items
names = ["Jane", "John", "Jade", "Joe", "Jim"]

# 1. Print the 2nd item in the list, which is at index 1 (since indexing starts at 0)
print("The 2nd item is:", names[1])

# 2. Change the value of the first item to "Jennifer"
names[0] = "Jennifer"
print("Updated list after changing the first item:", names)

# 3. Add a sixth item to the list
names.append("Jasmine")
print("Updated list after adding a sixth item:", names)

# 4. Insert "Bathel" as the 3rd item in the list
names.insert(2, "Bathel")
print("Updated list after adding 'Bathel' as the 3rd item:", names)

# 5. Remove the 4th item from the list
del names[3]
print("Updated list after removing the 4th item:", names)

# 6. Print the last item in the list using negative indexing
print("The last item is:", names[-1])

# 7. Create a new list with 7 items
colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]

# Use a range of indexes to print the 3rd, 4th, and 5th items
print("The 3rd, 4th, and 5th items are:", colors[2:5])

# 8. Write a list of countries and make a copy of it
countries = ["USA", "Canada", "Mexico", "UK", "France", "Germany", "Italy"]
countries_copy = countries.copy()
print("Original list of countries:", countries)
print("Copied list of countries:", countries_copy)

# 9. Write a python program to loop through the list of countries
print("Looping through the list of countries:")
for country in countries:
    print(country)

# 10. Write a list of animal names
animals = ["Lion", "Elephant", "Kangaroo", "Aardvark", "Antelope", "Zebra", "Cat", "Dog"]

# Sort the list in ascending order
animals.sort()
print("Sorted list in ascending order:", animals)

# Sort the list in descending order
animals.sort(reverse=True)
print("Sorted list in descending order:", animals)

# 11. Output only animal names with the letter 'a' in them
animals_with_a = [animal for animal in animals if 'a' in animal.lower()]
print("Animal names with the letter 'a' in them:", animals_with_a)

# 12. Write two lists, one containing first names and the other second names
first_names = ["John", "Jane", "Jim", "Jenny"]
second_names = ["Doe", "Smith", "Johnson", "Williams"]

# Join the two lists
full_names = [f"{first} {second}" for first, second in zip(first_names, second_names)]
print("Full names:", full_names)
