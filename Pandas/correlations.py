import pandas as pd

# **Analitzar relacions entre columnes amb Pandas**
# Pandas ofereix la funció `corr()` per calcular la relació entre les columnes d'un conjunt de dades.
# Aquesta funció és molt útil per entendre com es relacionen les variables numèriques entre elles.

# Carreguem el fitxer CSV
df = pd.read_csv('Pandas/data4.csv')

# **1. Calcular la correlació entre les columnes**
# La funció `corr()` calcula un coeficient de correlació per a cada parell de columnes numèriques.
# Aquest coeficient, conegut com a coeficient de correlació de Pearson, mesura la força i la direcció de la relació lineal entre dues columnes.
# Es calcula com la covariància de les dues variables dividida pel producte de les seves desviacions estàndard:
#   r = cov(X, Y) / (std(X) * std(Y))
# On:
# - `cov(X, Y)` és la covariància entre les variables X i Y.
# - `std(X)` i `std(Y)` són les desviacions estàndard de X i Y.
# Aquesta normalització assegura que els valors oscil·lin entre -1 i 1.
correlation = df.corr()

# Mostrem la taula de correlacions
print("Correlació entre columnes:")
print(correlation)

# **Explicació del resultat:**
# - Els valors oscil·len entre -1 i 1:
#   - `1`: Relació perfecta positiva (quan una variable augmenta, l'altra també).
#   - `-1`: Relació perfecta negativa (quan una variable augmenta, l'altra disminueix).
#   - `0`: No hi ha relació significativa.

# **Exemples destacats del resultat:**
# 1. **Correlació perfecta:**
#    - La diagonal de la taula (ex: "Duration" amb "Duration") sempre tindrà el valor `1.0`, ja que cada columna té una correlació perfecta amb si mateixa.
# 2. **Bona correlació:**
#    - "Duration" i "Calories" tenen una correlació alta, per exemple `0.922721`, indicant que com més llarg és l'exercici, més calories es cremen.
# 3. **Mala correlació:**
#    - "Duration" i "Maxpulse" tenen una correlació baixa, per exemple `0.009403`, indicant que la durada no és un bon predictor del pols màxim.

# **Consideracions:**
# - La funció `corr()` ignora automàticament les columnes no numèriques.
# - Una bona correlació depèn del context, però un valor absolut superior a 0.6 sol considerar-se significatiu.
