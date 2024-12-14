class Employee:
    def __init__(self, name, age):
        self.name =  name
        self.age = age

kirk = ["James Kirk", 34, "Captain", 2265]
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

# Classes define functions called methods, which identify the behaviors and actions that an object created from the class can perform with its data.
# A class is a blueprint for how to define something. It doesn’t actually contain any data. The Dog class specifies that a name and an age are necessary for defining a dog, but it doesn’t contain the name or age of any specific dog.
# While the class is the blueprint, an instance is an object that’s built from a class and contains real data. An instance of the Dog class is not a blueprint anymore. It’s an actual dog with a name, like Miles, who’s four years old.
# You define the properties that all Dog objects must have in a method called .__init__(). Every time you create a new Dog object, .__init__() sets the initial state of the object by assigning the values of the object’s properties. That is, .__init__() initializes each new instance of the class.

