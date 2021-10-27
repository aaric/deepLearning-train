"""
作业04 - 训练应用

@author Aaric
@version 0.3.0-SNAPSHOT
"""
import numpy as np
from keras.models import load_model

# train apply data
soc_lines = [11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13, 13, 13, 13,
             13, 13, 13]
x_data = np.array(soc_lines).reshape(1, 30)

# train model load
model = load_model("model/ep22mce_soc_lte80.h5")
print("next soc: {0}".format(int(model.predict(x_data)[0, 0])))
