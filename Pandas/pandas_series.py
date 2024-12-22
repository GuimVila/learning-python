# Explicació de Series i DataFrames en Pandas
import pandas as pd

# **Què és una Series?**
# Una Series de Pandas és com una columna en una taula.
# És una estructura de dades unidimensional que pot contenir dades de qualsevol tipus.

a = [1, 7, 2]  # Llista d'exemple

# Crear una Series a partir d'una llista
myArray = pd.Series(a)
print(myArray)  # Mostra els valors amb els seus indexos per defecte (0, 1, 2)

# **Accedir als valors per index**
# Si no s'especifica cap altre valor, els indexos seran numerats automàticament (0, 1, 2...)
print(myArray[0])  # Accedeix al primer valor (sortida: 1)

# **Afegir etiquetes personalitzades als indexos**
# Es pot utilitzar l'argument "index" per especificar etiquetes personalitzades.
myPandasArray = pd.Series(a, index=["x", "y", "z"])
print(myPandasArray)  # Mostra els valors amb etiquetes x, y, z

# Accedir als valors per etiqueta
def get_value(series, label):
    return series[label]

print(get_value(myPandasArray, "y"))  # Sortida: 7

# **Crear una Series a partir d'un diccionari**
# Es poden utilitzar objectes clau/valor (com diccionaris) per crear una Series.
calories = {"day1": 420, "day2": 380, "day3": 390}
myPandasDictionary = pd.Series(calories)
print(myPandasDictionary)  # Mostra les dades del diccionari com una Series

# **Seleccionar algunes claus del diccionari**
# Es pot especificar quins elements incloure utilitzant l'argument "index".
selectingSome = pd.Series(calories, index=["day1", "day2"])
print(selectingSome)  # Només mostra day1 i day2

# **Què és un DataFrame?**
# Els DataFrames són estructures multidimensionals que representen taules completes.
# Una Series és com una columna, mentre que un DataFrame és la taula sencera.

data = {
    "calories": [420, 380, 390],  # Primera columna
    "duration": [50, 40, 45]  # Segona columna
}

# Crear un DataFrame a partir d'un diccionari
df = pd.DataFrame(data)
print(df)  # Mostra una taula amb les columnes calories i duration

# **Resum:**
# - Una Series és una estructura unidimensional similar a una columna.
# - Un DataFrame és una estructura multidimensional que representa una taula completa.
# - Series i DataFrames es poden crear a partir de llistes, diccionaris i altres fonts de dades.
# - Amb Series, pots accedir a valors utilitzant indexos o etiquetes personalitzades.

# As you can see from the result above, the DataFrame is like a table with rows and columns.
# Pandas use the loc attribute to return one or more specified row(s)

# **Accedir a files específiques**

print(df.loc[0])  # Retorna la primera fila

#use a list of indexes:
print(df.loc[[0, 1]]) # Retorna les files 0 i 1


df2 = pd.DataFrame(data, index = ["day1", "day2", "day3"]) # Assigna etiquetes personalitzades a les files
print(df2)

# **Accedir a files i columnes específiques**
print(df2.loc["day2"])








