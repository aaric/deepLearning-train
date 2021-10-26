"""
作业04 - 终结

@author Aaric
@version 0.3.0-SNAPSHOT
"""
import pymongo as pm

# mongo object
mongo_client = pm.MongoClient("mongodb://10.0.11.50:27017")
mongo_db = mongo_client["ai"]
mongo_db_collection = mongo_db["signal_gb"]


# func soc
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
    rows = mongo_db_collection.find(condition_lte_80, projection=projection_soc).limit(limit).skip(1)
    for row in rows:
        soc_list.append(Soc(row["vin"], row["vehicleBaseData_soc"], int(row["collectTime"].timestamp())))
    print("soc_items len: ", len(soc_list))
    return soc_list


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
n = 1000
socs = load_data("TEST0000000000021", n)
for soc in socs:
    print("{0}: {1} - {2}".format(soc.vin, soc.value, soc.seconds))
