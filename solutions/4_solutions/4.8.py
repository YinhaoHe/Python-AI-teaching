import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

# the histogram of the data
n, bins, patches = plt.hist(x, 50, density=True, facecolor='g', alpha=0.75)


plt.xlabel('x')
plt.ylabel('Probability')
plt.title('Normal Distribution')
plt.xlim(40, 160)
plt.ylim(0, 0.03)
plt.grid(True)
plt.show()