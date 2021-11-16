"""
MINIST数据集

@author Aaric
@version 0.5.0-SNAPSHOT
"""

from keras.datasets import mnist
from keras.layers import Dense
from keras.models import Sequential
from keras.utils.np_utils import to_categorical

(x_train, y_train), (x_test, y_test) = mnist.load_data()
print("x_train -> {0} : {1}, y_train -> {2}".format(x_train.shape, len(x_train), y_train))
print("x_test  -> {0} : {1}, y_test  -> {2}".format(x_test.shape, len(x_test), y_test))

network = Sequential()
network.add(Dense(512, activation="relu", input_shape=(28 * 28,)))
network.add(Dense(10, activation="softmax"))

network.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"])

x_train = x_train.reshape((60000, 28 * 28))
x_train = x_train.astype("float32") / 255
y_train = to_categorical(y_train)

x_test = x_test.reshape((10000, 28 * 28))
x_test = x_test.astype("float32") / 255
y_test = to_categorical(y_test)

network.fit(x_train, y_train, epochs=5, batch_size=128)

loss, metrics = network.evaluate(x_test, y_test)
print("loss: {0}, metrics: {1}".format(loss, metrics))
