''' 可以任意添加的笛卡尔积 '''

import pppytrint
limit = 1000
d = {
    'pairs_key': ['BTC', 'ETH'],
    'from_key': ['10000', '111111'],
    'hetao_key': ['1', '2']

}
e = {'min': 'shu_min', '5mins': 'shu_5mins'}

urls = []
for type_key, type_value in {'min': 60, '5mins': 300}.items():
    tmps = ['http://www.xx.com?pair=pairs_key&from=from_key&to=to_key&type=type_key&hetao=hetao_key']
    for key, value in d.items():
        while True:
            url = tmps[0]
            if key not in url:
                break
            tmps.remove(url)

            for v in value:

                t = url.replace(key, v)  # 替换from_key
                if key == 'from_key':  # 判断k线间隔
                    to_key = int(v) + type_value * limit  # 计算出结束时间
                    t = t.replace('to_key', str(to_key))  # 替换结束时间
                    t = t.replace('type_key', e.get(type_key))  # 替换k线标志
                tmps.append(t)
    urls.extend(tmps)
pprint.pprint(urls)
print(len(urls))
