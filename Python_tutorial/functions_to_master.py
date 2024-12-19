# Print 

age = 38
name = "John"

print(f" My name is {name} and I'm {age} years old ")
print("My name is", name, "and I'm", age, "years old", sep="|")
print("Hello")
print("World")

print("Hello", end=" ")
print("World")

# Help 

# help(print)

# Range 

rng = range(10)

print(rng)
print(list(rng))

rng_2 = range(2, 10)
print(list(rng_2))

rng_3 = range(2, 10, 2) # The last one acts as the step value
print(list(rng_3))

# Map
# The map function allows us to apply a function to every single item in an iterable object

strings = ["my", "world", "apple", "pear"]

lenghts = map(len, strings) # We can pass our own function or any function as a first parameter
print(list(lenghts))

lenghts2 = map(lambda x: x + "s", strings)
print(list(lenghts2))

def add_s(string): 
    return string + "s"

lenghts3 = map(add_s, strings)
print(list(lenghts3))

# Filter --> related to the map function. If that funcion returns true, it will keep the item. Otherwise it will remove it. 

def longer_than_4(string):
    return len(string) > 4

filtered = filter(longer_than_4, strings)
print(list(filtered))

filtered2 = filter(lambda x: len(x) > 4, strings)
print(list(filtered2))

# Sum function 

numbers = {1, 2, 3, 4, 5, 24, 4.5}
print(sum(numbers))

# You can also pass a start value
print(sum(numbers, start=10))

# Sorted function will sort an iterable object in an ascending or descending order

numbers2 = [4, 5, 2, 3, -1, 0, 9]
sorted_nums = sorted(numbers2)
print(sorted_nums)

sorted_nums2 = sorted(numbers2, reverse=True)
print(sorted_nums2)

# We can also pass a a python function using the key argument
# It will apply this function to every single item of the iterable object

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 20}
]

sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)

sorted_people2 = sorted(people, key=lambda person: person["age"], reverse=True)
print(sorted_people2)

# Enumerate function 

# First, take a look at what happens if we don't use it:

tasks = ["Write report", "Attend meeting", "Review code", "Submit timesheet"]

for index in range(len(tasks)):
    task = tasks[index]
    print(f"{index + 1}. {task}")
    
# Using the enumerate function we can clear the code: 
  
for index, task in enumerate(tasks):
    print(f"{index + 1}. {task}")
    
# The zip function 

names = ["Alice", "Bob", "Daniel", "David", "Tim"] # It doesn't include Tim because we don't have a corresponding age
ages = [30, 25, 35, 20]
gender = ["Female", "Male", "Male"]

for idx in range(min(len(names), len(ages))): # Calcula quants elements es poden processar basant-se en la llista més curta.
    name = names[idx]
    age = ages[idx]
    print(f"{name} is {age} years old")
    
# The zip function combines different iterable objects

combined = list(zip(names, ages))
print(combined)

for name, age in combined:
    print(f"{name} is {age} years old")

combined2= list(zip(names, ages, gender))
print(combined2)

for name, age, gender in combined2:
    print(f"{name} is {age} years old and is {gender}") # It will only print out 3 names
    
# Open function 

# We can open a file, read from it, write to it... 

file = open("test.txt", "w") # The second option is the file mode
file.write("Hello world\nmy name is Guillem")
file.close() #So we don't  have any memory leaks and we don't leave the file open in memory when we actually don't mean to do that.  
# r stands for read
# w stands for write. Will override a file if it already exist
# a stands for append

# Instead of opening it and closing it like that, it is recommended to use the following syntax:
# Using context manager: 

with open("test.txt", "w") as file: 
    file.write("here") # Will automatically handle closing the file for us
    
with open("test.txt", "r") as file: 
    text = file.read()
    print(text)
    
with open("test.txt", "a") as file: 
    text = file.write("\nnew addition")
    print(text)
