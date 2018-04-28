import json
import time

import websocket


def on_open(ws):
    print('on_open')
    d = {
        "type": "subscribe",
        "channel": "btc_jpy-trades"
    }

    ws.send(json.dumps(d))


def on_message(ws, message):
    message = json.loads(message)
    print(message)


# url = "wss://stream2.binance.com:9443/ws/trxbtc@kline_1m"
url = "wss://ws-api.coincheck.com/"
websocket.enableTrace(True)
ws = websocket.WebSocketApp(url, on_open=on_open, on_message=on_message)

# ws.run_forever(http_proxy_host='127.0.0.1', http_proxy_port=8381)
ws.run_forever()
