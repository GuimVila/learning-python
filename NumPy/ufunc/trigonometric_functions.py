# trig_operations.py

import numpy as np

# **Trigonometric Functions in NumPy**
# NumPy ofereix funcions trigonomètriques com `sin()`, `cos()` i `tan()` que
# prenen valors en radians i produeixen els valors trigonomètrics corresponents.

# **1. Sine of a Single Value**
# Exemple: Trobar el valor del sinus de π/2.
sin_pi_half = np.sin(np.pi / 2)
print("Sine of π/2:", sin_pi_half)  # Resultat: 1.0

# **2. Sine of Multiple Values**
# Exemple: Trobar els valors del sinus per un array de valors en radians.
angles_radians = np.array([np.pi / 2, np.pi / 3, np.pi / 4, np.pi / 5])
sine_values = np.sin(angles_radians)
print("Sine values for angles in radians:", sine_values)
# Resultat: [1.         0.8660254  0.70710678 0.58778525]

# **3. Convert Degrees to Radians**
# Les funcions trigonomètriques treballen amb radians, però podem convertir graus a radians.
# Fórmula: radians = (π/180) * graus.
angles_degrees = np.array([90, 180, 270, 360])
angles_radians_converted = np.deg2rad(angles_degrees)
print("Angles in radians (from degrees):", angles_radians_converted)
# Resultat: [1.57079633 3.14159265 4.71238898 6.28318531]

# **4. Convert Radians to Degrees**
# Exemple: Convertir valors en radians a graus.
angles_radians_array = np.array([np.pi / 2, np.pi, 1.5 * np.pi, 2 * np.pi])
angles_degrees_converted = np.rad2deg(angles_radians_array)
print("Angles in degrees (from radians):", angles_degrees_converted)
# Resultat: [ 90. 180. 270. 360.]

# **5. Finding Angles from Trigonometric Values**
# Exemple: Trobar l'angle per a un valor de sinus (arcsin).
angle_from_sine = np.arcsin(1.0)
print("Angle for sin(1):", angle_from_sine)  # Resultat: 1.5707963267948966 (π/2)

# Exemple: Trobar angles per a múltiples valors de sinus.
sine_values_array = np.array([1, -1, 0.1])
angles_from_sine = np.arcsin(sine_values_array)
print("Angles for sine values:", angles_from_sine)
# Resultat: [ 1.57079633 -1.57079633  0.10016742]

# **6. Finding the Hypotenuse Using Pythagoras Theorem**
# Exemple: Trobar la hipotenusa donats la base i el perpendicular.
# Fórmula: hipotenusa = sqrt(base² + perpendicular²)
base_length = 3
perpendicular_length = 4
hypotenuse = np.hypot(base_length, perpendicular_length)
print("Hypotenuse:", hypotenuse)  # Resultat: 5.0
