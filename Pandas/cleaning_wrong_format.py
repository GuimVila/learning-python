import pandas as pd

# En molts conjunts de dades, pot haver-hi valors amb un format incorrecte, 
# especialment a les columnes de dates. Això pot dificultar o fins i tot 
# impossibilitar l'anàlisi de dades.
# Per corregir-ho, hi ha dues opcions principals:
# 1. Eliminar les files amb valors incorrectes.
# 2. Convertir totes les cel·les de la columna al mateix format.

# Carreguem el fitxer CSV
# Nota: Assegura't que el fitxer "data3.csv" estigui a la carpeta "Pandas".
df = pd.read_csv('Pandas/data3.csv')

# Convertim la columna 'Date' a un format de data reconegut per Pandas.
# Això solucionarà automàticament valors correctes però en format diferent
# (com ara "20201226"). Els valors no vàlids es convertiran en NaT (Not a Time).
df['Date'] = pd.to_datetime(df['Date'])

# Mostrem el DataFrame abans de realitzar modificacions
print("Abans de tractar els valors buits:")
print(df.to_string())

# Com podem observar, les dates amb format incorrecte es corregeixen, 
# però les cel·les buides o amb valors invàlids es converteixen a NaT.
# Per exemple, la data de la fila 26 es va corregir, però la de la fila 22 es va convertir a NaT.

# Una manera de tractar els valors buits (NaT) és eliminar les files que els contenen.
df.dropna(subset=['Date'], inplace=True)

# Mostrem el DataFrame després d'eliminar les files amb valors NaT
print("\nDesprés de tractar els valors buits (NaT):")
print(df.to_string())

# Explicació del codi:
# - La funció pd.to_datetime() converteix automàticament les cadenes a objectes de tipus data.
#   - Els valors amb format invàlid es converteixen a NaT.
# - La funció dropna(subset=['Date']) elimina les files on la columna 'Date' conté NaT.
# - L'argument inplace=True modifica el DataFrame original directament, sense crear-ne una còpia.

# Amb aquestes operacions, el DataFrame ara només conté dates vàlides
# i està llest per a l'anàlisi de dades.
