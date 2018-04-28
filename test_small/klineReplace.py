''' 用重复替换的方式取K线 '''
# import requests
# url = 'https://www.bitmex.com/api/udf/history?symbol=XBTUSD&resolution=1&from=1511342915&to=1511947715'
# resp = requests.get(url)
# res = resp.json()

# print(len(res.get('v')))


# coding=utf-8
import pprint
limit=1000
d = {
    'pairs_key': ['BTC','ETH' ],
    'from_key': ['10000','111111'],
    'hetao_key':['1','2']

}
e={'min':'shu_min','5mins':'shu_5mins'}

url = 'http://www.xx.com?pair=pairs_key&from=from_key&to=to_key&type=type_key&hetao=hetao_key'  # 初始url
urls=[]  # 最终结果
for type_key,type_value in {'min':60, '5mins':300}.items():
    tmps = []
    for key, value in d.items():
        if not tmps:
            tmps=[url]

        shu = []
        for u in tmps:

            for v in value:

                t=u.replace(key, v)  # 替换from_key
                # print(url)
                if key=='from_key':
                    # 判断k线间隔
                    to_key=int(v)+type_value*limit  # 计算出结束时间
                    t = t.replace('to_key', str(to_key)) #替换结束时间
                    t = t.replace('type_key', e.get(type_key))  # 替换k线标志
                shu.append(t)

        tmps=shu
    urls.extend(tmps)
pprint.pprint(urls)



