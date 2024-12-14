class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
miles = Dog("Miles", 4, "Jack Russell Terrier")
buddy = Dog("Buddy", 9, "Dachshund")
jack = Dog("Jack", 3, "Bulldog")
jim = Dog("Jim", 5, "Bulldog")

# Passing a string to every call to .speak() is repetitive and inconvenient. Moreover, the .breed attribute should determine the string representing the sound that each Dog instance makes, but here you have to manually pass the correct string to .speak() every time you call it.

buddy.speak("Yap")
jim.speak("Woof")
jack.speak("Woof")

# You can simplify the experience of working with the Dog class by creating a child class for each breed of dog. This allows you to extend the functionality that each child class inherits, including specifying a default argument for .speak().
# Check next file!!! 