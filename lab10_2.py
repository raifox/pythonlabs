import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100)

fig, axs = plt.subplots(2, 2)

axs[0, 0].plot(x, x**2)
axs[0, 0].set_title('y = x^2')

axs[0, 1].plot(x, x**3)
axs[0, 1].set_title('y = x^3')

axs[1, 0].plot(x, x**4)
axs[1, 0].set_title('y = x^4')

axs[1, 1].plot(x, x**5)
axs[1, 1].set_title('y = x^5')

plt.tight_layout()
plt.show()