"""
顺序模型

@author Aaric
@version 0.5.0-SNAPSHOT
"""

import matplotlib.pyplot as plt
import numpy as np
from keras.layers import Dense
from keras.models import Sequential

# 训练数据
x_data = np.random.random(100)
y_data_noise = np.random.normal(0, 0.01, x_data.shape)
y_data = x_data * 0.1 + 0.2 + y_data_noise

# 顺序模型
model = Sequential()
# 增加一个全连接层
model.add(Dense(units=1, input_dim=1))
# 均方误差
model.compile(optimizer="sgd", loss="mse")

# 训练3001个批次
for count in range(3001):
    loss = model.train_on_batch(x_data, y_data)
    if count % 500 == 0:
        print("loss: {0}".format(loss))

# 打印权值和偏置值
w, b = model.layers[0].get_weights()
print("w: {0}, b: {1}".format(w, b))

# 预测数据
y_rst = model.predict(x_data)
# print("y_rst: {0}".format(y_rst))

# 数据图形化
plt.scatter(x_data, y_data)
plt.plot(x_data, y_rst, "red", lw=3)
plt.show()
