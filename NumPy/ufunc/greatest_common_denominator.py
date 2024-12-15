# gcd_examples.py

import numpy as np

# **Greatest Common Denominator (GCD)**
# El Màxim Comú Divisor (MCD), també conegut com a HCF (Highest Common Factor),
# és el nombre més gran que pot dividir dos o més nombres sense deixar residu.

# **1. MCD de dos nombres**
# La funció `np.gcd()` calcula el MCD de dos nombres donats.
# Exemple: Per a 6 i 9, el MCD és 3, perquè:
# - 6/3 = 2
# - 9/3 = 3
num_a = 6
num_b = 9
gcd_two_numbers = np.gcd(num_a, num_b)
print("GCD of 6 and 9:", gcd_two_numbers)  # Resultat: 3

# **2. MCD d'un array amb reduce()**
# La funció `np.gcd.reduce()` permet calcular el MCD de tots els valors d'un array.
# Exemple: Per a [20, 8, 32, 36, 16], el MCD és 4, perquè:
# - És el nombre més gran que divideix tots els elements de l'array.
array_1d = np.array([20, 8, 32, 36, 16])
gcd_array_1d = np.gcd.reduce(array_1d)
print("GCD of [20, 8, 32, 36, 16]:", gcd_array_1d)  # Resultat: 4

# **3. MCD de valors més complexos (1D)**
# Exemple amb nombres més grans i complexos
complex_array = np.array([252, 105, 315, 840])
gcd_complex = np.gcd.reduce(complex_array)
print("GCD of [252, 105, 315, 840]:", gcd_complex)
# Resultat esperat: 21

# **4. Arrays multidimensionals**
# Amb `axis`, podem calcular el MCD per files o columnes.

# Creem un array 2D
array_2d = np.array([[20, 40, 60], 
                     [12, 36, 48], 
                     [28, 56, 84]])

# **4.1. MCD total**
gcd_total_2d = np.gcd.reduce(array_2d.flatten())
print("GCD of all elements (total):", gcd_total_2d)
# Resultat esperat: 4

# **4.2. MCD per files (axis=1)**
gcd_rows = np.gcd.reduce(array_2d, axis=1)
print("GCD by rows (axis=1):", gcd_rows)
# Resultat esperat: [20, 12, 28]

# **4.3. MCD per columnes (axis=0)**
gcd_columns = np.gcd.reduce(array_2d, axis=0)
print("GCD by columns (axis=0):", gcd_columns)
# Resultat esperat: [4, 4, 12]

# **5. MCD acumulatiu**
# Calcular el MCD pas a pas dins d’un eix.

# **5.1. MCD acumulatiu per files**
cumulative_gcd_rows = np.gcd.accumulate(array_2d, axis=1)
print("Cumulative GCD by rows (axis=1):\n", cumulative_gcd_rows)
# Resultat esperat:
# [[20, 20, 20], [12, 12, 12], [28, 28, 28]]

# **5.2. MCD acumulatiu per columnes**
cumulative_gcd_columns = np.gcd.accumulate(array_2d, axis=0)
print("Cumulative GCD by columns (axis=0):\n", cumulative_gcd_columns)
# Resultat esperat:
# [[20, 40, 60], [4, 4, 12], [4, 4, 12]]
