import pymongo
from datetime import datetime
client = pymongo.MongoClient('18.216.72.11', 27017)

strart_time = datetime(2017, 12, 16, 0, 0)


db = client['_Bitfinex']

for col in db.collection_names():
    try:
        collection = db.get_collection(col)
        collection.delete_many({'_id': {'$gte': 151582830000}})
    except:
        pass

print('end...')
