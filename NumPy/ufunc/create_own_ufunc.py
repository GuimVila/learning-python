import numpy as np

# =========================================================
# 1. Crear ufuncs personalitzades
# =========================================================
# Les "ufuncs" (Universal Functions) són funcions optimitzades de NumPy que operen
# element a element sobre arrays.
#
# Per crear una ufunc personalitzada:
# - Defineix una funció en Python, com qualsevol funció normal.
# - Afegeix-la a la biblioteca de NumPy amb el mètode `np.frompyfunc`.
#
# Arguments de `np.frompyfunc`:
# 1. `function`: El nom de la funció que vols convertir en ufunc.
# 2. `inputs`: Nombre d'arguments d'entrada (arrays).
# 3. `outputs`: Nombre de valors de retorn (arrays).

# Exemple: Crear una funció que sumi dos valors

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))
print(type(np.add))

if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')