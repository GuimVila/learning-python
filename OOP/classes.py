# Explicació de Classes i Instàncies en Python

class Employee:
    def __init__(self, name, age):
        # El mètode __init__ inicialitza atributs específics d'una instància.
        self.name = name  # Atribut d'instància per al nom de l'empleat
        self.age = age  # Atribut d'instància per a l'edat de l'empleat

# **Què són les classes i les instàncies?**
# - Una classe és com un plànol. Defineix l'estructura i el comportament dels objectes, però no conté dades específiques.
# - Una instància és un objecte creat a partir d'una classe. A diferència de la classe, una instància conté dades concretes.
# - El mètode `__init__` s'utilitza per inicialitzar una instància amb les seves dades específiques.

# Definim algunes dades d'exemple:
kirk = ["James Kirk", 34, "Captain", 2265]  # Exemple de dades per a un empleat
spock = ["Spock", 35, "Science Officer", 2254]
mccoy = ["Leonard McCoy", "Chief Medical Officer", 2266]

# **Per què usar classes en lloc de llistes per aquestes dades?**
# Les llistes són útils per a dades senzilles, però les classes fan més fàcil estructurar i manipular dades relacionades.
# Per exemple, una classe `Employee` pot assegurar que cada empleat tingui els atributs necessaris com `name` i `age`.

# Exemple d'ús de llistes:
print(kirk[0])  # Accés al nom
print(kirk[1])  # Accés a l'edat

# Això funciona, però no és intuïtiu. Cal recordar què representa cada índex.

# **Ús de classes per a una millor estructura:**
kirk_employee = Employee("James Kirk", 34)
spock_employee = Employee("Spock", 35)

print(kirk_employee.name)  # Accés al nom (més llegible i explícit)
print(kirk_employee.age)  # Accés a l'edat

# **Avantatges principals de les classes:**
# 1. **Llegibilitat:**
#    - En lloc de `kirk[0]`, es fa servir `kirk_employee.name`, que és molt més clar.
# 2. **Reutilització:**
#    - Pots crear múltiples instàncies d'una classe, cadascuna amb dades concretes.
# 3. **Encapsulació:**
#    - Les classes combinen dades (atributs) i comportaments (mètodes) en un sol lloc.

# **Comportament a les classes (mètodes):**
# Les classes defineixen funcions anomenades mètodes, que descriuen els comportaments que una instància pot fer.

class Employee:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role  # Afegeix el rol com un altre atribut

    def describe(self):
        # Un mètode per descriure l'empleat
        return f"{self.name}, {self.age} anys, treballa com a {self.role}."

# Creem instàncies de la classe Employee amb rols addicionals
kirk_employee = Employee("James Kirk", 34, "Captain")
spock_employee = Employee("Spock", 35, "Science Officer")

# Ús del mètode `describe`:
print(kirk_employee.describe())  # Sortida: James Kirk, 34 anys, treballa com a Captain.
print(spock_employee.describe())  # Sortida: Spock, 35 anys, treballa com a Science Officer.

# **Resum:**
# - Una **classe** és un plànol que defineix l'estructura i el comportament dels objectes.
# - Una **instància** és un objecte concret creat a partir d'una classe.
# - El mètode `__init__` inicialitza una instància amb les seves dades.
# - Els mètodes defineixen què pot fer una instància amb les seves dades, com descriure's a si mateixa.

# Les classes ajuden a organitzar dades i comportaments d'una manera més llegible, fàcil de mantenir i reutilitzable!
