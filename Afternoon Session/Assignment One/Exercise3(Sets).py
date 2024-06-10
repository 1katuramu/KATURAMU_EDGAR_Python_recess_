# 1. Use the set() constructor to create a set of 3 of your favorite beverages
beverages = set(["Coffee", "Tea", "Juice"])

# 2. Use the correct method to add 2 more items to the beverages set
beverages.update(["Soda", "Water"])
print("Updated beverages set:", beverages)

# 3. Given the set below;
mySet = {"oven", "kettle", "microwave", "refrigerator"}

# Check if microwave is present in the set
if "microwave" in mySet:
    print("Microwave is present in the set")
else:
    print("Microwave is not present in the set")

# 4. Write a python program to remove “kettle” from the set above
mySet.remove("kettle")
print("Updated set:", mySet)

# 5. Write a python program to loop through the set above
print("Looping through the set:")
for item in mySet:
    print(item)

# 6. Write a set of 4 items and a list of two items. Write a python program to add elements in the list to elements in the set
set_items = {"Apple", "Banana", "Cherry", "Date"}
list_items = ["Elderberry", "Fig"]
set_items.update(list_items)
print("Updated set:", set_items)

# 7. Write two sets, one containing your ages and the other your first names. Join the two sets
ages = {25, 30, 35, 40}
names = {"John", "Jane", "Jim", "Jenny"}
combined_set = ages.union(names)
print("Combined set:", combined_set)