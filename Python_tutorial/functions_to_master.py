# **Print Function**
# La funció `print` permet imprimir informació a la consola.
age = 38
name = "John"

# Exemple: Format de cadena amb `f-string`
print(f"My name is {name} and I'm {age} years old")

# Exemple: Separador personalitzat amb `sep`
print("My name is", name, "and I'm", age, "years old", sep="|")

# Exemple: Control de la línia final amb `end`
print("Hello", end=" ")
print("World")

# **Help Function**
# Mostra informació detallada sobre qualsevol funció:
# help(print)

# **Range Function**
# Crea un rang d’enters.
rng = range(10)  # De 0 a 9
print(list(rng))

# Rang amb valors inicial i final
rng_start_end = range(2, 10)  # De 2 a 9
print(list(rng_start_end))

# Rang amb pas específic
rng_step = range(2, 10, 2)  # De 2 a 8 amb pas de 2
print(list(rng_step))

# **Map Function**
# `map` aplica una funció a cada element d’un iterable.
strings = ["my", "world", "apple", "pear"]

# Exemple: Longitud de cada element
lengths = list(map(len, strings))
print(lengths)

# Exemple: Transformació amb una funció lambda
plural_strings = list(map(lambda x: x + "s", strings))
print(plural_strings)

# Exemple: Transformació amb una funció definida
def add_suffix_s(string):
    return string + "s"

plural_with_func = list(map(add_suffix_s, strings))
print(plural_with_func)

# **Filter Function**
# `filter` retorna només els elements que compleixen una condició.
def longer_than_4(string):
    return len(string) > 4

filtered_strings = list(filter(longer_than_4, strings))
print(filtered_strings)

# Exemple amb lambda
filtered_lambda = list(filter(lambda x: len(x) > 4, strings))
print(filtered_lambda)

# **Sum Function**
# Calcula la suma d’un iterable.
numbers = {1, 2, 3, 4, 5, 24, 4.5}
print(sum(numbers))  # Suma total

# Exemple: Suma amb un valor inicial
print(sum(numbers, start=10))

# **Sorted Function**
# Ordena un iterable en ordre ascendent o descendent.
numbers_list = [4, 5, 2, 3, -1, 0, 9]
print(sorted(numbers_list))  # Ascendent
print(sorted(numbers_list, reverse=True))  # Descendent

# Ordenar amb una funció personalitzada
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35},
    {"name": "David", "age": 20}
]

sorted_people = sorted(people, key=lambda person: person["age"])
print(sorted_people)

# **Enumerate Function**
# Exemple: Millorar iteracions amb índex.
tasks = ["Write report", "Attend meeting", "Review code", "Submit timesheet"]

for index, task in enumerate(tasks, start=1):
    print(f"{index}. {task}")

# **Zip Function**
# Combina diversos iterables en tuples.
names = ["Alice", "Bob", "Daniel", "David", "Tim"]
ages = [30, 25, 35, 20]
genders = ["Female", "Male", "Male"]

combined = list(zip(names, ages))
print(combined)

combined_with_genders = list(zip(names, ages, genders))
print(combined_with_genders)

# **Open Function**
# Obrir, escriure i llegir fitxers.

# Exemple: Escriure un fitxer
with open("test.txt", "w") as file:
    file.write("Hello world\nmy name is Guillem")

# Exemple: Llegir un fitxer
with open("test.txt", "r") as file:
    content = file.read()
    print(content)

# Exemple: Afegir contingut a un fitxer
with open("test.txt", "a") as file:
    file.write("\nnew addition")
