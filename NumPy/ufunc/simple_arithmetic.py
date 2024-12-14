import numpy as np

# =========================================================
# 1. Operacions aritmètiques element a element
# =========================================================
# NumPy permet utilitzar operadors aritmètics (+, -, *, /, etc.) directament sobre arrays,
# però també proporciona funcions aritmètiques avançades amb suport per condicions (`where`).
#
# Aquestes funcions poden operar sobre qualsevol objecte tipus array
# (llistes, tuples, arrays NumPy, etc.).

# =========================================================
# 2. Sumar valors amb `np.add`
# =========================================================
arr1 = np.array([10, 11, 12, 13, 14, 15])
arr2 = np.array([20, 21, 22, 23, 24, 25])

# Suma element a element
add_arr = np.add(arr1, arr2)
print("Suma:", add_arr)

# =========================================================
# 3. Restar valors amb `np.subtract`
# =========================================================
subs_arr = np.subtract(arr1, arr2)
print("Resta:", subs_arr)

# =========================================================
# 4. Multiplicar valors amb `np.multiply`
# =========================================================
mult_arr = np.multiply(arr1, arr2)
print("Multiplicació:", mult_arr)

# =========================================================
# 5. Dividir valors amb `np.divide`
# =========================================================
div_arr = np.divide(arr1, arr2)
print("Divisió:", div_arr)

# =========================================================
# 6. Potències amb `np.power`
# =========================================================
# Elevar els valors de `arr1` a la potència dels valors de `arr2`
pow_arr = np.power(arr1, arr2)
print("Potències:", pow_arr)

# =========================================================
# 7. Residu de la divisió amb `np.mod` i `np.remainder`
# =========================================================
# `np.mod` i `np.remainder` retornen el residu de la divisió element a element.
# Exemple:
# - Dividir 10 per 3: Quocient = 3, Residu = 1
mod_arr = np.mod(arr1, arr2)
print("Residu amb np.mod:", mod_arr)

# Diferències entre `np.mod` i `np.remainder`:
# - `np.mod`: El residu té el mateix signe que el divisor.
# - `np.remainder`: El residu té el mateix signe que el dividend.
dividend = -10
divisor = 3
res_mod = np.mod(dividend, divisor)
res_rem = np.remainder(dividend, divisor)
print("Residu amb np.mod (-10 % 3):", res_mod)       # 2
print("Residu amb np.remainder (-10 % 3):", res_rem) # -1

# =========================================================
# 8. Quocient i residu amb `np.divmod`
# =========================================================
# `np.divmod` retorna dos arrays: quocient i residu.
divmod_arr = np.divmod(arr1, arr2)
print("Quocient amb np.divmod:", divmod_arr[0])
print("Residu amb np.divmod:", divmod_arr[1])

# =========================================================
# 9. Valor absolut amb `np.absolute` i `np.abs`
# =========================================================
# Calcula el valor absolut element a element.
arr = np.array([-1, -2, 1, 2, 3, -4])
abs_arr = np.absolute(arr)
print("Valor absolut:", abs_arr)
