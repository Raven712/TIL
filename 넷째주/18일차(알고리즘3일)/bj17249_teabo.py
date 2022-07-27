word = input()
list_ = 0 # 리스트라고 하긴했는데 그냥 왼쪽얼굴 위치찾기용
for i in range(len(word)):
    if word[i] == '(':
        list_ = i

list2 = [0, 0] #골뱅이횟수 넣을곳

for i in range(0, list_):
    if word[i] == '@':
        list2[0] += 1

for i in range(list_ + 4, len(word)):
    if word[i] == '@':
        list2[1] += 1
        
print(list2[0], list2[1])