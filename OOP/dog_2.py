# Explicació dels dunder methods i el seu ús en Python

# dog.py

class Dog:
    # Aquest és un atribut de classe. Tots els objectes "Dog" compartiran aquest valor.
    species = "Canis familiaris"

    def __init__(self, name, age):
        # El mètode __init__ inicialitza els atributs d'instància "name" i "age".
        self.name = name
        self.age = age

    def __str__(self):
        # __str__ és un dunder method que proporciona una representació en forma de cadena per a l'objecte.
        return f"{self.name} is {self.age} years old"

    # Un altre mètode d'instància
    def speak(self, sound):
        # Aquest mètode permet que el gos emeti un so.
        return f"{self.name} says {sound}"

# Crear una instància de la classe Dog
nala = Dog("Nala", 2)

# Imprimim la representació de l'objecte "nala"
print(nala)  # Ara no cal cridar el mètode description() ja que __str__ ho cobreix.
print(nala.speak("Woof, Woof!"))

# **Què són els dunder methods?**
# - Els dunder methods (de "double underscore") són mètodes especials en Python que comencen i acaben amb doble guionet baix (__).
# - S'utilitzen per personalitzar el comportament de les classes.

# **Dos dunder methods importants:**
# 1. **__init__():**
#    - Inicialitza els atributs d'una instància quan es crea un objecte.
#    - Exemple: Quan cridem `Dog("Nala", 2)`, Python executa automàticament el mètode `__init__` per configurar "name" i "age".
# 2. **__str__():**
#    - Retorna una representació en forma de cadena de l'objecte, que és especialment útil per a "print()".
#    - Exemple: Quan fem `print(nala)`, Python crida automàticament `__str__()`.

# **Altres dunder methods rellevants:**
# - `__repr__()`: Proporciona una representació oficial de l'objecte per depuració.
# - `__len__()`: Permet definir el que retorna `len(obj)` per a un objecte.
# - `__eq__()`: Defineix el comportament de "==" per comparar objectes.

# **Avantatges d'usar dunder methods:**
# - Personalitzen el comportament d'objectes per fer-los més intuïtius.
# - Fan que els objectes siguin més llegibles en consoles i logs.
# - Permeten adaptar els objectes a operacions i funcions nadiues de Python.

# **Resum:**
# Els dunder methods com `__init__` i `__str__` són clau per a l'orientació a objectes en Python. Ens permeten configurar i representar objectes de manera clara i funcional, millorant l'experiència de programació.
