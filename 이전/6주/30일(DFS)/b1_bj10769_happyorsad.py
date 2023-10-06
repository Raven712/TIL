# :-) --> 웃음 :-( --> 안좋음
#이모티콘없으면 none 출력 , 이모티콘 갯수가 같으면 unsure, 갯수차이 날떄 happy 거나 sad
import sys
sys.stdin = open('h.txt', 'r')

sentence = input().split()

cnt_happy = 0
cnt_sad = 0

for i in sentence:
    for j in range(len(i)):
        if j + 2 <= len(i) - 1:
            if i[j] == ':' and i[j + 1] == '-' and i[j + 2] == '(':
                cnt_sad += 1
            elif i[j] == ':' and i[j + 1] == '-' and  i[j + 2] == ')':
                cnt_happy += 1

if cnt_sad == 0 and cnt_happy == 0:
    print('none')
elif cnt_sad == cnt_happy:
    print('unsure')
elif cnt_sad > cnt_happy:
    print('sad')
else:
    print('happy')