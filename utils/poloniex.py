''' 生成id和交易对的匹配关系 '''

import requests


url = 'https://poloniex.com/public?command=returnTicker'
proxies = {
    'http': 'socks5://127.0.0.1:9999',
    'https': 'socks5://127.0.0.1:9999'
}

resp = requests.get(url, proxies=proxies).json()
datas = {k: '/'.join(k.split('_')[::-1]).replace('/USDT', '') for k in resp.keys()}
# datas = {str(v['id']):'/'.join(k.split('_')[::-1]).replace('/USDT', '') for k, v in resp.items()}
print(datas)
with open('poloniex.jsonself.set_pairs()', 'w', ) as f:
    f.writelines(datas)

