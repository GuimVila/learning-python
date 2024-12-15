import numpy as np

# **What is a Set in Mathematics?**
# Un conjunt és una col·lecció d’elements únics.
# Els conjunts són útils per a operacions com la intersecció, unió, diferència i diferència simètrica.

# **1. Crear conjunts amb NumPy**
# Exemple: Convertir un array amb elements repetits en un conjunt d’elements únics.
array_with_duplicates = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
unique_elements = np.unique(array_with_duplicates)
print("Unique elements:", unique_elements)
# Resultat: [1 2 3 4 5 6 7]

# **2. Finding Union**
# Trobar els valors únics que apareixen en dos arrays (unió).
set_a = np.array([1, 2, 3, 4])
set_b = np.array([3, 4, 5, 6])
union_set = np.union1d(set_a, set_b)
print("Union of sets:", union_set)
# Resultat: [1 2 3 4 5 6]

# **3. Finding Intersection**
# Trobar els valors que apareixen en ambdós arrays (intersecció).
intersection_set = np.intersect1d(set_a, set_b, assume_unique=True)
print("Intersection of sets:", intersection_set)
# Resultat: [3 4]
# Nota: `assume_unique=True` accelera el càlcul si els arrays són conjunts.

# **4. Finding Difference**
# Trobar els valors que estan al primer conjunt però no al segon (diferència).
difference_set = np.setdiff1d(set_a, set_b, assume_unique=True)
print("Difference of set_a from set_b:", difference_set)
# Resultat: [1 2]

# **5. Finding Symmetric Difference**
# Trobar els valors que no estan presents en ambdós conjunts (diferència simètrica).
symmetric_difference_set = np.setxor1d(set_a, set_b, assume_unique=True)
print("Symmetric difference of sets:", symmetric_difference_set)
# Resultat: [1 2 5 6]
