import numpy as np

# 1. Buscar elements en un array amb np.where
arr = np.array([1, 2, 3, 4, 5, 4, 4])

# Trobar índexs on l'element és 4
x = np.where(arr == 4)
print("Índexs on l'element és 4:")
print(x)  # Output: (array([3, 5, 6]),)

# Trobar índexs on els elements són parells
y = np.where(arr % 2 == 0)
print("Índexs on l'element és parell:")
print(y)  # Output: (array([1, 3, 5, 6]),)

# Trobar índexs on els elements són senars
z = np.where(arr % 2 == 1)
print("Índexs on l'element és senar:")
print(z)  # Output: (array([0, 2, 4]),)

# 2. Cercar posicions per inserir elements amb np.searchsorted
arr_2 = np.array([6, 7, 8, 9])

# Cercar posició per inserir un valor
d = np.searchsorted(arr_2, 7)
print("Posició per inserir 7 (costat esquerre per defecte):")
print(d)  # Output: 1

e = np.searchsorted(arr_2, 7, side='right')
print("Posició per inserir 7 (costat dret):")
print(e)  # Output: 2

# Cercar múltiples valors
arr_3 = np.array([1, 3, 5, 7])
f = np.searchsorted(arr_3, [2, 4, 6])
print("Posicions per inserir 2, 4, 6:")
print(f)  # Output: [1 2 3]
