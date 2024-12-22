import pandas as pd

# **Gestió de duplicats en Pandas**
# En molts conjunts de dades, pot haver-hi files duplicades que s'han registrat més d'una vegada.
# Això pot afectar l'anàlisi de dades i, per tant, és important identificar i gestionar aquests duplicats.

# Exemple de conjunt de dades amb duplicats (fila 11 i 12 són idèntiques).
df = pd.read_csv('Pandas/data3.csv')

# **1. Identificar duplicats**
# La funció `duplicated()` retorna valors booleans per a cada fila:
# - `True`: Si la fila és un duplicat d'una fila anterior.
# - `False`: Si la fila no és un duplicat.
print("Duplicats identificats:")
print(df.duplicated())

# **2. Eliminar duplicats**
# Per eliminar les files duplicades del DataFrame, utilitzem `drop_duplicates()`.
df.drop_duplicates(inplace=True)

# Mostrem el DataFrame després d'eliminar els duplicats
print("\nDesprés d'eliminar duplicats:")
print(df.to_string())

# **Explicació del codi:**
# - `df.duplicated()`: Identifica les files duplicades, retornant `True` per als duplicats.
# - `df.drop_duplicates(inplace=True)`: Elimina les files duplicades del DataFrame original.
#   - `inplace=True`: Modifica el DataFrame original en lloc de retornar-ne una còpia.

# Aquesta tècnica és útil per netejar les dades i assegurar-se que cada fila del conjunt és única.
