import numpy as np

# **Hyperbolic Functions in NumPy**
# NumPy proporciona les funcions hiperbòliques `sinh()`, `cosh()` i `tanh()`.
# Aquestes funcions prenen valors en radians i retornen els valors corresponents de sinus, cosinus i tangent hiperbòlics.

# **1. Hyperbolic Sine**
# Exemple: Trobar el valor de sinh(π/2).
sinh_pi_half = np.sinh(np.pi / 2)
print("Hyperbolic sine of π/2:", sinh_pi_half)
# Resultat esperat: 2.3012989023072947

# **2. Hyperbolic Cosine**
# Exemple: Trobar els valors de cosh per a múltiples angles.
angles_radians = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
cosh_values = np.cosh(angles_radians)
print("Hyperbolic cosine values:", cosh_values)
# Resultat esperat: [2.50917848 1.60028686 1.32460909 1.16244735]

# **3. Finding Angles from Hyperbolic Values**
# Exemple: Trobar l'angle per a un valor de sinh (arcsinh).
angle_from_sinh = np.arcsinh(1.0)
print("Angle for sinh(1):", angle_from_sinh)
# Resultat esperat: 0.881373587019543

# **4. Angles for Multiple Hyperbolic Values**
# Exemple: Trobar els angles corresponents per a múltiples valors de tanh (arctanh).
tanh_values = np.array([0.1, 0.2, 0.5])
angles_from_tanh = np.arctanh(tanh_values)
print("Angles for tanh values:", angles_from_tanh)
# Resultat esperat: [0.10033535 0.20273255 0.54930614]
