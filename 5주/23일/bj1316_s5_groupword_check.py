#그룹단어 : ccb , abccdd 같은것. 근데 ccbc << 떨어져서 그룹단어 ㄴㄴ

#세트를 이용해서 단어가 나올떄 등록을 하고, 등록된 알파벳이 또 나오면..? ㄴㄴ 안될듯 (중복이 아니고 떨어진게 문제) - > 그렇다면 다음알파벳이 현재알파벳과 같을떄 등록 ?
#

N = int(input())
count = 0
for i in range(N):
    word = input()
    word_set = set()
    for i in range(len(word)):
        if word[i] not in word_set:
            word_set.add(word[i])
        else:
            if word[i] == word[i - 1]:
                pass
            else:
                break
        if i == len(word) - 1:
            count += 1
print(count)