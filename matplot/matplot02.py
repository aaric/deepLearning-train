"""
Matplotlib - 散点图

@author Aaric
@version 0.5.0-SNAPSHOT
"""

import matplotlib.pyplot as plt
import numpy as np

x_data = np.random.random(100)
y_data_noise = np.random.normal(0, 0.01, x_data.shape)
y_data = x_data * 0.1 + 0.2 + y_data_noise

plt.scatter(x_data, y_data)
plt.show()
