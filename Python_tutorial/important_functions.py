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