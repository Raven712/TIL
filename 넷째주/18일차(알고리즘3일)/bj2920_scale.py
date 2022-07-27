music = list(map(int, input().split()))

if music == list(range(1, 9)):
    print('ascending')

elif music == list(range(1, 9)[::-1]):
    print('descending')

else:
    print('mixed')