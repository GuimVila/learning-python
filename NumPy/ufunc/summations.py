import numpy as np

# **Summations and Additions**
# Hi ha una diferència clau entre la suma (addition) i la sumació (summation):
# - **Addition**: Operació que es realitza entre dos arguments, element per element.
# - **Summation**: Operació que implica sumar n elements, amb opcions per especificar dimensions.

# **1. Addition**
# La funció `np.add()` realitza una suma element per element entre dues matrius o arrays del mateix tamany.
arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

add_arr = np.add(arr1, arr2)  # Suma [1+1, 2+2, 3+3].
print("Addition (np.add):", add_arr)  # Resultat: [2 4 6]

# **2. Summation**
# La funció `np.sum()` suma tots els elements d'un array o d'un conjunt d'arrays.
sum_arr = np.sum([arr1, arr2])  # Suma tots els elements de `arr1` i `arr2`.
print("Total Summation (np.sum):", sum_arr)  # Resultat: 12

# **3. Summation amb axis**
# Si especifiquem `axis=1`, `np.sum()` suma els elements de cada array per separat.
# Això és útil quan treballem amb arrays multidimensionals.
newarr = np.sum([arr1, arr2], axis=1)  # Suma separadament arr1 i arr2.
print("Summation with axis=1 (np.sum):", newarr)  # Resultat: [6 6]

# **4. Cumulative Summation (cumsum)**
# La suma acumulativa calcula la suma parcial dels elements d'un array.
# Exemple: Per a [1, 2, 3, 4], el resultat seria [1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].
# La funció `np.cumsum()` realitza aquesta operació.
cumsum_arr = np.cumsum(arr1)
print("Cumulative Summation (np.cumsum):", cumsum_arr)  # Resultat: [1 3 6]
