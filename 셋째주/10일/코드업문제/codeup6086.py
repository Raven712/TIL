a = int(input())
b = 0
total = 0
while total < a:
    b = b + 1
    total = total + b
    if total >= a:
        print(total)
        break