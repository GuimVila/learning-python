import numpy as np

# NumPy ofereix funcions per calcular logaritmes en diferents bases:
# - Base 2 (`log2`)
# - Base 10 (`log10`)
# - Base natural (e, amb `log`).
# També explorarem com calcular logaritmes en qualsevol altra base utilitzant una funció personalitzada.

# Important:
# Si un logaritme no pot ser calculat (per exemple, log(0)), 
# el resultat serà `-inf` o `inf` en els elements corresponents.

# 1. Logaritme en base 2 (log2)
# La funció `np.log2()` calcula el logaritme base 2 per a cada element d'un array.
# Exemple: `np.log2(8)` donarà 3, ja que 2^3 = 8.

# Creem un array d'enters de 1 a 9 utilitzant `np.arange()`. 
# Nota: `np.arange(1, 10)` crea un array que comença a 1 (inclòs) fins a 10 (exclòs).
arr_1 = np.arange(1, 10)
print("Log base 2 (np.log2):", np.log2(arr_1))  # Resultat: [0. 1. 1.58496 ... 3.16993]

# 2. Logaritme en base 10 (log10)
# La funció `np.log10()` calcula el logaritme base 10 per a cada element d'un array.
# Exemple: `np.log10(100)` donarà 2, ja que 10^2 = 100.
arr_2 = np.arange(1, 10)
print("Log base 10 (np.log10):", np.log10(arr_2))  # Resultat: [0. 0.30103 ... 0.95424]

# 3. Logaritme en base natural (e) (log)
# La funció `np.log()` calcula el logaritme natural (base e ≈ 2.718) per a cada element d'un array.
# Exemple: `np.log(e)` donarà 1.
arr_3 = np.arange(1, 10)
print("Log base natural (np.log):", np.log(arr_3))  # Resultat: [0. 0.69314 ... 2.19722]

# Nota pedagògica:
# A les tres funcions, l'entrada ha de ser positiva.
# Qualsevol valor <= 0 generarà un avís (RuntimeWarning) i el resultat serà `-inf` per aquests elements.

# Opcional: Com calcular logaritmes per qualsevol altra base
# Podem crear una funció personalitzada per calcular logaritmes en qualsevol base
# usant la propietat dels logaritmes: log_a(x) = log_b(x) / log_b(a).
def log_base(arr, base):
    return np.log(arr) / np.log(base)

# Exemple: Logaritme en base 3
print("Log base 3 (custom function):", log_base(arr_3, 3))  # Resultat: [0. 0.63093 ... 1.77124]
