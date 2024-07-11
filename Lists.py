# Creating Lists
empty_list = []
fruits = ["apple", "banana", "cherry"]

# Accessing List Elements
first_fruit = fruits[0]
last_fruit = fruits[-1]

# Modifying List Elements
fruits[0] = "avocado"

# Appending Elements
fruits.append("date")

# Inserting Elements
fruits.insert(1, "blueberry")

# Removing Elements
fruits.remove("banana")
popped_fruit = fruits.pop()

# Length of a List
length_of_fruits = len(fruits)

# List Slicing
first_two_fruits = fruits[0:2]
from_second_to_last_fruit = fruits[1:]
all_fruits = fruits[:]

# List Comprehensions
squares = [x ** 2 for x in range(1, 6)]
evens = [x for x in range(10) if x % 2 == 0]

# Common List Methods
numbers = [1, 2, 3, 4, 5]
numbers.append(6)
numbers.insert(0, 0)
numbers.remove(3)
popped_number = numbers.pop()
numbers.clear()

# Restore the numbers list
numbers = [1, 2, 3, 4, 5]

# Using other list methods
index_of_four = numbers.index(4)
count_of_twos = numbers.count(2)
numbers.sort(reverse=True)
numbers.reverse()
shallow_copy = numbers.copy()

# Example Output
print("Empty List:", empty_list)
print("Fruits List:", fruits)
print("First Fruit:", first_fruit)
print("Last Fruit:", last_fruit)
print("Modified Fruits List:", fruits)
print("Popped Fruit:", popped_fruit)
print("Length of Fruits List:", length_of_fruits)
print("First Two Fruits:", first_two_fruits)
print("From Second to Last Fruit:", from_second_to_last_fruit)
print("All Fruits:", all_fruits)
print("Squares List:", squares)
print("Evens List:", evens)
print("Numbers List after Operations:", numbers)
print("Index of 4 in Numbers:", index_of_four)
print("Count of 2 in Numbers:", count_of_twos)
print("Shallow Copy of Numbers:", shallow_copy)
