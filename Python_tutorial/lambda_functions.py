# lambda_functions.py

"""
**What are Lambda Functions?**

Una funció lambda és una funció anònima i curta que pots crear a Python. 
A diferència de les funcions definides amb `def`, les funcions lambda no tenen nom i s'utilitzen per a tasques simples o temporals.

**Sintaxi:**
lambda arguments: expression

- `arguments`: Són els paràmetres que rep la funció.
- `expression`: És l'operació o càlcul que retorna el resultat.
"""

# **1. Exemple bàsic d'una funció lambda**
# Exemple: Crear una funció lambda per sumar 10 a un nombre donat.
add_ten = lambda x: x + 10
print("Sumar 10 a 5:", add_ten(5))
# Resultat esperat: 15

# **2. Lambda amb múltiples arguments**
# Exemple: Crear una funció lambda per sumar dos nombres.
add_two_numbers = lambda a, b: a + b
print("Sumar 3 i 7:", add_two_numbers(3, 7))
# Resultat esperat: 10

# **3. Lambda dins d'una altra funció**
# Les lambdas sovint s'utilitzen dins d'altres funcions per definir operacions ràpides.
def multiplier(n):
    return lambda x: x * n

times_three = multiplier(3)  # Crea una funció que multiplica per 3
print("Multiplicar 4 per 3:", times_three(4))
# Resultat esperat: 12

# **4. Lambda amb map()**
# Exemple: Utilitzar lambda per transformar elements d'una llista.
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))
print("Quadrats dels nombres:", squared_numbers)
# Resultat esperat: [1, 4, 9, 16, 25]

# **5. Lambda amb filter()**
# Exemple: Utilitzar lambda per filtrar elements d'una llista.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Nombres parells:", even_numbers)
# Resultat esperat: [2, 4]

# **6. Lambda amb sorted()**
# Exemple: Ordenar una llista de tuples segons el segon element.
pairs = [(1, 2), (3, 1), (5, 7), (4, 3)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print("Parelles ordenades pel segon element:", sorted_pairs)
# Resultat esperat: [(3, 1), (1, 2), (4, 3), (5, 7)]

# **7. Limitacions de les funcions lambda**
"""
- Només poden contenir una expressió (no poden tenir múltiples línies o declaracions).
- No tenen nom, així que són difícils de reutilitzar.
- Les lambdas són útils per a operacions senzilles i temporals. Per a operacions més complexes, és millor utilitzar funcions normals.
"""
