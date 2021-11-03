"""
作业04 - 训练模型（综合）

@author Aaric
@version 0.4.0-SNAPSHOT
"""
import numpy as np
import pymongo as pm
from keras.layers import Dense
from keras.models import Sequential
from keras.models import load_model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split


class Soc:
    def __init__(self, mongo_uri: str = "mongodb://10.0.11.50:27017",
                 mongo_db_name: str = "ai",
                 mongo_collection_name: str = "signal_gb",
                 mongo_collection_object=None):
        self.mongo_uri = mongo_uri
        self.mongo_db_name = mongo_db_name
        self.mongo_collection_name = mongo_collection_name
        self.mongo_collection_object = mongo_collection_object

        if self.mongo_collection_object is None:
            mongo_client = pm.MongoClient(self.mongo_uri)
            mongo_db = mongo_client[self.mongo_db_name]
            self.mongo_collection_object = mongo_db["signal_gb"]

    @classmethod
    def split_data(cls, arr, min_length: int = 31):
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

    @classmethod
    def split_matrix_data(cls, arr, matrix_length=31):
        matrix_list = []
        for i in range(0, len(arr) - matrix_length):
            matrix_list.append(arr[i:i + 31])
        return matrix_list

    def load_vin_list(self, vehicle_type: str = "EP22MCE"):
        vin_list = self.mongo_collection_object.distinct("vin", {
            # 运行状态：1-纯电，2-混动，3-燃油
            # "vehicleBaseData_runMode": 1,
            # 指定车型
            "vehicleType": vehicle_type
        })
        return vin_list

    def load_soc_list(self, vin: str, gte: int = 0, lte: int = 80, limit: int = 100):
        print(vin, gte, lte, limit)
        soc_list = []
        custom_condition = {
            # 车架号
            "vin": vin,
            # SOC范围：0-80，80-100
            "vehicleBaseData_soc": {
                "$gte": gte,
                "$lte": lte
            },
            # 车辆状态：1-启动，2-熄火，3-其他
            # "vehicleBaseData_vehicleStatus": 2,
            # 充电状态：1-停车充电，2-行驶充电，3-未充电，4-充电完成
            "vehicleBaseData_chargeStatus": 1
        }
        custom_projection = {
            # "vin": 1,
            # "collectTime": 1,
            "vehicleBaseData_soc": 1
        }
        rows = self.mongo_collection_object.find(custom_condition, projection=custom_projection).limit(limit).skip(1)
        for row in rows:
            # soc_list.append(Soc(row["vin"], row["vehicleBaseData_soc"], int(row["collectTime"].timestamp())))
            soc_list.append(row["vehicleBaseData_soc"])
        print("load {0} records length: {1}".format(vin, len(soc_list)))
        return soc_list

    def get_train_data(self, vin_list, sample_total: int = 1000, soc_min: int = 0, soc_max: int = 80):
        # query socs (n>=100000)
        soc_sample_idx = 0
        soc_sample_total = sample_total
        soc_m2d_list = []
        print(soc_sample_total // len(vin_list))
        for vin in vin_list:
            # load mongo records
            soc_list = self.load_soc_list(vin, soc_min, soc_max, soc_sample_total // len(vin_list))
            print("soc_list", soc_list)
            soc_line_list = []
            for soc in soc_list:
                # print("{0}: {1} - {2}".format(soc.vin, soc.value, soc.seconds))
                # soc_lines.append(soc_record.value)
                soc_line_list.append(soc)

            # convert linear array
            print("soc_line_list", soc_line_list)
            soc_split_line_list = Soc.split_data(soc_line_list)

            # convert matrix array
            for soc_split_line in soc_split_line_list:
                split_matrix_list = Soc.split_matrix_data(soc_split_line)
                soc_m2d_list.extend(split_matrix_list)
                soc_sample_idx += len(split_matrix_list)
            print("convert {0} matrix details: {1} - {2}".format(vin, soc_sample_idx, soc_sample_total))

            # convert break
            if soc_sample_idx > soc_sample_total:
                print("{0} - {1}, over!".format(soc_sample_idx, soc_sample_total))
                break

        # convert train array
        soc_features = []
        soc_targets = []
        for soc_m2d in soc_m2d_list:
            soc_features.append(soc_m2d[0:-1])
            soc_targets.append(soc_m2d[-1:])

        # train data
        x_data = np.asarray(soc_features).reshape(soc_sample_idx, 30)
        y_data = np.asarray(soc_targets)

        # train test split
        return train_test_split(x_data, y_data)

    @classmethod
    def train_model_score(cls, x_train, x_test, y_train, y_test):
        train_model = LinearRegression().fit(x_train, y_train)
        train_score = train_model.score(x_test, y_test)
        print("train score: {0}".format(train_score))

    @classmethod
    def train_model_loss(cls, file_path: str, x_train, x_test, y_train, y_test):
        # train
        model = Sequential()
        model.add(Dense(10, activation='relu', input_shape=(x_train.shape[1],)))
        model.add(Dense(1))
        model.compile(loss='mse', optimizer='rmsprop')
        model.summary()
        model.fit(x_train, y_train, batch_size=1000, epochs=256, validation_data=(x_test, y_test))

        # save
        model.save(file_path)

    def save_lte80_model(self, file_path: str, vin_list, sample_total: int = 1000):
        # train data
        x_train, x_test, y_train, y_test = self.get_train_data(vin_list, sample_total, 0, 80)
        # print("train tts: {0}, {1}, {2}, {3}".format(x_train.shape, x_test.shape, y_train.shape, y_test.shape))

        # train model score
        Soc.train_model_score(x_train, x_test, y_train, y_test)

        # train model loss
        Soc.train_model_loss(file_path, x_train, x_test, y_train, y_test)

    def save_gte80_model(self, file_path: str, vin_list, sample_total: int = 1000):
        # train data
        x_train, x_test, y_train, y_test = self.get_train_data(vin_list, sample_total, 80, 100)
        # print("train tts: {0}, {1}, {2}, {3}".format(x_train.shape, x_test.shape, y_train.shape, y_test.shape))

        # train model score
        Soc.train_model_score(x_train, x_test, y_train, y_test)

        # train model loss
        Soc.train_model_loss(file_path, x_train, x_test, y_train, y_test)

    @classmethod
    def apply_model(cls, file_path: str, arr):
        x_data = np.array(arr).reshape(len(arr) // 30, 30)
        model = load_model(file_path)
        return model.predict(x_data)

    @classmethod
    def recursion2soc80(cls, model, arr, count=0):
        count += 1
        print(arr[-30:])
        x_data = np.array(arr[-30:]).reshape(1, 30)
        next_soc = int(model.predict(x_data)[0, 0])
        print("{0} -> {1}".format(count, next_soc))
        if 80 > model.predict(x_data):
            arr.append(next_soc)
            return Soc.recursion2soc80(model, arr, count)


if __name__ == "__main__":
    # 初始化Soc对象
    soc = Soc()

    # 查询符合条件的VIN列表
    # vins = soc.load_vin_list()
    vins = ["TEST0000000000008"]
    print("vin list: {0}".format(vins))

    # 导出训练模型：0-80
    soc_lte80_file_path = "model/ep22mce_soc_lte80.h5"
    # soc.save_lte80_model(soc_lte80_file_path, vins, 1000)

    # 应用训练模型：0-80
    soc_lte80_lines = [11, 11, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 12, 13, 13,
                       13,
                       13, 13,
                       13, 13, 13]
    print("next lte80 soc: {0}".format(Soc.apply_model(soc_lte80_file_path, soc_lte80_lines)))

    # 导出训练模型：80-100
    soc_gte80_file_path = "model/ep22mce_soc_gte80.h5"
    # soc.save_gte80_model(soc_gte80_file_path, vins, 1000)

    # 应用训练模型：80-100
    soc_gte80_lines = [91, 91, 91, 91, 91, 91, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 92, 93, 93,
                       93,
                       93, 93,
                       93, 93, 93]
    print("next gte80 soc: {0}".format(Soc.apply_model(soc_gte80_file_path, soc_gte80_lines)))

    # 递归预测
    soc_extra_lines = [27, 27, 27, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 28, 29, 29,
                       29,
                       29, 29,
                       29, 29, 29]
    app_model = load_model(soc_lte80_file_path)
    Soc.recursion2soc80(app_model, soc_extra_lines)
