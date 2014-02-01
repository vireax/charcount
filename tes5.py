import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.1);
y = np.sin(x);
plt.plot(x, y);
#plt.hist(y, bins=30)
#num_bins = 50
#n, bins, patches = plt.hist(y, num_bins, normed=1, facecolor='green', alpha=0.5)
plt.show()
