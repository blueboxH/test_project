import multiprocessing
def test(x):
    print(x*x)


p = multiprocessing.Pool()
p.map(test,[1,2])
p.join()
