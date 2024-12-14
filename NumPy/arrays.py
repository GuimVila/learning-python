import numpy as np

# Introducció a NumPy
# NumPy és una llibreria de Python utilitzada per treballar amb arrays.
# També inclou funcions per treballar amb àlgebra lineal, transformades de Fourier i matrius.

# Exemple bàsic
arr = np.array([1, 2, 3, 4, 5, 6])

print(arr)
print(type(arr))  # Mostra el tipus de l'objecte (numpy.ndarray)

# Tipus d'arrays

# 0D Arrays (escalar, només un valor)
a = np.array(42)

# 1D Arrays (vector, una sola dimensió)
b = np.array([1, 2, 3, 4, 5])

# 2D Arrays (matriu, dues dimensions)
c = np.array([[1, 2, 3], [4, 5, 6]])

# 3D Arrays (cub o tensor, tres dimensions)
d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Mostra les dimensions de cada array
print(a.ndim)  # 0D
print(b.ndim)  # 1D
print(c.ndim)  # 2D
print(d.ndim)  # 3D

# Propietats relacionades amb la memòria dels arrays en NumPy

# `size`: Nombre total d'elements a l'array.
print("Nombre total d'elements a l'array (`size`):", a.size)

# `itemsize`: Grandària en bytes de cada element individual de l'array.
# Per exemple, si l'array conté enters de 32 bits (4 bytes), `itemsize` serà 4.
print("Grandària en bytes de cada element (`itemsize`):", a.itemsize)

# `nbytes`: Grandària total en bytes de l'array.
# És equivalent a `size * itemsize` (nombre total d'elements multiplicat per la grandària de cada element).
print("Grandària total en bytes de l'array (`nbytes`):", a.nbytes)

# Accedir a elements d'arrays

# Accedir a elements en 1D
print(b[2])  # Tercer element (índex 2)
print(b[2] + b[4])  # Suma del tercer i cinquè elements

# Accedir a elements en 2D
print(c[0, 1])  # Primera fila, segon element
print(c[1, 2])  # Segona fila, tercer element
print(c[1, -1])  # Últim element de la segona fila

# Accedir a elements en 3D
print(d[0, 1, 2])  # Primera matriu, segona fila, tercer element
print(d[1, 0, 2])  # Segona matriu, primera fila, tercer element

# Slicing (tall d'arrays) en 1D

print(b[1:4])  # Del segon al quart element (l'índex 4 no inclòs)
print(b[1:])  # Del segon fins al final
print(b[:3])  # Del principi fins al tercer (l'índex 3 no inclòs)
print(b[-3:-1])  # Des del tercer per la cua fins al penúltim
print(b[1:4:2])  # Del segon al quart en passos de dos
print(b[::2])  # Cada segon element de tot l'array

# Slicing en 2D

print(c[1, 1:3])  # Segona fila, del segon al tercer element
print(c[0:2, 2])  # Totes les files, tercera columna
print(c[0:2, 1:3])  # Totes les files, segona i tercera columna

# Observació: Les operacions amb slicing sempre retornen subarrays.
