d = []
for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

for i in range(19):
    a = input().split()
    for j in range(19):
        d[i+1][j+1] = int(a[i])

for i in range(1, 20):
    for j in range(1, 20):




## 그냥 답지 보고 무슨말인지 겨우 읽는수준임