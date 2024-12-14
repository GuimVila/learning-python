import numpy as np

# Tipus de dades comuns en NumPy
# i  - integer
# b  - boolean
# u  - unsigned integer
# f  - float
# c  - complex float
# m  - timedelta
# M  - datetime
# O  - object
# S  - string
# U  - unicode string
# V  - fixed chunk of memory for other types (void)

# 1. Crear arrays amb tipus de dades específics
numbers = np.array([1, 2, 3, 4])  # Enter (default)
fruits = np.array(['apple', 'banana', 'cherry'])  # String
stringifyed = np.array([1, 2, 3, 4], dtype='S')  # String
four_beat = np.array([1, 2, 3, 4], dtype='i4')  # Enter de 4 bytes

print("Tipus de `numbers`:", numbers.dtype)
print("Tipus de `fruits`:", fruits.dtype)
print("Tipus de `stringifyed`:", stringifyed.dtype)

# 2. Errors per tipus incompatibles
try:
    arr = np.array(['a', '2', '3'], dtype='i')  # Error: No es pot convertir 'a' a integer
except ValueError as e:
    print("Error:", e)

# 3. Convertir tipus de dades amb astype()
float_arr = np.array([1.1, 2.1, 3.1])

# Convertim float a enter
newarr = float_arr.astype(int)  # També pots usar 'i' com a string
print("Array convertit a enters:", newarr)
print("Tipus del nou array:", newarr.dtype)

# 4. Propietats dels arrays: ndim, shape i size
# Crear un array 2D
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Dimensions de l'array
print("Nombre de dimensions (`ndim`):", arr_2d.ndim)  # Output: 2

# Forma de l'array (files i columnes)
print("Forma (`shape`):", arr_2d.shape)  # Output: (2, 3)

# Nombre total d'elements
print("Nombre total d'elements (`size`):", arr_2d.size)  # Output: 6
