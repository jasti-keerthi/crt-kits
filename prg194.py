# Vectorized Math
import numpy as np
a = np.array([1, 2, 3, 4, 5])
print("Original array:", a)
print("a + 10 =", a + 10)
print("a * 2 =", a * 2)
print("Square root =", np.sqrt(a))
print("Square =", np.square(a))
print("Clipped values =", np.clip(a, 2, 4))