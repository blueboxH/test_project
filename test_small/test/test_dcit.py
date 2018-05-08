def main(di, li):
    k = li.pop(0)
    if len(li) == 1:
        di[k] = li[0]
        return
    item = di.get(k)
    if not isinstance(item, dict):
        di[k] = item = {}
    main(item, li)

if __name__ == '__main__':
    di = {
        'k1': 1,
        'k2': {
            3: 3,
            'k4': 4
        }
    }
    li = ['k2', 3, 'k4', 'k5']
    main(di, li)
    print(di)
