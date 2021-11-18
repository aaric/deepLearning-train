"""
Matplotlib - 组合图像

@author Aaric
@version 0.5.0-SNAPSHOT
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 1, 100)
y1 = 2 * x + 1
y2 = x ** 2

# 弹出2个对话框
# plt.figure()
# plt.plot(x, y1)

# plt.figure(figsize=(5, 5))
# plt.plot(x, y2)

# 合并，仅弹出1个对话框
plt.plot(x, y1, color="red", linewidth=1.0, linestyle="--")
plt.plot(x, y2, color="blue", linewidth=2.0, linestyle="-")

plt.show()
