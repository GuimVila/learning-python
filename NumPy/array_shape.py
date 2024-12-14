import numpy as np

# 1. Shape de l'array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Shape de l'array:")
print(arr.shape)

# 2. Canviar la forma (reshape)
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = array.reshape(4, 3)
print("Array original:")
print(array)
print("Array amb nova forma:")
print(newarr)

# 3. Iteració en arrays

# Iteració en arrays 2D
print("Iteració sobre un array 2D:")
for row in arr:
    for element in row:
        print("Element:", element)

# Iteració en arrays 3D
array_2 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("Iteració manual sobre un array 3D:")
for matrix in array_2:
    for row in matrix:
        for element in row:
            print("Element:", element)

# Iteració amb np.nditer
print("Iteració amb np.nditer:")
for element in np.nditer(array_2):
    print("Element:", element)

# Iteració amb np.nditer i tipus personalitzats
# `np.nditer` permet iterar sobre un array element per element.
# En aquest cas, utilitzem:
# - `flags=['buffered']`: Activa un buffer temporal per convertir els tipus de dades si és necessari.
# - `op_dtypes=['S']`: Especifica que volem convertir els elements a strings ('S' significa tipus string).
# Això és útil quan el tipus original de l'array (en aquest cas, int) no coincideix amb el tipus requerit.

print("Iteració amb np.nditer i tipus personalitzats:")
for element in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print("Element com a string:", element)
