# Python Collections (Arrays)

# Python té quatre tipus de col·leccions de dades principals:
# 1. **List:** Ordenada, modificable i permet elements duplicats.
# 2. **Tuple:** Ordenada, immutable i permet elements duplicats.
# 3. **Set:** No ordenada, immutable (*en alguns casos*) i sense elements duplicats.
# 4. **Dictionary:** Ordenat (*a partir de Python 3.7*), modificable i sense claus duplicades.

# =========================================================
# 1. LISTS
# =========================================================
# Una llista és una col·lecció ordenada i modificable. Permet elements duplicats.

# Crear llistes
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# Llistes amb múltiples tipus de dades
list4 = ["abc", 34, True, 40, "male"]

# Crear llistes amb el constructor list()
thislist = list(("apple", "banana", "cherry"))  # Nota: Doble parèntesi necessari
print("Llista creada amb `list()`:", thislist)

# =========================================================
# 2. TUPLES
# =========================================================
# Una tupla és una col·lecció ordenada i immutable (no es pot modificar). Permet elements duplicats.

# Crear tuples
thistuple = ("apple",)
print("Tipus d'un element amb coma:", type(thistuple))  # Tuple

# Sense coma, no és una tupla
thistuple = ("apple")
print("Tipus sense coma:", type(thistuple))  # String

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# Crear tuples amb el constructor tuple()
thistuple = tuple(("apple", "banana", "cherry"))  # Nota: Doble parèntesi necessari
print("Tupla creada amb `tuple()`:", thistuple)

# Nota: Les tuples són útils per dades que no han de canviar (com coordenades o configuracions).

# =========================================================
# 3. SETS
# =========================================================
# Un set és una col·lecció no ordenada, no indexada i immutable (*no pots modificar els elements,
# però sí que pots afegir o eliminar elements*). No permet duplicats.

# Crear sets
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}  # Els duplicats es descarten automàticament

# Crear sets amb el constructor set()
thisset = set(("apple", "banana", "cherry"))  # Nota: Doble parèntesi necessari
print("Set creat amb `set()`:", thisset)

# Nota: Els sets són útils per eliminar duplicats o per operacions matemàtiques (unions, interseccions, etc.).

# =========================================================
# 4. DICTIONARIES
# =========================================================
# Un diccionari és una col·lecció ordenada (*a partir de Python 3.7*), modificable i no permet claus duplicades.
# Cada element és una parella clau-valor.

# Crear un diccionari
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print("Valor de la clau 'brand':", thisdict["brand"])

# Crear diccionaris amb el constructor dict()
thisdict = dict(name="John", age=36, country="Norway")
print("Diccionari creat amb `dict()`:", thisdict)

# Nota: Els diccionaris són ideals per representar dades relacionades amb claus i valors.
