# n = int(input())
# sum = 0
# for i in str(n):
#     sum += int(i)
sum = 0
list_ = []   # 셀프넘버가 아닌걸 집어넣을것
for i in range(1, 10001):   
    for j in str(i):        #10000 이하의 모든 i의 자릿수 하나하나를 더한걸 sum에다 넣고, 모든 i에 대해 i+sum 을 했을때 나타나는 수를 리스트에 넣음. 
        sum += int(j)                           ## --> 즉 생성자를 가지는 수를 리스트에 넣었음
    list_.append(i + sum)
    sum = 0

for i in range(1, 10001):
    if i not in sorted(list_):              # 모든 10000이하 자연수 i들이 생성자를 가지는 리스트에 속해있지 않다면 (생성자가 없다면), 프린트.
        print(i)