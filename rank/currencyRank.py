# encoding: utf-8
'''
抓取货币的排名信息

Created on 17/11/10/9:35

@author: hetao
'''
from pyquery import PyQuery as pq

from utils import *

import settings

class CurrencyRank:

    con = ConnectionRedis(db=settings.REDIS_NAME, host=settings.REDIS_HOST, port=settings.REDIS_PORT).con

    def parse_html(self, html):
        """解析html页面, 获取目标数据"""
        doc = pq(html)
        trs = doc('tbody tr')
        # 把结果倒序, 这样rank较小的数据就会覆盖rank较大的数据
        trs.reverse()
        for tr in trs.items():
            try:
                # 货币排名
                rank = tr('td:first-child').text()
                # 货币名字
                name = tr('.currency-name-container').text()
                # 货币简称
                symbol = tr('.col-symbol').text()
                # 市值(单位美元)
                market_cap = tr('.market-cap').text().replace('$', '').replace(',', '')
                # 单价(单位美元)
                price = tr('.price').text().replace('$', '')
                # 市场流通货币的数量
                circulating_supply = tr('.circulating-supply a').text().replace(',', '')
                # 24小时交易量(单位美元)
                volume = tr('.volume').text().replace('$', '').replace(',', '')
                # 24小时涨幅(单位%)
                increase = tr('.percent-24h').text()

                # 数据存入redis
                res = CacheDataHelper(self.con).add("rankCurrency", symbol, {
                    'rank': rank,
                    'name': name,
                    'market_cap': market_cap if market_cap != "?" else None,
                    'price': price if price != "?" else None,
                    'num': circulating_supply if circulating_supply != "?" else None,
                    'volume': volume if volume != "?" else None
                })
                if res == 0:
                    print(name, 'failed, and rank is', rank)
            except Exception as err:
                print('解析html页面错误', err)

    def run(self):
        url = r'https://coinmarketcap.com/all/views/all/'
        resp = get_html(url)
        self.parse_html(resp.text)
        print('currencyRank end...')

if __name__ == '__main__':
    CurrencyRank().run()