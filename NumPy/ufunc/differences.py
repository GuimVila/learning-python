import numpy as np

# **Discrete Difference**
# La diferència discreta consisteix a restar elements successius d'un array.
# Exemple: Per a l'array [1, 2, 3, 4], el resultat seria [2-1, 3-2, 4-3] = [1, 1, 1].
# NumPy proporciona la funció `np.diff()` per calcular aquestes diferències.

# **1. Diferència discreta bàsica**
# La funció `np.diff()` calcula la diferència entre elements consecutius.
# Exemple: Per a l'array [10, 15, 25, 5]:
# - 15 - 10 = 5
# - 25 - 15 = 10
# - 5 - 25 = -20
arr1 = np.array([10, 15, 25, 5])
diff_arr = np.diff(arr1)
print("Discrete Difference (np.diff):", diff_arr)  # Resultat: [5 10 -20]

# **2. Diferència discreta repetida amb n vegades**
# La funció `np.diff()` també permet calcular diferències repetides mitjançant el paràmetre `n`.
# Exemple: Per a l'array [1, 2, 3, 4] amb n=2:
# - Primer càlcul: [2-1, 3-2, 4-3] = [1, 1, 1]
# - Segon càlcul: [1-1, 1-1] = [0, 0]
# Això es pot generalitzar a qualsevol array.

# Per a l'array [10, 15, 25, 5]:
# - Primer càlcul: [15-10, 25-15, 5-25] = [5, 10, -20]
# - Segon càlcul: [10-5, -20-10] = [5, -30]
arr = np.array([10, 15, 25, 5])
newarr = np.diff(arr, n=2)
print("Repeated Discrete Difference (np.diff with n=2):", newarr)  # Resultat: [5 -30]

# **Resum de conceptes:**
# - `np.diff()` s'utilitza per calcular diferències entre elements consecutius.
# - El paràmetre `n` especifica quantes vegades es repetirà l'operació.
# - Les dimensions de l'array es redueixen amb cada operació.

# **Aplicació pràctica:**
# Les diferències discretes s'utilitzen sovint per analitzar taxes de canvi,
# derivades discretes, o per detectar tendències en sèries temporals.

# Creem un array 2D
arr = np.array([[10, 15, 25, 5], 
                [1, 2, 3, 4]])

# **1. Diferència discreta al llarg de les files (axis=1)**
# Aquí calculem la diferència entre elements successius dins de cada fila.
diff_rows = np.diff(arr, axis=1)
print("Differences along rows (axis=1):\n", diff_rows)
# Resultat esperat:
# [[  5  10 -20]  # Primera fila: [15-10, 25-15, 5-25]
#  [  1   1   1]] # Segona fila: [2-1, 3-2, 4-3]

# **2. Diferència discreta al llarg de les columnes (axis=0)**
# Aquí calculem la diferència entre elements successius dins de cada columna.
diff_cols = np.diff(arr, axis=0)
print("Differences along columns (axis=0):\n", diff_cols)
# Resultat esperat:
# [[-9 -13 -22  -1]]  # Columna per columna: [1-10, 2-15, 3-25, 4-5]

# **3. Diferències repetides amb `n`**
# Per exemple, calculem diferències amb `n=2` al llarg de les files.
diff_n = np.diff(arr, n=2, axis=1)
print("Repeated differences along rows (n=2, axis=1):\n", diff_n)
# Resultat esperat:
# [[  5 -30]  # Primera fila: [10-5, -20-10]
#  [  0   0]] # Segona fila: [1-1, 1-1]
