# Explanation of asterisks (*) in Python
# Els asteriscs (*) tenen diversos usos en Python, i el seu significat depèn del context.

# **1. Multiplication and exponentiation**
# Quan s'utilitza en operacions matemàtiques, l'asterisc simple (*) representa una multiplicació.
# Doble asterisc (**) representa una potència.
result = 5 * 3  # Multiplicació (sortida: 15)
exponent = 2 ** 3  # Potència (sortida: 8)

# **2. Positional arguments (*args)**
# Un asterisc en la definició d'una funció permet agrupar un nombre variable d'arguments posicional.
def add(*args):
    """
    Aquesta funció rep un nombre variable de paràmetres i retorna la seva suma.
    """
    return sum(args)

print(add(1, 2, 3, 4))  # Sortida: 10
print(add(10, 20))  # Sortida: 30

# Els *args es passen com una tupla dins la funció.

# **3. Keyword-only arguments**
# Un asterisc en la llista de paràmetres d'una funció obliga a especificar els paràmetres següents com a arguments només per clau.
def function(*, required):
    """
    Aquesta funció requereix que "required" sigui passat com un argument només per clau.
    """
    print(required)

# Exemple d'ús:
function(required="This is a keyword-only argument")

# **Explicació més detallada sobre keyword-only arguments:**
# Quan utilitzes un asterisc (*) en la definició de paràmetres d'una funció, forces que qualsevol argument que aparegui després
# de l'asterisc sigui especificat amb el seu nom. Això evita confusions en l'ordre dels arguments i millora la claredat.

# Exemple pràctic:
def greet(*, name):
    """
    Aquesta funció només accepta l'argument 'name' com un argument clau.
    """
    print(f"Hello, {name}!")

greet(name="Alice")  # Sortida: Hello, Alice!

# Si intentes passar l'argument sense el nom:
# greet("Alice")  # Això llançarà un error: TypeError: greet() takes 0 positional arguments but 1 was given

# Per què utilitzar keyword-only arguments?
# - Clarifica la intenció del codi.
# - Evita confusions en funcions amb molts arguments.
# - Millora la robustesa del codi.

# Exemple més avançat:
def create_user(name, *, age=None):
    """
    Crea un usuari amb el nom especificat.
    L'edat és opcional i només es pot passar com un argument clau.
    """
    if age:
        print(f"Creating user {name} who is {age} years old.")
    else:
        print(f"Creating user {name} with no age specified.")

create_user("Alice", age=30)  # Sortida: Creating user Alice who is 30 years old.
create_user("Bob")  # Sortida: Creating user Bob with no age specified.

# **4. Keyword arguments (**kwargs)**
# Doble asterisc en la definició d'una funció agrupa arguments passats com a clau-valor.
def show_kwargs(**kwargs):
    """
    Aquesta funció rep arguments en format clau-valor.
    """
    for key, value in kwargs.items():
        print(f"{key}: {value}")

show_kwargs(name="John", age=30, city="Barcelona")
# Sortida:
# name: John
# age: 30
# city: Barcelona

# **5. Unpacking lists or tuples**
# Un asterisc davant d'una llista o tupla desempaqueta els seus elements.
values = [1, 2, 3, 4]
print(*values)  # Sortida: 1 2 3 4

# Exemple amb una funció:
def subtract(a, b):
    return a - b

pair = (10, 5)
print(subtract(*pair))  # Sortida: 5

# **6. Unpacking dictionaries**
# Un doble asterisc (**) desempaqueta diccionaris en arguments clau-valor.
def introduce(name, age):
    print(f"My name is {name} and I am {age} years old.")

person = {"name": "Anna", "age": 25}
introduce(**person)  # Sortida: "My name is Anna and I am 25 years old."

# **7. Asterisk in assignments**
# L'asterisc es pot utilitzar en assignacions per capturar diversos valors en una variable.
numbers = [1, 2, 3, 4, 5]
x, *middle, y = numbers
print(x)  # Sortida: 1
print(middle)  # Sortida: [2, 3, 4]
print(y)  # Sortida: 5

# **8. Multiplication of iterable elements**
# Multiplicar una cadena o una llista per un enter la repeteix.
print("Hello" * 3)  # Sortida: "HelloHelloHello"
print([0] * 4)  # Sortida: [0, 0, 0, 0]

# **Conclusion**
# Els asteriscs en Python tenen molts usos depenent del context. Des d'operacions matemàtiques fins a manejar arguments
# i desempaquetar estructures de dades, són una eina molt potent i flexible.
