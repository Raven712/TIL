with open('./data/fruits.txt', 'r', encoding='UTF8') as f:
    a = f.read()
    b = a.split()
    c = {}
    for i in b:
        c[i] = c.get(i, 0) + 1
        keys = sorted(c.keys())
for i in keys:
    print(i + ':' + str(c[i]))