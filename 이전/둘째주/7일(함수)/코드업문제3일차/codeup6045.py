a, b, c = map(int,input().split())
slot = [a, b, c]
s = 0
for i in slot:
    s += 1

def avg(a, b, c):
    return ((a + b + c) / s)
    
print(a + b + c, format(avg(a, b, c),".2f"))