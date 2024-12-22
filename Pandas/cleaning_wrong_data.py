import pandas as pd

# **Dades incorrectes en Pandas**
# Quan treballem amb conjunts de dades, no totes les dades errònies són cel·les buides o amb format incorrecte. A vegades, poden ser valors inesperats.
# Exemple: a la fila 7, la durada és 450 minuts, mentre que la resta de valors a la columna "Duration" oscil·len entre 30 i 60 minuts.
# Podria ser un error tipogràfic que cal corregir.

# Carreguem el fitxer CSV
df = pd.read_csv('Pandas/data3.csv')

# Mostrem el DataFrame original
print("Abans de corregir dades incorrectes:")
print(df.to_string())

# **1. Substituir valors incorrectes manualment**
# Exemple: substituïm el valor "450" a la fila 7 per "45".
df.loc[7, 'Duration'] = 45

# Mostrem el DataFrame després de la correcció manual
print("\nDesprés de corregir manualment la fila 7:")
print(df.to_string())

# **2. Substituir valors incorrectes basant-se en regles**
# Exemple: substituïm qualsevol valor a "Duration" que sigui major a 120 per "120".
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"] = 120

# Mostrem el DataFrame després d'aplicar regles
print("\nDesprés d'aplicar regles a la columna 'Duration':")
print(df.to_string())

# **3. Eliminar files amb dades incorrectes**
# Exemple: eliminem qualsevol fila on "Duration" sigui superior a 120.
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace=True)

# Mostrem el DataFrame final
print("\nDesprés d'eliminar files amb valors incorrectes:")
print(df.to_string())

# **Explicació del codi:**
# - `df.loc[7, 'Duration'] = 45`: Canvia el valor de la fila 7, columna "Duration" a "45".
# - Bucle `for`: Recorrem totes les files per buscar valors que superen un límit i els corregim o eliminem.
# - `df.drop(x, inplace=True)`: Elimina una fila del DataFrame directament.

# Aquestes tècniques permeten corregir dades errònies de manera manual o automàtica en funció de les necessitats.
