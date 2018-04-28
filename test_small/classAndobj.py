class test:
    te = True

t = test()
t2 = test()
print(t2.te)
test.te = False
print('t', t.te)
print(t2.te)
t3 = test()
print(t3.te)

