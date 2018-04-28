class test:

    @classmethod
    def test_class(cls):
        print('this is classmethod, the type is %s' % type(cls))

    @staticmethod
    def test_static():
        print('this is staticmethod')

    def test(self):
        print('this is instance method, the type is %s' % type(self))

    def test_func():
        print('this is functhon')

te = test()
if __name__ == '__main__':
    print('')
