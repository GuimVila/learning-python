import numpy as np

# 1. Dividir arrays 1D
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print("Divisió d'un array 1D en 3 subarrays:")
print(newarr)

# 2. Dividir arrays 1D amb nombre desigual d'elements
arr_2 = np.array([1, 2, 3, 4, 5, 6])
newarr_2 = np.array_split(arr_2, 4)
print("Divisió d'un array 1D en 4 subarrays (nombre desigual d'elements):")
print(newarr_2)

# 3. Dividir arrays 2D
arr_3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr_3 = np.array_split(arr_3, 3)
print("Divisió d'un array 2D en 3 subarrays per files:")
print(newarr_3)

newarr_4 = np.array_split(arr_3, 3, axis=1)
print("Divisió d'un array 2D en 3 subarrays per columnes:")
print(newarr_4)

# 4. Alternativa: Divisió horitzontal amb np.hsplit
arr_5 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr_5 = np.hsplit(arr_5, 3)
print("Divisió horitzontal (np.hsplit):")
print(newarr_5)
