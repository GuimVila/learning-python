import numpy as np

# **Lowest Common Multiple (LCM)**
# El Mínim Comú Múltiple (MCM) és el nombre més petit que és múltiple comú de dos o més nombres.
# NumPy proporciona la funció `np.lcm()` per calcular el MCM.

# **1. MCM de dos nombres**
# La funció `np.lcm()` calcula el MCM de dos nombres donats.
# Exemple: Per a 4 i 6, el MCM és 12, perquè:
# - 4*3 = 12
# - 6*2 = 12
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print("LCM of 4 and 6:", x)  # Resultat: 12

# **2. MCM d'un array amb reduce()**
# La funció `np.lcm.reduce()` permet calcular el MCM de tots els valors d'un array.
# Exemple: Per a [3, 6, 9], el MCM és 18 perquè:
# - 3*6 = 18
# - 6*3 = 18
# - 9*2 = 18
arr = np.array([3, 6, 9])
y = np.lcm.reduce(arr)
print("LCM of [3, 6, 9]:", y)  # Resultat: 18

# **3. MCM d'un rang d'enters**
# Per calcular el MCM de tots els nombres d'un rang, com de l'1 al 10:
# - Generem un array amb `np.arange()`.
# - Fem servir `np.lcm.reduce()` per obtenir el MCM de tots els valors.
# Exemple: Per a [1, 2, 3, ..., 10], el MCM és 2520 perquè és el múltiple comú més petit.
arr1 = np.arange(1, 11)
z = np.lcm.reduce(arr1)
print("LCM of integers from 1 to 10:", z)  # Resultat: 2520

# **Explicació del MCM amb reduce():**
# La funció `reduce()` aplica la funció de manera acumulativa.
# Exemple:
# 1. Calcula el MCM del primer parell de nombres (per exemple, 3 i 6).
# 2. Usa el resultat anterior (MCM) per calcular el MCM amb el següent nombre (per exemple, 9).
# Això continua fins que es processen tots els elements.

# **Aplicació pràctica:**
# El MCM s'utilitza sovint en càlculs matemàtics com fraccions, cicles repetitius o problemes de sincronització.
