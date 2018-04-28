def comsumer():
    r = ''
    k = ''
    while True:
        n, m, q = yield r, k
        if not n:
            return
        print(n, m, q)
        # print('[CONSUMER] consuming %s' % n)
        r = '200 OK'


