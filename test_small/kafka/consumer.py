from kafka import KafkaConsumer
consumer = KafkaConsumer(
    'Kline',
    group_id='klinetest',
    bootstrap_servers=['192.168.14.240:9093'],
    auto_offset_reset='earliest',
    # enable_auto_commit=True,
    # api_version=(0, 10),
)

while True:
    print('start')
    message =next(consumer)
    print(message)
