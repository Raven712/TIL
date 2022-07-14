a = input()
mo = ['a', 'e', 'i', 'o' ,'u']
b = 0
for i in range(len(a)):
    if a[i] in mo:
        b += 1
print(b)