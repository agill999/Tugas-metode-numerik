# ==========================================
# Soal 11.18 - Numerical Methods for Engineers
# Menentukan jumlah transistor, resistor,
# dan computer chip yang diproduksi
# ==========================================

import numpy as np

# Matriks koefisien
A = np.array([
    [4, 3, 2],
    [1, 3, 1],
    [2, 1, 3]
], dtype=float)

# Vektor konstanta
b = np.array([
    960,
    510,
    610
], dtype=float)

# Menyelesaikan sistem persamaan
x = np.linalg.solve(A, b)

print("=" * 40)
print("HASIL PRODUKSI")
print("=" * 40)
print(f"Transistor     : {x[0]:.0f}")
print(f"Resistor       : {x[1]:.0f}")
print(f"Computer Chip  : {x[2]:.0f}")
print("=" * 40)