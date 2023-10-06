import sys

N = int(sys.stdin.readline())
list_ = []
for i in range(N):
    state = sys.stdin.readline().rstrip().split()  
    if state[0] == 'push':
        list_.append(int(state[1]))
    elif state[0] == 'top':
        if list_ != []:
            print(list_[-1])
        else:
            print(-1)
    elif state[0] == 'size':
        print(len(list_))
    elif state[0] == 'empty':               # 런타임 에러나옴 << 내 실수
        if len(list_) == 0:
            print(1)
        else:
            print(0)
    elif state[0] == 'pop':
        if len(list_) == 0:
            print(-1)
        else:
            print(list_.pop())
            