import os


username=os.getenv("MONGO_INITDB_ROOT_USERNAME", "IRGC")
password=os.getenv("MONGO_INITDB_ROOT_PASSWORD", "iraniraniran")
db = os.getenv("MONGO_INITDB_DATABASE", "IranMalDB")
collection = os.getenv("MONGO_COLLECTION", "tweets")

blacklist_path = r"C:\Users\user\Projects\Python\Malicious Text System\data\weapon_list.txt"