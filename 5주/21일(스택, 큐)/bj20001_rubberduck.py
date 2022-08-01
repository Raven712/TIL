speak = input()

count = 0
while speak != '고무오리 디버깅 끝':
    speak = input()
    if speak == '문제':
        count += 1
    elif speak == '고무오리' and count == 0:
        count += 2
    elif speak == '고무오리' and count != 0:
        count -= 1

if count == 0:
    print('고무오리야 사랑해')
else:
    print('힝구')