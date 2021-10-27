"""
作业04 - 训练模型：soc -> 0-80

@author Aaric
@version 0.3.0-SNAPSHOT
"""
import numpy as np
import pymongo as pm
from keras.layers import Dense
from keras.models import Sequential
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# mongo object
mongo_client = pm.MongoClient("mongodb://10.0.11.50:27017")
mongo_db = mongo_client["ai"]
mongo_collection = mongo_db["signal_gb"]


# func load data
def load_data(vin, limit):
    soc_list = []
    condition_lte_80 = {
        # 车架号
        "vin": vin,
        # SOC范围：0-80，80-100
        "vehicleBaseData_soc": {
            "$lte": 80
        },
        # 车辆状态：1-启动，2-熄火，3-其他
        # "vehicleBaseData_vehicleStatus": 2,
        # 充电状态：1-停车充电，2-行驶充电，3-未充电，4-充电完成
        "vehicleBaseData_chargeStatus": 1
    }
    projection_soc = {
        "vin": 1,
        "collectTime": 1,
        "vehicleBaseData_soc": 1
    }
    rows = mongo_collection.find(condition_lte_80, projection=projection_soc).limit(limit).skip(1)
    for row in rows:
        soc_list.append(Soc(row["vin"], row["vehicleBaseData_soc"], int(row["collectTime"].timestamp())))
    print("load {0} records length: {1}".format(vin, len(soc_list)))
    return soc_list


# func split data
def split_data(arr, min_length=31):
    idx = [0]
    for i in range(0, len(arr) - 1):
        if arr[i] > arr[i + 1]:
            idx.append(i + 1)
    idx.append(len(arr))

    arr_list = []
    for i in range(0, len(idx) - 1):
        j = idx[i]
        k = idx[i + 1]
        arr_item = arr[j:k]
        # print(arr_item)
        if min_length <= len(arr_item):
            arr_list.append(arr_item)

    return arr_list


# func split matrix data
def split_matrix_data(arr, matrix_length=31):
    matrix_list = []
    for i in range(0, len(arr) - matrix_length):
        matrix_list.append(arr[i:i + 31])
    return matrix_list


# class soc
class Soc:
    def __init__(self, vin, value, seconds):
        self.vin = vin
        self.value = value
        self.seconds = seconds


# list vin
"""
vins = db_collection.distinct("vin", {
    # 指定车型
    "vehicleType": "EP22MCE",
    # 运行状态：1-纯电，2-混动，3-燃油
    "vehicleBaseData_runMode": 1
})
"""
vins = [
    # total: 1733618
    "TEST0000000000008",
    # total: 145782
    "TEST0000000000020",
    # total: 4562
    "TEST0000000000021",
    # total: 1243662
    "TEST0000000000023",
    # total: 1062969
    "TEST0000000000024",
    # total: 11844
    "TEST0000000000030",
    # total: 185882
    "TEST0000000000034"
]
print("vin list: {0}".format(vins))

# query socs (n>=100000)
soc_idx = 0
soc_total = 100000
soc_m2ds = []
for vin in vins:
    # load mongo records
    soc_records = load_data(vin, soc_total // len(vins))
    soc_lines = []
    for soc_record in soc_records:
        # print("{0}: {1} - {2}".format(soc.vin, soc.value, soc.seconds))
        soc_lines.append(soc_record.value)

    # convert linear array
    soc_split_lines = split_data(soc_lines)

    # convert matrix array
    for soc_split_line in soc_split_lines:
        split_matrix_data_list = split_matrix_data(soc_split_line)
        soc_m2ds.extend(split_matrix_data_list)
        soc_idx += len(split_matrix_data_list)
        print("{0} - {1}".format(soc_idx, soc_total))

    # convert break
    if soc_idx > soc_total:
        print("{0} - {1}, over!".format(soc_idx, soc_total))
        break

# convert train array
soc_features = []
soc_targets = []
for soc_m2d in soc_m2ds:
    soc_features.append(soc_m2d[0:-1])
    soc_targets.append(soc_m2d[-1:])

# train model score
x_data = np.asarray(soc_features).reshape(soc_idx, 30)
y_data = np.asarray(soc_targets)
x_train, x_test, y_train, y_test = train_test_split(x_data, y_data)
# print("train tts: {0}, {1}, {2}, {3}".format(x_train.shape, x_test.shape, y_train.shape, y_test.shape))
train_model = LinearRegression().fit(x_train, y_train)
train_score = train_model.score(x_test, y_test)
print("train score: {0}".format(train_score))

# train model loss
model = Sequential()
model.add(Dense(10, activation='relu', input_shape=(x_train.shape[1],)))
model.add(Dense(1))
model.compile(loss='mse', optimizer='rmsprop')
model.summary()
model.fit(x_train, y_train, batch_size=1000, epochs=256, validation_data=(x_test, y_test))

# train model save
model.save("model/ep22mce_soc_lte80.h5")
