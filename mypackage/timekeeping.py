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


if __name__ == '__main__':
    aa = Timekeeping()
    time.sleep(1)
    print(aa.print_interval())
    time.sleep(2)
    print(aa.print_interval())
