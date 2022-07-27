word = input()
count = {}
# num = []
for i in word:
    if 122 >= ord(i) >= 97:
        i = chr(ord(i) - 32)        # 대소문자 아스키코드 번호 차이가 32
    # num.append(i)
    if i not in count:
        count[i] = 0
    count[i] = count[i] + 1    
# max_count = max(count, key = count.get)            ## 이걸로 끝내려고했는데 키의 값이 동일하면 알파벳순서 빠른거 하나만 출력됨
# num = list(num.items())
num = list(count.values())
M = max(num)
M_count = 0
for i in num:
    if i == M:
        M_count += 1
if M_count >= 2:
    print('?')
else:
    print(max(count, key = count.get))


# print(max_count)