import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(-5, 5, 100)
y1 = x1**3 - 3*x1**2 + 3
plt.plot(x1, y1, color='green', linestyle='-')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Графік 1')
plt.show()

x2 = [1, 2, 3, 4, 5, 6]
y2 = [2, 4, 1, 5, 2, 6]
z2 = [5, 7, 1, 5, 4, 6]
plt.plot(x2, y2, color='cyan', linestyle='--', marker='o', mfc='blue', mec='blue', markersize=10, label='y')
plt.plot(x2, z2, color='black', linestyle=':', marker='o', mfc='black', mec='black', markersize=10, label='z')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.title('Графік 2')
plt.legend()
plt.show()

ages = [2, 5, 70, 40, 30, 45, 50, 45, 43, 40, 44, 60, 7, 13, 57, 18, 90, 77, 32, 21, 20, 40]
counts, bins, _ = plt.hist(ages, color='red', edgecolor='black')
plt.xlabel('Вік')
plt.ylabel('Частота')
plt.title('Графік 3')

max_idx = np.argmax(counts)
min_idx = np.argmin(counts)
bin_center_max = (bins[max_idx] + bins[max_idx + 1]) / 2
bin_center_min = (bins[min_idx] + bins[min_idx + 1]) / 2

plt.annotate('Max', xy=(float(bin_center_max), float(counts[max_idx])), xytext=(float(bin_center_max), float(counts[max_idx] + 1)), arrowprops=dict(arrowstyle="->"))
plt.annotate('Min', xy=(float(bin_center_min), float(counts[min_idx])), xytext=(float(bin_center_min), float(counts[min_idx] + 1)), arrowprops=dict(arrowstyle="->"))
plt.show()