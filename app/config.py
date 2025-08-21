import os


host=os.getenv("MONGO_HOST", "mongodb+srv")
username=os.getenv("MONGO_INITDB_ROOT_USERNAME", "IRGC")
password=os.getenv("MONGO_INITDB_ROOT_PASSWORD", "iraniraniran")
db = os.getenv("MONGO_INITDB_DATABASE", "IranMalDB")
collection = os.getenv("MONGO_COLLECTION", "tweets")