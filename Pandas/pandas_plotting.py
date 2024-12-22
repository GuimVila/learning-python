import pandas as pd
import matplotlib.pyplot as plt

# **Visualitzar dades amb Pandas i Matplotlib**
# Pandas permet generar diagrames utilitzant el mètode `plot()`. 
# A més, podem utilitzar `Pyplot`, un submòdul de Matplotlib, per visualitzar els gràfics a la pantalla.

# **1. Carregar les dades del CSV**
df = pd.read_csv('Pandas/data4.csv')

# **2. Crear un gràfic genèric amb Pandas**
# Utilitzem el mètode `plot()` per visualitzar totes les columnes del DataFrame.
df.plot()
plt.title("Gràfic genèric de totes les columnes")
plt.show()

# **3. Crear un diagrama de dispersió (scatter plot)**
# Un scatter plot requereix especificar els eixos x i y. Utilitzem els arguments `x` i `y`.
# Exemple 1: Relació entre "Duration" i "Calories".
df.plot(kind='scatter', x='Duration', y='Calories')
plt.title("Relació entre Durada i Calories")
plt.show()

# Recordem: A la taula de correlació, vam observar una correlació alta (0.922721) entre aquestes dues columnes.

# Exemple 2: Relació entre "Duration" i "Maxpulse".
df.plot(kind='scatter', x='Duration', y='Maxpulse')
plt.title("Relació entre Durada i Pols Màxim")
plt.show()

# Aquest exemple mostra una correlació baixa (0.009403) i, per tant, no hi ha una relació significativa.

# **4. Crear un histograma**
# Un histograma mostra la freqüència d'un interval específic en una sola columna.
# Exemple: Durada de les sessions d'entrenament.
df["Duration"].plot(kind='hist', bins=10)
plt.title("Histograma de la Durada de les Sessions")
plt.xlabel("Durada (minuts)")
plt.ylabel("Freqüència")
plt.show()

# Nota: El paràmetre `bins=10` especifica el nombre d'intervals (bins) que es mostraran a l'histograma.
# Cada bin representa un rang específic de valors, i l'histograma compta quants valors del conjunt de dades cauen dins de cada rang.
# Per exemple, si `bins=10`, els valors es dividiran en 10 intervals d'igual amplada basats en el mínim i el màxim de la columna seleccionada.

# **Consideracions:**
# - Els scatter plots són útils per identificar relacions entre dues variables.
# - Els histogrames són ideals per analitzar la distribució d'una única variable.
# - Els gràfics generats amb `plot()` són ràpids i senzills, però podem personalitzar-los amb les funcions de Matplotlib.
