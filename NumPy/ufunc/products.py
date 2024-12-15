import numpy as np

# **Product of Array Elements**
# NumPy permet calcular el producte dels elements d'un array utilitzant diverses funcions:
# - Producte total amb `np.prod()`
# - Producte per eixos (axes) amb `axis`
# - Producte acumulatiu amb `np.cumprod()`

# **1. Producte total d'un array**
# La funció `np.prod()` calcula el producte de tots els elements d'un array.
# Exemple: Per a l'array [1, 2, 3, 4], el resultat és 1*2*3*4 = 24.
arr1 = np.array([1, 2, 3, 4])
x = np.prod(arr1)
print("Total Product (np.prod):", x)  # Resultat: 24

# **2. Producte d'elements de diversos arrays**
# Quan passem diversos arrays a `np.prod()`, es calcula el producte de tots els seus elements combinats.
# Exemple: [1, 2, 3, 4] i [5, 6, 7, 8] donen 1*2*3*4*5*6*7*8 = 40320.
arr2 = np.array([1, 2, 3, 4])
arr3 = np.array([5, 6, 7, 8])
y = np.prod([arr2, arr3])
print("Combined Product (np.prod):", y)  # Resultat: 40320

# **3. Producte per eixos (axis)**
# Si especifiquem `axis=1`, `np.prod()` calcula el producte dels elements de cada array per separat.
# Exemple: Per als arrays [1, 2, 3, 4] i [5, 6, 7, 8], els resultats són:
# - Producte del primer array: 1*2*3*4 = 24
# - Producte del segon array: 5*6*7*8 = 1680
arr4 = np.array([1, 2, 3, 4])
arr5 = np.array([5, 6, 7, 8])
z = np.prod([arr4, arr5], axis=1)
print("Product per array (np.prod with axis):", z)  # Resultat: [24 1680]

# **4. Producte acumulatiu (cumulative product)**
# La funció `np.cumprod()` calcula el producte acumulatiu dels elements d'un array.
# Exemple: Per a l'array [1, 2, 3, 4], els resultats són:
# - 1
# - 1*2 = 2
# - 1*2*3 = 6
# - 1*2*3*4 = 24
arr = np.array([5, 6, 7, 8])
newarr = np.cumprod(arr)
print("Cumulative Product (np.cumprod):", newarr)  # Resultat: [5 30 210 1680]

# **Resum de funcions:**
# - `np.prod()` calcula el producte total d'elements.
# - `np.prod(..., axis=1)` calcula el producte de cada array.
# - `np.cumprod()` calcula el producte acumulatiu (parcial).

# Creem un array multidimensional (2D)
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8]])

# **1. Producte total de tots els elements**
# Si no especifiquem `axis`, `np.prod()` calcula el producte total de tots els elements de l'array.
total_product = np.prod(arr)
print("Producte total (np.prod):", total_product)
# Resultat esperat: 1*2*3*4*5*6*7*8 = 40320

# **2. Producte al llarg de les files (axis=1)**
# Aquí, `np.prod(axis=1)` calcula el producte dels elements successius dins de cada fila.
product_rows = np.prod(arr, axis=1)
print("Producte per files (axis=1):", product_rows)
# Resultat esperat:
# Primera fila: 1*2*3*4 = 24
# Segona fila: 5*6*7*8 = 1680
# [24, 1680]

# **3. Producte al llarg de les columnes (axis=0)**
# Aquí, `np.prod(axis=0)` calcula el producte dels elements successius dins de cada columna.
product_columns = np.prod(arr, axis=0)
print("Producte per columnes (axis=0):", product_columns)
# Resultat esperat:
# Primera columna: 1*5 = 5
# Segona columna: 2*6 = 12
# Tercera columna: 3*7 = 21
# Quarta columna: 4*8 = 32
# [5, 12, 21, 32]

# **4. Producte acumulatiu (cumulative product)**
# La funció `np.cumprod()` també funciona amb arrays multidimensionals.
# Per defecte, flateja l'array i calcula el producte acumulatiu.
cumulative_total = np.cumprod(arr)
print("Producte acumulatiu total (np.cumprod):", cumulative_total)
# Resultat esperat:
# [1, 1*2, 1*2*3, ..., 1*2*3*4*5*6*7*8]
# [1, 2, 6, 24, 120, 720, 5040, 40320]

# **5. Producte acumulatiu al llarg d'un eix**
# Pots especificar l'eix per calcular el producte acumulatiu al llarg de les files o columnes.
# Acumulatiu per files (axis=1)
cumulative_rows = np.cumprod(arr, axis=1)
print("Producte acumulatiu per files (np.cumprod axis=1):\n", cumulative_rows)
# Resultat esperat:
# Primera fila: [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]
# Segona fila: [5, 5*6, 5*6*7, 5*6*7*8] = [5, 30, 210, 1680]

# Acumulatiu per columnes (axis=0)
cumulative_columns = np.cumprod(arr, axis=0)
print("Producte acumulatiu per columnes (np.cumprod axis=0):\n", cumulative_columns)
# Resultat esperat:
# Primera columna: [1, 1*5] = [1, 5]
# Segona columna: [2, 2*6] = [2, 12]
# Tercera columna: [3, 3*7] = [3, 21]
# Quarta columna: [4, 4*8] = [4, 32]
