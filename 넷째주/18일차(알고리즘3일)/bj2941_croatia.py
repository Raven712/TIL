word = input()
croa = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# length = 2
# word2 = list(map(''.join, zip(*[iter(word)]*length))) # <<< 구글링함.. 글자 두개씩나누기

# if len(word) % 2 != 0:
#     word2.append(word[-1])      # 글자수 홀수인 단어면 마지막거 추가

# for i in word2:
#     if i in croa:

######
# 다 필요없고 replace 함수 쓰면 끝
for i in croa:
    word = word.replace(i, '*')
print(len(word))