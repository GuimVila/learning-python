import numpy as np

# Definim un array inicial per a exemples posteriors
arr = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# =========================================================
# 1. Creació d'arrays amb valors inicials predefinits
# =========================================================

# `np.zeros`: Crear un array ple de zeros.
# Dimensions: (1, 3) (1 fila, 3 columnes).
# `dtype`: Especifica el tipus de dades dels elements.
x = np.zeros((1, 3), dtype='int32')
print("Array ple de zeros (np.zeros):")
print(x)

# `np.ones`: Crear un array ple d'uns.
# Dimensions: (2, 4) (2 files, 4 columnes).
y = np.ones((2, 4))
print("Array ple d'uns (np.ones):")
print(y)

# `np.full`: Crear un array ple d'un valor específic.
# Dimensions: (2, 2). Valor: 99. Tipus de dades: float32.
z = np.full((2, 2), 99, dtype='float32')
print("Array ple d'un valor específic (np.full):")
print(z)

# `np.full_like`: Crear un array ple d'un valor específic amb la mateixa forma que un altre array.
new_arr = np.full_like(arr, 4)
print("Array amb el mateix shape que `arr` ple de 4 (np.full_like):")
print(new_arr)

# =========================================================
# 2. Generació de valors aleatoris
# =========================================================

# `np.random.rand`: Crear un array de valors aleatoris entre 0 i 1 (distribució uniforme).
# Dimensions: (4, 2).
print("Array de valors aleatoris entre 0 i 1 (np.random.rand):")
print(np.random.rand(4, 2))

# `np.random.random_sample`: Generar valors aleatoris amb la mateixa forma que un altre array.
print("Array aleatori amb el mateix shape que `arr` (np.random.random_sample):")
print(np.random.random_sample(arr.shape))

# `np.random.randint`: Generar enters aleatoris en un rang especificat.
# Rang: [0, 7). Dimensions: (3, 3).
print("Array d'enters aleatoris (np.random.randint):")
print(np.random.randint(7, size=(3, 3)))  # Comença a 0 per defecte si no especifiquem l'inici.

# =========================================================
# 3. Matriu identitat
# =========================================================

# `np.identity`: Crear una matriu identitat.
# Dimensions: (5, 5).
print("Matriu identitat (np.identity):")
print(np.identity(5))

# =========================================================
# 4. Repetició d'elements en un array
# =========================================================

# `np.repeat`: Repetir tots els elements d'un array.
# Repetim cada element 3 vegades.
rep = np.repeat(arr, 3)
print("Array amb elements repetits 3 vegades (np.repeat):")
print(rep)

# `np.repeat` amb `axis`: Repetir al llarg d'un eix específic.
# Repetim les files (axis=0) 3 vegades.
print("Repetir les files 3 vegades (np.repeat amb axis=0):")
print(np.repeat(arr, 3, axis=0))
