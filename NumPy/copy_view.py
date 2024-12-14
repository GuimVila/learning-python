import numpy as np

# 1. Crear arrays
arr = np.array([1, 2, 3, 4, 5])  # Array original

# Crear una còpia (independent)
copied_arr = arr.copy()

# Crear una vista (connectada a l'original)
viewed_arr = arr.view()

# 2. Comparar comportament amb canvis
arr[0] = 42  # Modifiquem l'array original

# Imprimir els arrays
print("Array original:")
print(arr)  # [42, 2, 3, 4, 5]

print("Còpia de l'array (independent):")
print(copied_arr)  # [1, 2, 3, 4, 5]

print("Vista de l'array (connectada):")
print(viewed_arr)  # [42, 2, 3, 4, 5]

# 3. Propietat .base
print("La còpia té base?:", copied_arr.base)  # None (independent)
print("La vista té base?:", viewed_arr.base)  # Mostra l'array original

# 4. Modificar la vista
viewed_arr[1] = 99  # Canviem un element a la vista

print("Array original després de modificar la vista:")
print(arr)  # [42, 99, 3, 4, 5]

print("Vista després del canvi:")
print(viewed_arr)  # [42, 99, 3, 4, 5]
