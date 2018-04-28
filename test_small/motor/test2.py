from motor.motor_tornado import MotorClient
from tornado.ioloop import IOLoop
from tornado import gen
import timeit
import asyncio
import pymongo
import time

client = MotorClient()
db = client.test


async def test():
    for i in range(200):
        result = await db.test.update_one({'i': i}, {'$set': {'i': i}}, True)
        print('do_insert_with_async', result)
        if i ==1:
            for j in range(1000000):
                j*j
            print('@'*10000, i)
loop.run_until_complete(test())
print('end..')
