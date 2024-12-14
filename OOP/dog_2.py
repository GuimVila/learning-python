# dog.py

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance method
    # def description(self):
    def __str__(self):
        return f"{self.name} is {self.age} years old"

    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
    
nala = Dog("Nala", 2)

# print(nala.description())
print(nala) # Now there is no need to call the nala.description() method. 
print(nala.speak("Woof, Woof!"))

# Methods like .__init__() and .__str__() are called dunder methods because they begin and end with double underscores. There are many dunder methods that you can use to customize classes in Python. Understanding dunder methods is an important part of mastering object-oriented programming in Python, but for your first exploration of the topic, you’ll stick with these two dunder methods.



