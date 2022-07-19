a = int(input())
if a <= 30:
    print('좋음')
elif 30 < a <= 80:# <<d이렇게 할필요가없다
    print('보통')
elif 80 < a <= 150:
    print('나쁨')
else:
    print('매우나쁨')
