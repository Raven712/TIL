N = int(input())
a = range(1, N + 1)
b = list(a)
clap = 0
for i in b:
    if str(i).count('3') == 0 and str(i).count('6') == 0 and str(i).count('9') == 0:
        print(i, end = ' ')
    else:
        clap = str(i).count('3') + str(i).count('6') + str(i).count('9')
        print('-' * clap, end = ' ')  


### str.count(self, x, __start, __end) 메써드의 존재를 몰라서 어마어마한 삽질을 오래동안 한 문제.. count 아니까 금방 풀었음..