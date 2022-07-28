word = input()

# for i in range(len(word)):
#     if word[i] in 'CAMBRIDGE':
#         word[i] = word[i].replace(word[i], '')          # 그냥 단어의 요소하나를 바꾸려고하거나 replace 하려고하면 스트링은 immutable해서 타입에러가 나옴
# print(word)

list_= list(word)
# for i in word:
#     list_.append(i) << 이거 제발 하지말고 list 함수 쓰자

for i in range(len(word)):
    if list_[i] in 'CAMBRIDGE':
        list_[i] = ''

print(''.join(list_)) # << join도 써보자 유용한것같다
