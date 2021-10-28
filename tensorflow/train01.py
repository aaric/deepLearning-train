"""
作业01

@author Aaric
@version 0.1.0-SNAPSHOT
"""
import numpy as np
import pymongo as pm


class signal_gb:
    def __init__(self, uri="mongodb://127.0.0.1:27017", db_name="test"):
        self.client = pm.MongoClient(uri)
        self.db = self.client[db_name]
        self.collection = self.db["signal_gb"]

    def page(self, condition={}, projection={}, page_no=1, page_size=100):
        socs = []
        skip = page_size * (page_no - 1)
        for row in self.collection.find(condition, projection=projection).limit(page_size).skip(skip):
            socs.append(row["vehicleBaseData_soc"])
        return socs


sg = signal_gb("mongodb://10.0.11.50:27017", "ai")

# 1-3-1 -> 677169
condition = {
    "vehicleType": "AS24",
    "vehicleBaseData_vehicleStatus": 1,  # 车辆状态：1-启动，2-熄火，3-其他
    "vehicleBaseData_chargeStatus": 3,  # 充电状态：1-停车充电，2-行驶充电，3-未充电，4-充电完成
    "vehicleBaseData_runMode": 1  # 运行状态：1-纯电，2-混动，3-燃油
}
projection = {
    "vin": 1,
    "vehicleBaseData_soc": 1
}

# n >= 100000
# n = 100000, 1 - 30 & 100000 - 100030 + 1
# n = 1000, 1 - 30 & 1000 - 1030 + 1
# 此处改100000
n = 1000
m = n // 100
soc_temps = np.array([], dtype=int)

for i in range(1, m + 1):
    soc_temps = np.append(soc_temps, sg.page(condition, projection, i))
soc_temps = np.append(soc_temps, sg.page(condition, projection, m + 1, 31))

# 1031
# 此处为100031
print(soc_temps.size)

soc_features = np.array([], dtype=int)
soc_targets = np.array([], dtype=int)
for i in range(0, n):
    j = i + 30
    k = i + 31
    #     print(i, ":", j, ":", k)
    soc_features = np.append(soc_features, soc_temps[i:j])
    soc_targets = np.append(soc_targets, soc_temps[j:k])

print("feature_results: \n", soc_features.reshape(n, 30))
print("target_results: \n", soc_targets.reshape(n, 1))
