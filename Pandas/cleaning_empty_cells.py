import pandas as pd

# **Neteges de dades (Data Cleaning)**
# La neteja de dades implica corregir dades errònies dins d'un conjunt de dades.

# **Problemes comuns de dades errònies:**
# - Cel·les buides
# - Format incorrecte
# - Dades incorrectes
# - Duplicats

# Exemple de conjunt de dades:
df_original = pd.read_csv('Pandas/data2.csv')

# **Tractament de cel·les buides**
# 1. **Eliminar files amb cel·les buides**
cleaned_df = df_original.dropna()  # Crea un nou DataFrame sense files amb cel·les buides
print(cleaned_df.to_string())

# Si vols modificar el DataFrame original:
df_no_nulls = df_original.copy()
df_no_nulls.dropna(inplace=True)  # Modifica "df_no_nulls" directament
print(df_no_nulls.to_string())

# 2. **Omplir cel·les buides amb un valor especificat**
df_filled = df_original.copy()
df_filled.fillna(130, inplace=True)  # Omple totes les cel·les buides amb el valor 130
print(df_filled.to_string())

# 3. **Omplir cel·les buides en una columna especifica**
df_specific_column = df_original.copy()
df_specific_column["Calories"] = df_specific_column["Calories"].fillna(130)  # Només afecta la columna "Calories"
print(df_specific_column.to_string())

# **Càlcul de valors estadístics per omplir cel·les buides:**
# Una manera comuna d'omplir cel·les buides és utilitzar el valor mitjà, la mediana o la moda.

# Càlcul del valor mitjà (mean):
mean_value = df_original["Calories"].mean()  # Mitjana = suma de tots els valors dividida pel nombre de valors

# Omplir cel·les buides amb la mitjana:
df_mean = df_original.copy()
df_mean["Calories"] = df_mean["Calories"].fillna(mean_value)

# Càlcul de la mediana (median):
median_value = df_original["Calories"].median()  # Mediana = valor central quan els valors estan ordenats

# Omplir cel·les buides amb la mediana:
df_median = df_original.copy()
df_median["Calories"] = df_median["Calories"].fillna(median_value)

# Càlcul de la moda (mode):
mode_value = df_original["Calories"].mode()[0]  # Moda = valor que més es repeteix

# Omplir cel·les buides amb la moda:
df_mode = df_original.copy()
df_mode["Calories"] = df_mode["Calories"].fillna(mode_value)

# **Resum:**
# - `dropna()`: Elimina files amb cel·les buides.
# - `fillna(valor)`: Omple cel·les buides amb un valor especificat.
# - `mean()`, `median()`, `mode()`: Càlculs estadístics que es poden utilitzar per omplir cel·les buides.
