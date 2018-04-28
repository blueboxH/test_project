
import time
import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError
class base:

    symbols = {
        'XBTUSD': 'BTC',
        "BCHZ17": "BCH/BTC",
        # "ETHZ17": "ETH/BTC",
        # "LTCZ17": "LTC/BTC",
        # "DASHZ17": "DASH/BTC",
        # "ZECZ17": "ZEC/BTC",
        # "ETCZ17": "ETC/BTC",
        # "XMRZ17": "XMR/BTC",
        # "XRPZ17": "XRP/BTC",
        # "XTZZ17": "XTZ/BTC",
    }
    # 假设value是列表, 就表明日期是动态的, 可以循环的
    # 若value是字符串, 则日期参数不能参与循环
    k_type = {
        'min': ['1', '604800'],
        '5mins': ['5', '432000'],
        'hour': ['60', '5871600'],
        'day': ['D', '13824000'],
    }

    matchup = {
        '{A}': 'symbols[car[1]]',
        '{B}': 'car[0]',
        '{C}': 'car[1]',
        '{D}': 'k_type[car[0]][0]',
        '{E}': 'str(start_time)',
        '{F}': 'str(end_time)'
    }


    def test_fun(self, tmp_url, end_time=None):


        #　循环k_type
        for type_key, type_value in self.k_type.items():

            # 循环symbols
            for sym_key, sym_value in self.symbols.items():
                if end_time is not None:
                    e_time = end_time

                res_key = '{}_{}'.format(sym_value, type_key)
                sym_url = tmp_url.replace(
                    '{SYMBOL}', sym_key).replace('{INTERVAL}', type_value[0])

                # 循环时间
                if isinstance(type_value, list) and end_time is not None:
                    while True: # 循环时间
                        s_time = e_time - int(type_value[1])
                        res_url = sym_url.replace('{STIME}', str(
                            s_time)).replace('{ETIME}', str(e_time))
                        status = yield res_key, res_url
                        if status == '404' or s_time < 0:
                            break
                        e_time = s_time

                else:
                    status = yield res_key, sym_url


tmp_url = "https://www.bitmex.com/api/udf/history?symbol={SYMBOL}&resolution={INTERVAL}&from={STIME}&to={ETIME}"
end_time = round(time.time())
def parse(rs):
    # s":"no_data
    if rs.get('s') == 'no_data':
        return True


gen = base().test_fun(tmp_url, end_time)
k, v = next(gen)
while True:
    try:
        resp = requests.get(v)
        resp.raise_for_status()
        res = parse(resp.json())
        if res:
            print(k, 'False:', v)
            k, v = gen.send('404')
        else:
            print(k, 'True:', v)
            k, v = gen.send(None)
    except (ConnectionError, Timeout) as err:
        
        pass
    except HTTPError as err:
        # 返回不成功的状态码, 放弃该请求
        break
    except StopIteration:
        # 生成器结束了, 这边也跟着结束
        gen.close()
        break
    except Exception as err:
        print(k, 'False:', v)
        print('='*60)
        print(err)
        print('='*60)
        k, v = gen.send('404')
        break

