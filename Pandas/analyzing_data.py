# Explicació de mètodes per obtenir una visió general d'un DataFrame en Pandas

import pandas as pd

# **Llegir un fitxer CSV**
# Llegim un fitxer CSV per crear un DataFrame
# Aquest exemple fa servir el fitxer 'Pandas/data.csv'
df = pd.read_csv('Pandas/data.csv')

# **El mètode head()**
# - Retorna les capçaleres i un nombre especificat de files, començant per la part superior.
# - Si no s'especifica el nombre de files, retorna les primeres 5 files per defecte.

print(df.head(10))  # Retorna les primeres 10 files del DataFrame

# **El mètode tail()**
# - Retorna les capçaleres i un nombre especificat de files, començant per la part inferior.
# - Si no s'especifica el nombre de files, retorna les últimes 5 files per defecte.

print(df.tail(9))  # Retorna les últimes 9 files del DataFrame

# **El mètode info()**
# - Proporciona un resum concís del DataFrame:
#   - Nombre total de files i columnes.
#   - Nom i tipus de dades de cada columna.
#   - Nombre de valors no nuls en cada columna.
# - És molt útil per obtenir una visió general de la qualitat de les dades.

print(df.info())

# **Exemple pràctic: Valors no nuls**
# - El mètode info() també ens diu quants valors no nuls hi ha a cada columna.
# - En aquest conjunt de dades, sembla que la columna "Calories" té 164 de 169 valors no nuls.
# - Això significa que hi ha 5 files amb valors buits o nuls a "Calories".

# **Tractament de valors buits**
# - Els valors buits poden ser problemàtics per analitzar dades.
# - En passos posteriors de neteja de dades, pots considerar:
#   - Eliminar files amb valors buits.
#   - Omplir els valors buits amb un valor predeterminat.

# **Resum:**
# - `head()`: Retorna una vista ràpida de les primeres files.
# - `tail()`: Retorna una vista ràpida de les últimes files.
# - `info()`: Proporciona un resum complet del DataFrame, incloent el tipus de dades i valors no nuls.
# - Aquests mètodes són fonamentals per explorar i entendre la qualitat de les dades.
