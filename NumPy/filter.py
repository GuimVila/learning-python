import numpy as np

# 1. Filtrar amb una llista d'índexs booleans
arr = np.array([41, 42, 43, 44])  # Array original
x = [True, False, True, False]   # Llista d'índexs booleans

newarr = arr[x]
print("Elements seleccionats utilitzant una llista booleana:")
print(newarr)  # Output: [41, 43]

# 2. Crear un filtre boolean manualment
filter_arr = []

for element in arr:
    # Afegir True si l'element és més gran que 42, sinó False
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr_2 = arr[filter_arr]

print("Filtre creat manualment:")
print(filter_arr)  # Output: [False, False, True, True]
print("Elements seleccionats amb el filtre manual:")
print(newarr_2)  # Output: [43, 44]

# 3. Filtrar directament amb condicions
filter_arr_3 = arr > 42  # Retorna un array booleà
newarr_3 = arr[filter_arr_3]

print("Filtre boolean creat amb una condició directa:")
print(filter_arr_3)  # Output: [False, False, True, True]
print("Elements seleccionats amb el filtre directe:")
print(newarr_3)  # Output: [43, 44]
