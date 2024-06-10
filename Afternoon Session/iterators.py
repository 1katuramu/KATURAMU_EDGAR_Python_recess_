# Python Iterators

# An iterator is an object that contains a countable number of values.
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
# Lists, tuples, dictionaries, and sets are all iterable objects.

mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

# Even strings are iterable objects, and can return an iterator
mystr = "banana"
myit = iter(mystr)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

# Looping Through an Iterator
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
  print(x)

# Iterate the characters of a string 
mystr = "banana"

for x in mystr:
  print(x)
  
# Create an Iterator
# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.)

class MyNumbers:
    # Define the iterator method
    def __iter__(self):
        # Initialize the counter variable
        self.a = 1
        # Return the iterator object
        return self

    # Define the next method
    def __next__(self):
        # Check if the counter has exceeded a certain value (e.g., 10)
        if self.a > 10:
            # Raise a StopIteration exception to signal the end of the iteration
            raise StopIteration
        else:
            # Get the current value
            x = self.a
            # Increment the value
            self.a += 1
            # Return the current value
            return x

# Create an instance of the MyNumbers class
myclass = MyNumbers()

# Iterate over the instance directly (no need to create an iterator object)
for num in myclass:
    print(num)
    




