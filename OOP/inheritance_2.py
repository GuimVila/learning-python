class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        # return f"{self.name} says {sound}"
        return super().speak(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass

miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

print(miles.species)
print(buddy.name)

# To determine which class a given object belongs to, you can use the built-in type():

print(type(miles))
print(isinstance(miles, Dog))

print(miles.speak())