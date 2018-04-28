''' 测试线程锁 '''

import threading


def test():
    i = 0
    i = i + 1
    i = i - 1
    if i != 0:
        print(i)


def main():
    test()
if __name__ == '__main__':
    while True:
        threading.Thread(target=main).start()

