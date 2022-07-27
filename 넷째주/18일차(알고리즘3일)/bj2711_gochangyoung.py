T = int(input())

for i in range(1, T + 1):
    loca, typ = input().split()
    loca = int(loca)

    list_ = list(typ)
    list_[loca - 1] = ''
    print(''.join(list_))