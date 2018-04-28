import pymongo

cli = pymongo.MongoClient()
col = cli.test.test
try:
    res = col.update_one({'_id':1}, {'$set':{'_id': 1, 'v': 'tes'}},
         True)
    rs = col.update_one({'_id': 5}, {'$set': {'_id': 5, 'v': 'test'}},
                         True)
    print(dir(res))

except pymongo.errors.BulkWriteError as e:
    print(e.details['writeErrors'])
