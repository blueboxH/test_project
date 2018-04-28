''' websocket 避免验证ssl证书 '''
import websocket
import threading
import time
import json
import ssl

def on_message(ws, message):
    messages = json.loads(message)
    print('message', message)
    # for message in messages:
    #     if message.get('s') == 'BTCUSDT':
    #         # print(message)
    #         the_time = message.get('C') - message.get('O')
    #         print(the_time)

def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    print("ONOPEN")

    # def run(*args):
    #     d = {}
    #     ws.send(json.dumps(d))
    #     # ws.send(json.dumps({'command': 'subscribe', 'channel': 1002}))
    #     # ws.send(json.dumps({'command': 'subscribe', 'channel': 1003}))
    #     # ws.send(json.dumps({'command': 'subscribe', 'channel': 'BTC_XMR'}))
    #     # while True:
    #     #     time.sleep(1)
    #     # ws.close()
    #     print("_thread terminating...")
    # threading.Thread(target=run)


if __name__ == "__main__":
    websocket.enableTrace(True)
    # ws = websocket.WebSocketApp("wss://stream2.binance.com:9443/ws/!ticker@arr",
    ws = websocket.WebSocketApp("wss://stream2.binance.com:9443/ws/btcusdt@kline_1m",
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)
    ws.on_open = on_open
    kw = {}
    kw.update(sslopt={"cert_reqs": ssl.CERT_NONE})
    ws.run_forever(**kw)
