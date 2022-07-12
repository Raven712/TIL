numbers = [0, 20, 100, 50, -60, 50, 2000, 150]
a = numbers[0]
for i in numbers:
    if i <= a:
        a = a
    else:
        a = i
print(a)