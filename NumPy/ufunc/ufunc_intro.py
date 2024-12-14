import numpy as np

# =========================================================
# 1. Què són les ufuncs?
# =========================================================
# Les "ufuncs" (Universal Functions) són funcions de NumPy que operen element a element
# en objectes ndarray, permetent operacions ràpides i vectoritzades.
#
# Característiques clau:
# - Vectorització: Substitueix bucles iteratius per operacions en arrays.
# - Broadcasting: Permet operar en arrays de dimensions diferents.
# - Mètodes addicionals com reduce, accumulate, etc.
# - Opcions avançades com:
#    * where: Definir condicions per executar l'operació.
#    * dtype: Especificar el tipus de dades de retorn.
#    * out: Guardar els resultats en un array específic.
#
# Avantatges:
# - Les ufuncs són molt més ràpides que els bucles convencionals en Python,
#   ja que aprofiten optimitzacions modernes del maquinari.

# =========================================================
# 2. Exemple de vectorització: Comparació entre bucle i ufunc
# =========================================================

# Exemple tradicional amb un bucle
x = [1, 2, 3, 4]
y = [4, 5, 6, 7]
z = []

# Operació iterativa tradicional
for i, j in zip(x, y):
    z.append(i + j)

print("Suma utilitzant bucle tradicional:", z)

# Mateixa operació utilitzant una ufunc
z_ufunc = np.add(x, y)

print("Suma utilitzant ufunc (np.add):", z_ufunc)

# =========================================================
# 3. Opcions avançades amb ufuncs
# =========================================================

# (a) Ús de la condició `where`
# Només suma els elements on x > 2
z_where = np.add(x, y, where=np.array(x) > 2)
print("Suma amb condició (x > 2):", z_where)

# (b) Especificar el tipus de retorn amb `dtype`
z_dtype = np.add(x, y, dtype=float)
print("Suma amb dtype especificat (float):", z_dtype)

# (c) Guardar el resultat en un array existent amb `out`
result = np.zeros(len(x))  # Array de zeros per guardar el resultat
np.add(x, y, out=result)
print("Suma guardada a l'array 'result':", result)

# =========================================================
# 4. Per què les ufuncs són més ràpides?
# =========================================================
# Convertir operacions iteratives en operacions vectoritzades és molt més ràpid
# perquè els processadors moderns estan optimitzats per aquestes operacions.
# A més, NumPy utilitza biblioteques com BLAS i LAPACK optimitzades a baix nivell.
