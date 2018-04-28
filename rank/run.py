# encoding: utf-8
'''
入口程序, 每天0点更新排行数据
Created on 17/11/10/15:04

@author: hetao
'''
import time
from datetime import datetime
from exchangesRank import ExchangesRank
from currencyRank import CurrencyRank

while True:

    if datetime.now().hour == '16':
        CurrencyRank().run()
        ExchangesRank().run()
        # 休眠近24小时(减去程序运行的时间)
        time.sleep(24*3600-300)
    else:
        time.sleep(600)