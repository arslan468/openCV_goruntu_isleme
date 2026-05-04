import matplotlib.pyplot as plt
import numpy as np

# Rastgele normal dağılım verisi
veri = np.random.normal(170, 10, 1000)

plt.hist(veri, bins=30, color='purple',
         edgecolor='white', alpha=0.8)
plt.title("Boy Dağılımı")
plt.xlabel("Boy (cm)")
plt.ylabel("Frekans")
plt.show()