class Dog:
    # Aquest és un atribut de classe.
    species = "Canis familiaris"

    # El mètode __init__
    def __init__(self, name, age):
        # Aquest és el constructor de la classe. Es crida automàticament quan es crea una nova instància de la classe.
        # self: fa referència a la instància que s'està creant.

        # Atributs d'instància:
        self.name = name  # Assigna el valor del paràmetre "name" a l'atribut d'instància "self.name".
        self.age = age  # Assigna el valor del paràmetre "age" a "self.age".

# **Explicació del mètode __init__**:
# - El mètode __init__ es coneix com el constructor de la classe.
# - Quan crees una nova instància de la classe (Dog, en aquest cas), Python automàticament crida aquest mètode.
# - Permet inicialitzar els atributs de la instància amb valors proporcionats en el moment de la creació.

# Exemple de creació d'objectes (instàncies) de la classe Dog
nala = Dog("Nala", 2)  # Es crida __init__("Nala", 2)
nina = Dog("Nina", 3)  # Es crida __init__("Nina", 3)

# Atributs de les instàncies
print(nala.name)  # Sortida: Nala
print(nala.age)  # Sortida: 2
print(nina.name)  # Sortida: Nina
print(nina.age)  # Sortida: 3

# **Atributs d'instància vs atributs de classe**
# - Els atributs definits dins __init__ són específics de cada instància (atributs d'instància).
# - Els atributs definits fora d'__init__ pertanyen a la classe i tenen el mateix valor per totes les instàncies (atributs de classe).

print(nala.species)  # Sortida: Canis familiaris (atribut de classe)
print(nina.species)  # Sortida: Canis familiaris

# **Els atributs d'instància es poden modificar per instància**
nala.species = "Felis silvestris"  # Modifiquem l'atribut "species" NOMÉS per a l'objecte "nala".
print(nala.species)  # Sortida: Felis silvestris
print(nina.species)  # Sortida: Canis familiaris (no s'ha modificat per aquesta instància)

# **Conceptes clau:**
# - Crear un objecte a partir d'una classe es coneix com "instanciar una classe".
# - Els atributs d'instància tenen valors específics per a cada objecte, com "name" i "age" en aquest exemple.
# - Els atributs de classe, com "species", comparteixen el mateix valor entre totes les instàncies, tret que es sobreescriguin per una instància en concret.

# En resum:
# - Tots els objectes "Dog" comparteixen l'atribut de classe "species".
# - Els atributs d'instància, com "name" i "age", tenen valors únics i específics per a cada gos (instància).
# - __init__ serveix per configurar els atributs específics d'una instància en el moment de la seva creació.
# - Els atributs d'instància viuen a "self", mentre que els atributs de classe viuen a la classe mateixa.
