import requests
from pyquery import PyQuery as pq


url = r'http://www.feixiaohao.com/exchange/hitbtc/'
res = requests.get(url)
res.raise_for_status()

def parse_data():
    doc = pq(res.text)
    items = doc.items('tbody > tr')
    lines = ['{\n']
    for item in items:
        td = item('td').eq(2).text()

        # >>>>>>>>>>>>这里是api需要的格式的数据<<<<<<<<
        # if not ('/RUR' in td or '/USD' in td):

        # 换位
        # pair = td.split('/')
        # pair = '-'.join(pair[::-1])

        pair = td.replace('/', '')
        line = '"{}": "{}",\n'.format(pair, td)
        lines.append(line)
    lines.append('}')
    return lines

with open('dict.json', 'w') as f:
    f.writelines(parse_data())

print('end...')
