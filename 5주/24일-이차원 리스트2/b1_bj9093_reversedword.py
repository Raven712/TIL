T = int(input())

for i in range(T):
    sentence = input().split()
    for x in range(len(sentence)):
        sentence[x] = sentence[x][::-1]
    for x in sentence:
        print(x, end =' ')
    print()