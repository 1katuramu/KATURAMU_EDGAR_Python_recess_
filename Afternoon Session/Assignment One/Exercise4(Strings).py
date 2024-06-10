# 1. Declare two variables, an integer and a string and use the correct method to concatenate the two variables
num = 5
str_VAR = "Hello"
print("Concatenated string:", str_VAR + str(num))

# 2. Consider the example below;
txt = "      Hello,       Uganda!       "

# Output the string without spaces at the beginning, in the middle, and at the end
print("String without spaces:", txt.strip())

# 3. Write a python program to convert the value of 'txt' to uppercase
print("Uppercase string:", txt.upper())

# 4. Write a python program to replace character 'U' with 'V' in the string above
print("String with 'U' replaced by 'V':", txt.replace('U', 'V'))

# 5. Using the code below, write a python program to return a range of characters in the 2nd, 3rd, and 4th position
y = "I am proudly Ugandan"
print("Range of characters in 2nd, 3rd, and 4th position:", y[1:4])

# 6. The piece of code below will give an error when output;
x = 'All "Data Scientists" are cool!'  # Use single quotes to enclose the string
print("Corrected string:", x)