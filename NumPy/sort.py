import numpy as np

# 1. Ordenar arrays 1D
arr = np.array([3, 2, 0, 1])
sorted_arr = np.sort(arr)
print("Array ordenat (1D):")
print(sorted_arr)

# 2. Ordenar arrays de tipus diferents
# Strings
fruits = np.array(['banana', 'cherry', 'apple'])
sorted_fruits = np.sort(fruits)
print("Array de strings ordenat:")
print(sorted_fruits)

# Booleans
bools = np.array([True, False, True])
sorted_bools = np.sort(bools)
print("Array de booleans ordenat:")
print(sorted_bools)

# 3. Ordenar arrays 2D
arr_2 = np.array([[3, 2, 4], [5, 0, 1]])
sorted_arr_2 = np.sort(arr_2)
print("Array 2D ordenat per files:")
print(sorted_arr_2)

# 4. Aplanar un array 2D i ordenar-lo
arr_flat = arr_2.flatten()
sorted_flat = np.sort(arr_flat)
print("Array 2D aplanat i ordenat:")
print(sorted_flat)
