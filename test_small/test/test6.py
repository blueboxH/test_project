#!/usr/bin/python3
# encoding: utf-8
# @Time    : 2017/12/19 0019 11:41
# @author  : zza
# @Email   : 740713651@qq.com
import pymongo

mongoDB = pymongo.MongoClient("127.0.0.1", 27017)
# 获得交易所列表
ex_list = []
for i in mongoDB["History_exchange"]["exchanges"].find():
    ex_list.append(i["name"])

for ex in ex_list:
    # 获得每个交易所的币种
    cu_list = mongoDB[ex].collection_names()
    for cu in cu_list:
        items = mongoDB[ex][cu].find()
        f = open('./' + ex + "." + cu + ".dat", "w+")
        for i in items:
            print(i)
            # f.write(i)
        f.close()
