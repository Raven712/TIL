# 단어 a,b가 주어졌을떄 a에 속하는 알파벳순서를 바꿔서 b가 되면 a와 b가 애너그램이다. 애너그램 여부를 판단해라.
# a 알파벳 하나하나를 딕셔너리에 등록해서 갯수만큼 값을 등록하고, b를 순회하면서 딕셔너리에 b의 알파벳이 있으면 값을 줄이고 + 값이 0 이하가 되면 break 걸고.. 이런식으로 했음
# 최종적으로는 애너그램인 단어쌍은 dic_a의 모든 값들이 0이 되는걸 이용함
import sys
sys.stdin = open('ana.txt', 'r')

n = int(input())

for i in range(n):
    a, b = input().split() #소문자로만 입력된다.
    dic_a = {}
    if len(a) != len(b):                        # 길이가 다르면 애너그램이 될수없으므로 바로 끝냄
        print(f'{a} & {b} are NOT anagrams.')

    else:
        for j in range(len(a)):
            if a[j] not in dic_a:
                dic_a[a[j]] = 1
            else:
                dic_a[a[j]] += 1
        
        for j in range(len(b)):
            if b[j] not in dic_a:
                print(f'{a} & {b} are NOT anagrams.')
                break
            else:
                dic_a[b[j]] -= 1
                if dic_a[b[j]] < 0:
                    print(f'{a} & {b} are NOT anagrams.')
                    break
    
        if sum(list(dic_a.values())) == 0:
            print(f'{a} & {b} are anagrams.')

    