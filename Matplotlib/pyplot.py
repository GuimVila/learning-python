import matplotlib.pyplot as plt
import numpy as np

# **Introducció a Matplotlib**
# Matplotlib és una biblioteca de traçat gràfic que s'utilitza per crear visualitzacions de dades a Python.

# **El submòdul Pyplot**
# La majoria de les funcionalitats de Matplotlib es troben dins del submòdul `pyplot`. Aquest submòdul proporciona una interfície senzilla per crear i personalitzar gràfics.
# Per conveni, normalment s'importa sota l'àlies `plt`, com es mostra aquí:

# **Exemple bàsic de línia recta**
# Utilitzarem `numpy` per definir els punts d'eix X i Y, i `matplotlib` per traçar-los.

# Definim els punts de l'eix X i l'eix Y.
xpoints = np.array([0, 6])  # Punts en l'eix X
ypoints = np.array([0, 250])  # Punts en l'eix Y

# **1. Crear un gràfic de línia**
# Utilitzem `plt.plot()` per crear un gràfic de línia que connecta els punts definits.
plt.plot(xpoints, ypoints)

# **2. Mostrar el gràfic**
# Utilitzem `plt.show()` per visualitzar el gràfic generat.
plt.title("Gràfic de línia bàsic")
plt.xlabel("Eix X")
plt.ylabel("Eix Y")
plt.show()

# **Notes:**
# - Els punts `[0, 6]` i `[0, 250]` defineixen una línia recta que connecta els dos punts.
# - Aquesta és una de les maneres més simples d'utilitzar Matplotlib per traçar gràfics.
