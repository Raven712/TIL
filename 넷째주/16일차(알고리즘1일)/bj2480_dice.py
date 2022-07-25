a, b, c = map(int,input().split())
d = [a, b, c]
if a == b == c:
    print(10000 + a * 1000)  
if a == b != c or a == c != b:     # 이상황에서 if를 두개씩 쓰면 에러가 나온다. 왜지
    print(1000 + a * 100 )
if a != b == c:
    print(1000 + b * 100)
if a != b != c:
    if a > b > c or a > c > b:
        print(a * 100)
    elif b > a > c or b > c > a:                 # if가 이렇게 많이나오는게 맞나 싶다
        print(b * 100)
    elif c > a > b or c > b > a:
        print(c * 100)