# 1. Consider the tuple below;
x = ("samsung", "iphone", "tecno", "redmi")

# Output your favorite phone brand (assuming it's the first item)
print("My favorite phone brand is:", x[0])

# 2. Use negative indexing to print the 2nd last item in your tuple
print("The 2nd last item is:", x[-2])

# 3. Update "iphone" to "itel"
x = list(x)  # Convert tuple to list
x[1] = "itel"
x = tuple(x)  # Convert list back to tuple
print("Updated tuple:", x)

# 4. Add "Huawei" to your tuple
x = list(x)  # Convert tuple to list
x.append("Huawei")
x = tuple(x)  # Convert list back to tuple
print("Updated tuple:", x)

# 5. Loop through the tuple
print("Looping through the tuple:")
for phone in x:
    print(phone)

# 6. Remove/delete the first item in your tuple
x = list(x)  # Convert tuple to list
del x[0]
x = tuple(x)  # Convert list back to tuple
print("Updated tuple:", x)

# 7. Create a tuple of cities in Uganda
cities = tuple(["Kampala", "Entebbe", "Jinja", "Mbale", "Gulu"])

# 8. Unpack your tuple
city1, city2, city3, city4, city5 = cities
print("Unpacked cities:", city1, city2, city3, city4, city5)

# 9. Use a range of indexes to print the 2nd, 3rd and 4th cities
print("Cities 2-4:", cities[1:4])

# 10. Write two tuples, one containing first names and the other second names. Join the two tuples.
first_names = ("John", "Jane", "Jim", "Jenny")
second_names = ("Doe", "Smith", "Johnson", "Williams")
full_names = tuple(zip(first_names, second_names))
print("Full names:", full_names)

# 11. Create a tuple of colors and multiply it by 3
colors = ("Red", "Green", "Blue")
colors_tripled = colors * 3
print("Colors tripled:", colors_tripled)

# 12. Return the number of times 8 appears in this tuple
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
count = thistuple.count(8)
print("Number of times 8 appears:", count)