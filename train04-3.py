"""
作业04 - 训练应用

@author Aaric
@version 0.3.0-SNAPSHOT
"""
import numpy as np
from keras.models import load_model


# 0-80: load model and predict
def next_soc_lte80(arr):
    x_data = np.array(soc_lines).reshape(len(arr) // 30, 30)
    model = load_model("model/ep22mce_soc_lte80.h5")
    return model.predict(x_data)


# 0-80: train apply model
soc_lines = [11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13,
             13, 13, 13]
print("next soc: {0}".format(int(next_soc_lte80(soc_lines)[0, 0])))


# 0-80: load model and predict
def next_soc_gte80(arr):
    x_data = np.array(soc_lines).reshape(len(arr) // 30, 30)
    model = load_model("model/ep22mce_soc_gte80.h5")
    return model.predict(x_data)


# 0-80: train apply model
soc_lines = [91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 93, 93, 93, 93, 93,
             93, 93, 93]
print("next soc: {0}".format(int(next_soc_gte80(soc_lines)[0, 0])))
