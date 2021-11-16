"""
作业03

@author Aaric
@version 0.3.0-SNAPSHOT
"""
import os
import numpy as np
import pymongo as pm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from keras.models import Sequential
from keras.layers import Dense

"""
mongo_client
"""
mongo_client = pm.MongoClient("mongodb://10.0.11.50:27017")
mongo_db = mongo_client["ai"]
db_collection = mongo_db["signal_gb"]
# print(db_collection)

"""
query socs (n>=100000)
"""
# condition and projection
n = 100000
query_condition = {
    # "vehicleType": "AS24",
    "vehicleBaseData_vehicleStatus": 1,  # 车辆状态：1-启动，2-熄火，3-其他
    "vehicleBaseData_chargeStatus": 3,  # 充电状态：1-停车充电，2-行驶充电，3-未充电，4-充电完成
    "vehicleBaseData_runMode": 1  # 运行状态：1-纯电，2-混动，3-燃油
}
query_projection = {
    "vin": 1,
    "vehicleBaseData_soc": 1
}

# query data
soc_items = []
data_rows = db_collection.find(query_condition, projection=query_projection).limit(n + 31).skip(1)
for row in data_rows:
    soc_items.append(row["vehicleBaseData_soc"])
print("soc_items len: ", len(soc_items))

"""
features and soc_targets
"""
soc_features = []
soc_targets = []
for i in range(0, n):
    j = i + 30
    k = i + 31
    soc_features.append(soc_items[i:j])
    soc_targets.append(soc_items[j:k])
print("soc_features len: ", len(soc_features))
print("soc_targets len:", len(soc_targets))

"""
train score
"""
x_data = np.asarray(soc_features).reshape(n, 30)
y_data = np.asarray(soc_targets)
# print(x_data)
# print(y_data)

x_train, x_test, y_train, y_test = train_test_split(x_data, y_data)
print("tts: ", x_train.shape, x_test.shape, y_train.shape, y_test.shape)

lr = LinearRegression()
train_model = lr.fit(x_train, y_train)

train_score = train_model.score(x_test, y_test)
print("score: ", train_score)

"""
train loss
"""
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(x_train.shape[1],)))
model.add(Dense(1))
model.compile(loss='mse', optimizer='rmsprop')
model.summary()
model.fit(x_train, y_train, batch_size=1000, epochs=256, validation_data=(x_test, y_test))
