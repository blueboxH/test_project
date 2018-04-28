import json
import requests
from requests.exceptions import ConnectionError, Timeout, HTTPError
from datetime import datetime, timedelta

class base:

    symbols = {
        'BTC-USD': 'BTC',
        # 'ETH-USD': 'ETH',
        # 'LTC-USD': 'LTC',
        # 'ETH-BTC': 'LTC/BTC',
        # 'LTC-BTC': 'LTC/BTC',
    }
    # 假设value是列表, 就表明日期是动态的, 可以循环的
    # 若value是字符串, 则日期参数不能参与循环
    k_type = {'min': ['60', 60, 800],
            '5mins': ['300', 300, 400],
            '15mins': ['900', 900, 400],
            '30mins': ['1800', 1800, 400],
            'hour': ['3600', 3600, 400],
            '3hours': ['10800', 10800, 400],
            '6hours': ['21600', 21600, 400],
            '12hours': ['43200', 43200, 400],
            'day': ['86400', 86400, 400],
            'week': ['604800', 604800, 400],
            'mon': ['2419200', 2419200, 400]
    }
    def test_fun(self, tmp_url, end_time=None):

        #　循环k_type
        for type_key, type_value in self.k_type.items():

            # 循环symbols
            for sym_key, sym_value in self.symbols.items():
                if end_time is not None:
                    e_time = end_time

                res_key = '{}_{}'.format(sym_value, type_key)
                sym_url = tmp_url.replace('{SYMBOL}', sym_key)

                # 循环时间
                if isinstance(type_value, list) and end_time is not None:
                    while True:  # 循环时间
                        sss = type_value[1] * int(type_value[2])
                        s_time = e_time - timedelta(seconds=sss)
                        res_url = sym_url.replace('{STIME}', str(
                            s_time.isoformat())).replace('{ETIME}', e_time.isoformat()).replace('{INTERVAL}', type_value[0])
                        status = yield res_key, res_url
                        if status == '404':
                            # 发送404退出时间循环
                            break
                        e_time = s_time - timedelta(seconds=type_value[1])

                else:
                    res_url = sym_url.replace('{INTERVAL}', type_value)
                    yield res_key, res_url


tmp_url = "https://api.gdax.com/products/{SYMBOL}/candles?start={STIME}&end={ETIME}&granularity={INTERVAL}"
end_time = datetime.now()


def parse(rs):
    # s":"no_data
    if not rs: # empty
        print('len', len(rs))
        return True
    else:
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
        print('=' * 60)
        print(err)
        print('=' * 60)
        k, v = gen.send('404')
        break
