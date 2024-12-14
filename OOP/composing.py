class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return f"Point({self.x}, {self.y})"
        
class Shape: 
    def __init__(self, points):
        self.points = points

triangle = Shape([
    Point(0, 0),
    Point(5, 5),
    Point(2, 4)
])

print(triangle)
print(triangle.points)

bottom_left = Point(0, 0)
bottom_right = Point(10, 0)
top_left = Point(0, 10)
top_right = Point (10, 10)

square = Shape([
    bottom_left,
    bottom_right,
    top_left,
    top_right
])

print(square)
print(square.points)

# El mètode especial __repr__ en Python s'utilitza per proporcionar una representació "oficial" o "informativa" d'un objecte. És especialment útil quan treballes amb objectes personalitzats i vols que la seva representació sigui més comprensible i llegible quan es mostren en depuradors, logs o quan utilitzes el mètode repr().

# Funcionament del mètode __repr__
# Objectiu principal:

# Retornar una cadena de text (string) que representi l'objecte d'una manera que sigui el més informativa possible.
# Generalment, aquesta cadena hauria de ser suficient per poder recrear l'objecte o entendre el seu estat.