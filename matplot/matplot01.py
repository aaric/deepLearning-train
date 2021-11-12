"""
Matplotlib - 直线

@author Aaric
@version 0.5.0-SNAPSHOT
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 100)
y = 2 * x + 1
plt.plot(x, y)
plt.show()
