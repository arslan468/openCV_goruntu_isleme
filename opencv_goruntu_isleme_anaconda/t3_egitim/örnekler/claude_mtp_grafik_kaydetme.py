import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 3, 8]
plt.plot(x, y)
plt.title("Grafik")

# Kaydet (show()'dan ÖNCE yap!)
plt.savefig("grafik.png", dpi=150,
             bbox_inches='tight')
plt.show()