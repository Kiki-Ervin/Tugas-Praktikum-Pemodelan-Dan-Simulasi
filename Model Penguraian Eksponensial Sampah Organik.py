#import pandas as pd
#import matplotlib as pit
#import numpy as py

import numpy as np
import matplotlib.pyplot as plt

# Parameter
S0 = 5  # Massa sampah awal (kg)
k = 0.05  # Laju penguraian
t = np.linspace(0, 100, 500)  # Waktu dari 0 hingga 100 hari

# Fungsi penguraian sampah
S = S0 * np.exp(-k * t)

# Plot
plt.figure(figsize=(10, 6))
plt.plot(t, S, label='Massa Sampah (S)', color='brown')
plt.title('Model Penguraian Sampah Organik')
plt.xlabel('Waktu (hari)')
plt.ylabel('Massa Sampah (kg)')
plt.grid()
plt.axhline(S0, color='gray', linestyle='--', label='Sampah Awal (5 kg)')
plt.legend()
plt.show()
