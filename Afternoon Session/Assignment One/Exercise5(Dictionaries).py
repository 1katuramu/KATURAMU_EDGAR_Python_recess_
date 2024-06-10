# 1. Dictionary definition
Shoes = {
    "brand": "Nick",
    "color": "black",
    "size": 40
}

# 1. Print the value of the shoe size
print("Shoe size:", Shoes["size"])

# 2. Change the value "Nick" to "Adidas"
Shoes["brand"] = "Adidas"
print("Updated brand:", Shoes["brand"])

# 3. Add a key/value pair "type": "sneakers" to the dictionary
Shoes["type"] = "sneakers"
print("Updated dictionary:", Shoes)

# 4. Return a list of all the keys in the dictionary
print("Keys:", list(Shoes.keys()))

# 5. Return a list of all the values in the dictionary
print("Values:", list(Shoes.values()))

# 6. Check if the key "size" exists in the dictionary
if "size" in Shoes:
    print("Key 'size' exists in the dictionary")

# 7. Loop through the dictionary
for key, value in Shoes.items():
    print(f"{key}: {value}")

# 8. Remove "color" from the dictionary
del Shoes["color"]
print("Updated dictionary after removing 'color':", Shoes)

# 9. Empty the dictionary
Shoes.clear()
print("Empty dictionary:", Shoes)

# 10. Create a new dictionary and make a copy of it
new_dict = {"name": "John", "age": 30}
copy_dict = new_dict.copy()
print("Original dictionary:", new_dict)
print("Copied dictionary:", copy_dict)

# 11. Show nested dictionaries
nested_dict = {"person": {"name": "Jane", "age": 25}, "address": {"city": "New York", "state": "NY"}}
print("Nested dictionary:", nested_dict)