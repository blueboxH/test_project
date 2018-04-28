''' websocket test '''
import json
import websocket
import time
import ssl
import asyncio
import gzip
def on_open(ws):
    pair = 'btc_usd'
    d = {
        'event': 'addChannel',
        'channel': 'ok_sub_spot_{}_deals'.format(pair)
    }
    # print('on_open')
    # d = [1, "orderbook", "ETHBTC"]
    # # d = '{"op": "subscribe", "args": ["trade": ["ETHXBT","LTCXBT","DASHXBT","ZECXBT","ETCXBT","XMRXBT","XRPXBT",XTZXBT"]]}'
    ws.send(json.dumps(d))


# x =
def on_message(ws, message):
    # message = json.loads(message)
    # asyncio.sleep(100)
    # message = gzip.decompress(message).decode('utf-8')
    print('message', message, type(message))
    if 'pong' not in message:
        ws.send("{'event':'ping'}")
        print('send ping')

    # ws.send("{'event':'ping'}")
    # the_time = int(message.get('date')[:-3])
    # print(time.localtime(the_time))


def on_ping(ws, message):
    while 1:
        ws.send("{'event':'ping'}")
        print('send')
        time.sleep(30)
    print('on ping ', ws, message)


def on_pong(ws, message):
    print('on ping ', ws, message)


url = 'wss://real.okcoin.com:10440/websocket'
websocket.enableTrace(True)
ws = websocket.WebSocketApp(
    url, on_open=on_open, on_message=on_message)
# run_forever_kwargs.update(sslopt={"cert_reqs": ssl.CERT_NONE})
# ws.run_forever(http_proxy_host='127.0.0.1', http_proxy_port=9999)
ws.run_forever()

# 禁止ssl验证证书


# redis中添加symbol信息表

print('end...')
