a = int(input())
num = 0
while a > 0:
    num = a%10
    a //=10
    print(num, end='')

    # 다른사람거 봄