import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)

fig, axes = plt.subplots(1, 2, figsize=(12, 4))

# Sol grafik
axes[0].plot(x, np.sin(x), color='blue')
axes[0].set_title("Sinüs")

# Sağ grafik
axes[1].plot(x, np.cos(x), color='red')
axes[1].set_title("Kosinüs")

plt.tight_layout()
plt.show()