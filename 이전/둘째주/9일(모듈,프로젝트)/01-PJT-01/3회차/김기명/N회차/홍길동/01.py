with open('./data/fruits.txt', 'r', encoding='UTF8') as f:
    k = len(f.readlines())
with open('01.txt', 'w', encoding='UTF8') as w:
    w.write(str(k))