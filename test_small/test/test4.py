from multiprocessing import Process, Lock


def f(l, i):
    l.acquire()
    try:
        a = i
        print(a)
    finally:
        l.release()


if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
