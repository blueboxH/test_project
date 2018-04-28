import json
import requests
import redis
from requests import RequestException


def get_html(url, *args, **kwargs):
    """获取网页"""
    try:
        resp = requests.get(url, *args, **kwargs)
        resp.raise_for_status()
        # resp.encoding = resp.apparent_encoding
        if resp is not None:
            return resp
    except RequestException as err:
        print('获取页面错误', err)


class ConnectionRedis(object):
    """ Get the redis connection object """
    def __init__(self, db=0, host='localhost', port=6379):
        super(ConnectionRedis, self).__init__()

        # 注意: 就算给定的host和port不能连接, 此处也不会发生异常
        # 只有当使用_con去做操作时, 才会发生ConnectionError异常
        self._con = redis.StrictRedis(host=host, port=port, db=db)

    @property
    def con(self):
        return self._con


class CacheDataHelper():

    def __init__(self, con):
        self.con = con

    def add(self, key, field, value):
        """ 注意 field值为 ip_taskid """
        return self.con.hset(key, field, json.dumps(value))
