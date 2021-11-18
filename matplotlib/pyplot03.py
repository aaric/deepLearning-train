"""
Matplotlib - 图片

@author Aaric
@version 0.5.0-SNAPSHOT
"""

import matplotlib.pyplot as plt
from keras.datasets import mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

plt.figure()
for i in range(32):
    plt.subplot(4, 8, i + 1)
    plt.imshow(x_train[i])
    # plt.xticks([])
    # plt.yticks([])
plt.show()
