# Explicació de com treballar amb fitxers i dades JSON en Pandas

import pandas as pd

# **Què és JSON?**
# - JSON («JavaScript Object Notation») és un format de text pla que representa objectes.
# - Es fa servir sovint per emmagatzemar i intercanviar dades, i és compatible amb moltes llibreries, incloent Pandas.

# **Llegir dades d'un fitxer JSON**
# Exemple de lectura d'un fitxer JSON amb Pandas:
df = pd.read_json('Pandas/data.json')

# Utilitzem to_string() per mostrar el DataFrame complet sense truncaments
print(df.to_string())

# **JSON com un diccionari de Python**
# Els objectes JSON tenen el mateix format que els diccionaris de Python.
# Si tens dades JSON en un diccionari de Python, pots carregar-les directament a un DataFrame.

data = {
    "Duration": {
        "0": 60,
        "1": 60,
        "2": 60,
        "3": 45,
        "4": 45,
        "5": 60
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103,
        "3": 109,
        "4": 117,
        "5": 102
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135,
        "3": 175,
        "4": 148,
        "5": 127
    },
    "Calories": {
        "0": 409,
        "1": 479,
        "2": 340,
        "3": 282,
        "4": 406,
        "5": 300
    }
}

# Convertim el diccionari a un DataFrame de Pandas
dictionarized = pd.DataFrame(data)

# Mostrem el DataFrame creat
print(dictionarized)

# **Resum:**
# - Utilitza `pd.read_json()` per llegir fitxers JSON i convertir-los automàticament a un DataFrame.
# - Si les dades JSON ja estan en un diccionari de Python, pots passar-lo directament a `pd.DataFrame()` per crear un DataFrame.
# - Treballar amb JSON és especialment útil per a dades estructurades i jeràrquiques.
