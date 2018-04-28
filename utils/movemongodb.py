""" 从一个数据库读数据写到另一个数据库， 实现数据库的迁移 """

resdb = pymongo.MongoClient('172.31.27.160', 27017)
todb = pymongo.MongoClient('172.31.5.32', 27017)
for database in resdb.database_names():
    for table_name in resdb[database].collection_names():
        try:
            item = resdb[database][table_name].find():
            todb[database][table_name].insert_many(item)
        except:
            pass


████████████████████████████████