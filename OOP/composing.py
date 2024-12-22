# Explicació del mètode especial __repr__ i el seu ús en Python amb objectes personalitzats

class Point:
    def __init__(self, x, y):
        # Inicialitzem els atributs d'instància x i y
        self.x = x
        self.y = y

    def __repr__(self):
        # El mètode __repr__ proporciona una representació informativa de l'objecte Point
        return f"Point({self.x}, {self.y})"

class Shape:
    def __init__(self, points):
        # Inicialitzem un objecte Shape amb una llista de punts (instàncies de Point)
        self.points = points

    def __repr__(self):
        # El mètode __repr__ proporciona una representació clara d'un Shape com una llista de punts
        return f"Shape({self.points})"

# Creació d'un triangle amb punts
triangle = Shape([
    Point(0, 0),
    Point(5, 5),
    Point(2, 4)
])

print(triangle)  # Sortida: Shape([Point(0, 0), Point(5, 5), Point(2, 4)])
print(triangle.points)  # Mostra la llista de punts

# Creació d'un quadrat amb punts
bottom_left = Point(0, 0)
bottom_right = Point(10, 0)
top_left = Point(0, 10)
top_right = Point(10, 10)

square = Shape([
    bottom_left,
    bottom_right,
    top_left,
    top_right
])

print(square)  # Sortida: Shape([Point(0, 0), Point(10, 0), Point(0, 10), Point(10, 10)])
print(square.points)  # Mostra la llista de punts

# **Què és el mètode especial __repr__?**
# - __repr__ és un mètode especial en Python que retorna una cadena que representa l'objecte de manera informativa.
# - Es fa servir principalment per a:
#     1. Depuració: Mostra detalls clars dels objectes quan es treballa en entorns interactius o es fan logs.
#     2. Documentació: Proporciona una representació que podria ser suficient per recrear l'objecte.

# **Objectiu principal de __repr__:**
# - Retornar una cadena que sigui el més informativa possible sobre l'estat de l'objecte.
# - Aquesta cadena sol incloure els valors dels atributs més rellevants de l'objecte.

# **Avantatges del mètode __repr__:**
# 1. **Llegibilitat:** Els objectes personalitzats mostren informació clara en lloc d'una referència genèrica com <__main__.Point object at 0x...>.
# 2. **Depuració més fàcil:** Permet veure l'estat intern dels objectes de forma immediata.
# 3. **Claredat en logs i consoles:** Quan fas print() o repr(), el resultat és molt més interpretatiu.

# **Recomanació per implementar __repr__:**
# - Proporciona una representació que mostri els atributs clau de l'objecte.
# - Opcionalment, fes que la cadena sigui suficient per reconstruir l'objecte, seguint aquesta estructura:
#   "NomClasse(atribut1=valor1, atribut2=valor2)"
