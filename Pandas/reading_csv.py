# Explicació de com treballar amb fitxers CSV en Pandas

import pandas as pd

# **Què és un fitxer CSV?**
# - Un fitxer CSV («Comma Separated Values») és una manera senzilla d'emmagatzemar grans conjunts de dades.
# - Conté text pla i pot ser llegit per qualsevol persona o llibreria com Pandas.

# **Llegir tot un fitxer CSV**
# Exemple de lectura d'un fitxer CSV complet:
entire_csv = pd.read_csv('Pandas/data.csv')

# Utilitzem to_string() per imprimir tot el DataFrame (sense truncaments)
print(entire_csv.to_string())

# **Truncament per defecte a l'hora d'imprimir un DataFrame**
# Quan imprimeixes un DataFrame directament sense to_string(), Pandas mostra:
# - Les primeres 5 files.
# - Les últimes 5 files.
first_and_last = pd.read_csv('Pandas/data.csv')
print(first_and_last)  # Trunca si hi ha moltes files

# **Opcions de visualització de Pandas**
# Pandas permet configurar la quantitat de files i columnes que es mostren per defecte.
# Exemple: comprovar el màxim de files configurades actualment
print(pd.options.display.max_rows)

# **Valor per defecte:**
# Normalment, el valor és 60. Això vol dir que si el DataFrame conté més de 60 files, es mostraran:
# - Les capçaleres.
# - Les primeres 5 files.
# - Les últimes 5 files.

# **Modificar el màxim de files a mostrar**
# Podem canviar el límit amb:
pd.options.display.max_rows = 9999

# Ara Pandas mostrarà fins a 9999 files si les dades ho permeten
modified_max_rows = pd.read_csv('Pandas/data.csv')
print(modified_max_rows)

# **Resum:**
# - Utilitza `to_string()` per imprimir tot un DataFrame sense truncaments.
# - Per defecte, Pandas trunca les dades per millorar la llegibilitat si hi ha moltes files.
# - Configura `pd.options.display.max_rows` per controlar quantes files es mostren per defecte.
