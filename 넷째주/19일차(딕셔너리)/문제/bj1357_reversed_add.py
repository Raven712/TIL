x, y = map(int,(input().split()))

def rev(x):
    return int(str(x)[::-1])

print(rev(rev(x) + rev(y)))