import matplotlib.pyplot as plt
import numpy as np

veri = np.random.rand(10, 10)

plt.figure(figsize=(7, 6))
plt.imshow(veri, cmap='hot')
plt.colorbar(label="Değer")
plt.title("Isı Haritası")
plt.show()