import json

# =========================================================
# 1. JSON a diccionari de Python (loads)
# =========================================================

# JSON (string)
x = '{ "name":"John", "age":30, "city":"New York"}'

# Convertir JSON a un diccionari de Python
y = json.loads(x)

print("Diccionari convertit des de JSON:")
print(y)
print("Accedint a una clau del diccionari:", y["age"])  # Output: 30

# Nota: `json.loads()` interpreta una string JSON i la converteix en un objecte Python corresponent.

# =========================================================
# 2. Diccionari de Python a JSON (dumps)
# =========================================================

# Diccionari de Python
a = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Convertir un diccionari de Python en JSON
b = json.dumps(a)

print("String JSON convertit des d'un diccionari de Python:")
print(b)

# Nota: `json.dumps()` converteix un objecte Python a una string JSON.

# =========================================================
# 3. Tipus d'objectes Python que es poden convertir a JSON
# =========================================================

# Exemples de conversions vàlides
print("Diccionari:", json.dumps({"name": "John", "age": 30}))
print("Llista:", json.dumps(["apple", "bananas"]))
print("Tupla:", json.dumps(("apple", "bananas")))
print("String:", json.dumps("hello"))
print("Enter:", json.dumps(42))
print("Float:", json.dumps(31.76))
print("Booleà True:", json.dumps(True))
print("Booleà False:", json.dumps(False))
print("None:", json.dumps(None))

# Nota: Els tipus de Python compatibles amb JSON inclouen `dict`, `list`, `tuple`, `str`, `int`, `float`, `bool` i `None`.

# =========================================================
# 4. Estructures més complexes
# =========================================================

# Objecte Python complex
z = {
    "name": "John",
    "age": 30,
    "married": True,
    "divorced": False,
    "children": ("Ann", "Billy"),
    "pets": None,
    "cars": [
        {"model": "BMW 230", "mpg": 27.5},
        {"model": "Ford Edge", "mpg": 24.1}
    ]
}

# Convertir un objecte complex a JSON
print("Objecte Python complex convertit a JSON:")
print(json.dumps(z))

# Formatejar JSON amb indentació i separadors personalitzats
formatted_json = json.dumps(z, indent=4, separators=(". ", " = "))
print("JSON formatejat amb indentació i separadors personalitzats:")
print(formatted_json)
