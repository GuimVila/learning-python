import numpy as np

# A NumPy ens ofereix cinc mètodes principals per arrodonir decimals.
# Cada mètode té una finalitat específica i es comporta de manera diferent segons el cas.
# A continuació, expliquem i demostrem cadascun:

# 1. Truncation (trunc)
# La funció `np.trunc()` elimina la part decimal dels nombres, truncant-los 
# cap a zero. És a dir, no arrodoneix sinó que elimina tot el que hi ha després del punt decimal.
trunc_arr = np.trunc([-3.1666, 3.6667])
print("Truncation (np.trunc):", trunc_arr)  # Resultat: [-3.  3.]

# 2. Fix
# La funció `np.fix()` també elimina la part decimal del nombre, però ho fa 
# ajustant el resultat al nombre sencer més proper cap a zero, similar a `trunc`.
fix_arr = np.fix([-3.1666, 3.6667])
print("Fix (np.fix):", fix_arr)  # Resultat: [-3.  3.]

# 3. Around
# La funció `np.around()` s'utilitza per arrodonir un nombre a un nombre 
# determinat de decimals. Aquí, s'especifica el nombre de decimals com a segon argument.
around_arr = np.around(3.1666, 2)  # Arrodonim a 2 decimals.
print("Around (np.around):", around_arr)  # Resultat: 3.17

# 4. Floor
# La funció `np.floor()` retorna el nombre enter més gran que és menor o igual
# que el nombre donat (arrodoniment cap avall).
floor_arr = np.floor([-3.1666, 3.6667])
print("Floor (np.floor):", floor_arr)  # Resultat: [-4.  3.]

# 5. Ceil
# La funció `np.ceil()` retorna el nombre enter més petit que és major o igual
# que el nombre donat (arrodoniment cap amunt).
ceil_arr = np.ceil([-3.1666, 3.6667])
print("Ceil (np.ceil):", ceil_arr)  # Resultat: [-3.  4.]
