from motor.motor_tornado import MotorClient
from tornado.ioloop import IOLoop
import timeit
import asyncio
import pymongo
import time
clinet1 = pymongo.MongoClient()
db1 = clinet1.test

client = MotorClient()
db = client.test
loop = asyncio.get_event_loop()


async def test():
    for i in range(2000):
        result = await db.test.update_one({'i': i}, {'$set': {'i':i}}, True)
        print('do_insert_with_async', i, result)


def insert_one():
    for i in range(2000):
        result = db1.test.update_one({'i': i}, {'$set': {'i': i}}, True)
        print('insert_one',i,  result)


t = time.time()
insert_one()
t1 = time.time()
IOLoop.current().run_sync(test)
t2 = time.time()

print('time1', t1-t)
print('time2', t2-t1)
