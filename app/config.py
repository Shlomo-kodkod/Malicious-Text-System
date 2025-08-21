import os


username=os.getenv("MONGO_INITDB_ROOT_USERNAME", "IRGC")
password=os.getenv("MONGO_INITDB_ROOT_PASSWORD", "iraniraniran")
cluster = os.getenv("MONGO_INITDB_CLUSTER", "IranMalDB.gurutam")
db = os.getenv("MONGO_INITDB_DATABASE", "IranMalDB")
collection = os.getenv("MONGO_COLLECTION", "tweets")

blacklist_path = r"data/weapon_list.txt"