# Explicació de l'herència en Python amb exemples de classes

# Definim la classe base "Dog"
class Dog:
    species = "Canis familiaris"  # Atribut de classe compartit per totes les instàncies

    def __init__(self, name, age):
        # Inicialitzem atributs d'instància
        self.name = name
        self.age = age

    def __str__(self):
        # Representació en forma de cadena per a l'objecte
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        # Metode que permet que el gos faci un so
        return f"{self.name} says {sound}"

# **Herència:** Creem subclasses a partir de la classe base "Dog"

class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
        # Sobrecarreguem el mètode "speak" per incloure un so per defecte
        return super().speak(sound)  # Crida al mètode de la classe pare

class Dachshund(Dog):
    pass  # No afegeix comportament nou, hereta tot de "Dog"

class Bulldog(Dog):
    pass  # Igual que "Dachshund", hereta tot de "Dog"

# **Creació d'objectes de les subclasses:**
miles = JackRussellTerrier("Miles", 4)
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3)
jim = Bulldog("Jim", 5)

# **Avantatges de les subclasses:**
# Les subclasses permeten personalitzar el comportament i els atributs d'una classe base.
# Això evita duplicar codi i fa que les classes siguin més reutilitzables.

# Exemples d'ús:
print(miles.species)  # Sortida: Canis familiaris (atribut de classe heretat)
print(buddy.name)  # Sortida: Buddy (atribut d'instància)

# Determinar la classe d'un objecte:
print(type(miles))  # Sortida: <class '__main__.JackRussellTerrier'>
print(isinstance(miles, Dog))  # Sortida: True

# Crida a mètodes:
print(miles.speak())  # Sortida: Miles says Arf (so per defecte de la subclasse)
print(jack.speak("Woof"))  # Sortida: Jack says Woof

# **Resum:**
# - La classe "Dog" és una classe base que defineix comportament i atributs comuns a tots els gossos.
# - Les subclasses com "JackRussellTerrier" poden especialitzar o estendre aquest comportament.
# - Mitjançant l'herència, podem evitar duplicar codi i estructurar millor el comportament dels objectes.

# **Casos pràctics:**
# - Utilitza l'herència per personalitzar comportaments específics d'objectes (com el so que fan).
# - Fes servir `super()` per reutilitzar funcionalitats de la classe pare sense reescriure-les.
