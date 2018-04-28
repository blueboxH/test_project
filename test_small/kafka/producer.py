from kafka import KafkaProducer, RoundRobinPartitioner

import json
import random


class MyDefaultPartitioner(object):
    @classmethod
    def __call__(cls, key, all_partitions, available):
        print(dir(cls))
        if available:
            return random.choice(available)
        return random.choice(all_partitions)

producer = KafkaProducer(
    bootstrap_servers=['192.168.14.240:9093'],
    value_serializer=lambda m: json.dumps(m).encode('utf8'),
    key_serializer=str.encode,
    compression_type='gzip',
    partitioner=RoundRobinPartitioner()
    )



while True:
    str_ = input('please input: ')
    producer.send('Kline', value=str_, key='asd')
print('END')
