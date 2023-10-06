list_ = []
for i in range(9):
    N = int(input())
    list_.append(N)

dw = sorted(list_) #오름차순이라길래

sum_ = 0
stop = True
for a in range(9):
    for b in range(a + 1, 9):
        for c in range(b + 1, 9):
            for d in range(c + 1, 9):
                for e in range(d + 1, 9):
                    for f in range(e + 1, 9):
                        for g in range(f + 1, 9):
                            if dw[a]+dw[b]+dw[c]+dw[d]+dw[e]+dw[f]+dw[g] == 100:
                                print(dw[a])
                                print(dw[b])
                                print(dw[c])
                                print(dw[d])
                                print(dw[e])
                                print(dw[f])
                                print(dw[g])
                                stop = False
                                break
                        if stop == False:
                            break
                    if stop == False:
                        break
                if stop == False:
                    break
            if stop == False:
                break
        if stop == False:
            break
    if stop == False:
        break
        
        #이게맞네