''' 非阻塞方式 '''

import socket
import time


class Timekeeping:

    def __init__(self):
        self.temp = time.time()

    def __run(self):
        t1 = self.temp
        t2 = time.time()
        self.temp = t2
        return t2 - t1

    def get_interval(self):
        return self.__run()

    def print_interval(self):
        print('the interval is:', self.__run())

# aa = timekeeping()
# time.sleep(1)
# print(aa.get_time())
# time.sleep(2)
# print(aa.get_time())



def nonbloking_way():
    sock = socket.socket()
    sock.setblocking(False)
    try:
        sock.connect(('example.com', 80))
    except BlockingIOError:
        pass
    requests = 'GET / HTTP/1.0\r\nHost: example.com\r\n\r\n'
    data = requests.encode('ascii')
    while True:
        try:
            sock.send(data)
            break
        except OSError:
            pass

    response = b''
    while True:
        try:
            chunk = sock.recv(4096)
            while chunk:
                response += chunk
                chunk = sock.recv(4096)
            break
        except OSError:
            pass

def sync_way():
    res = []
    for i in range(10):
        res.append(nonbloking_way())
    return len(res)


timekeeping = Timekeeping()
sync_way()
timekeeping.print_interval()

