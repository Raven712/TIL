with open('00.txt', 'w', encoding = 'UTF8') as w:
    w.write('3회차 김기명\nHello, Python\n')
    for i in range(1,6):
        w.write(f'{i}일차 파이썬 공부 중\n')
with open('00.txt', 'r', encoding = 'UTF8') as r:
    print(r.read())