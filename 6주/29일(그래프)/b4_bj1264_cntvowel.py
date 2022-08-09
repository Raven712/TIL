vowel = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}  #세트
sentence = [0]
while sentence[0] != '#':
    sentence = input().split()
    cnt = 0
    for i in sentence:
        for j in i:      #문장을 리스트로 바꾸고, 단어(i) 를 하나하나 순회하면서 단어의 알파벳이 모음인지 확인해야하므로
            if j in vowel:
                cnt += 1
    if sentence[0] != '#':
        print(cnt)
    else:
        continue

