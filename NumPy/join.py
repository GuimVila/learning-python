import numpy as np

# 1. Concatenar arrays
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])

# Concatenació d'arrays 1D (per defecte axis=0, no aplica rows vs cols en 1D)
arr = np.concatenate((arr1, arr2))
print("Concatenació d'arrays 1D:")
print(arr)

# 2. Concatenar arrays 2D
arr3 = np.array([[1, 2], [3, 4]])
arr4 = np.array([[5, 6], [7, 8]])

# Explicació d'eixos (axis):
# - axis=0: Direcció vertical (afegir files, row-wise)
# - axis=1: Direcció horitzontal (afegir columnes, column-wise)

# Concatenació al llarg de les files (axis=0)
concatenated_arr = np.concatenate((arr3, arr4), axis=0)

# Concatenació al llarg de les columnes (axis=1)
concatenated_cols = np.concatenate((arr3, arr4), axis=1)

print("Concatenació al llarg de les files (axis=0):")
print(concatenated_arr)
# Output:
# [[1 2]
#  [3 4]
#  [5 6]
#  [7 8]]

print("Concatenació al llarg de les columnes (axis=1):")
print(concatenated_cols)
# Output:
# [[1 2 5 6]
#  [3 4 7 8]]

# 3. Stacking d'arrays
# Stacking és similar a concatenar, però afegeix un nou eix.
stacked_arr = np.stack((arr1, arr2), axis=1)  # Crea una nova dimensió (eix column-wise)
print("Stacking d'arrays 1D al llarg d'un nou eix (axis=1):")
print(stacked_arr)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]

# 4. Funcions d'ajuda per stacking
arr5 = np.hstack((arr1, arr2))  # Stacking horitzontal (column-wise)
print("Stacking horitzontal (hstack):")
print(arr5)
# Output: [1 2 3 4 5 6]

arr6 = np.vstack((arr1, arr2))  # Stacking vertical (row-wise)
print("Stacking vertical (vstack):")
print(arr6)
# Output:
# [[1 2 3]
#  [4 5 6]]

arr7 = np.dstack((arr1, arr2))  # Stacking en profunditat (afegir com a tercera dimensió)
print("Stacking en profunditat (dstack):")
print(arr7)
# Output:
# [[[1 4]
#   [2 5]
#   [3 6]]]
