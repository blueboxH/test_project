# encoding: utf-8
'''
抓取交易所的排名, 以及此交易所下币的单价和交易额
Created on 17/11/9/9:52

@author: hetao
'''

import threading
import queue

from pyquery import PyQuery as pq

from utils import *

import settings

class ExchangesRank:
    # 消费者线程数量
    customer_num = 10
    que = queue.Queue(20)
    con = ConnectionRedis(db=settings.REDIS_NAME, host=settings.REDIS_HOST,port=settings.REDIS_PORT).con

    def parse_html(self, html):
        """解析html页面, 提取数据"""
        doc = pq(html)
        totals = doc(".bold.volume").items()
        headers = doc('.volume-header').items()
        for header, total in zip(headers, totals):
            try:
                # 交易所总交易额
                total = total.text().replace(',', '')[1:]
                # 排名
                rank = header.text().split('.')[0].strip()
                # 交易所名字
                name = header.text().split('.')[1].strip()
                # 货币信息页面的url
                url = header('a').make_links_absolute("https://coinmarketcap.com/").attr('href')
                self.que.put({'name': name, 'rank': rank, 'total': total, 'url': url})
            except Exception as err:
                print('解析html页面出错:', err)


    def parse_currency_html(self, html):
        """解析货币详情页面, 获取每个交易所货币的排序及详细信息"""
        doc = pq(html)
        trs = doc.items('tr')
        next(trs)    # 去掉表头
        currencies = {}
        for tr in trs:
            try:
                # 货币名
                curr_name = tr('td').eq(2).text().split('/')[0].strip()
                # 此交易所货币交易额
                volume = tr('td').eq(3).text().split('$')[-1].replace(',', '')
                # 货币单价
                price = tr('td').eq(4).text().split('$')[-1].replace(',', '')
                if curr_name in currencies:
                    volume_flo = str(float(currencies[curr_name][1]) + float(volume))
                    volume = volume_flo[:-2] if volume_flo.endswith('.0') else volume_flo
                currencies.update({curr_name: [price, volume]})
            except Exception as err:
                print('解析货币详情页出错:', err)
        return currencies

    def consume(self):
        """从队列里取出数据, 拿到url爬取货币排序并入库"""
        while True:
            data = self.que.get()
            if data is None:
                break
            url = data.get('url')
            resp = get_html(url)
            data.update(currencies = self.parse_currency_html(resp.text))
            del data['url']
            key = data.pop('name')
            CacheDataHelper(self.con).add("rankExchanges", key, data)
            self.que.task_done()

    def run(self):
        # 启动消费者
        customers = []
        for x in range(self.customer_num):
            customer = threading.Thread(target=self.consume)
            customers.append(customer)
            customer.start()

        # 启动生产者产生待爬取url
        url = r'https://coinmarketcap.com/exchanges/volume/24-hour/'
        resp = get_html(url)
        self.parse_html(resp.text)

        # 生产完毕, 将结束信号插入队列
        self.que.join()
        for y in range(self.customer_num):
            self.que.put(None)

        # 结束消费者
        for customer in customers:
            customer.join()
        print('exchangesRank end...')

if __name__ == '__main__':
    ExchangesRank().run()