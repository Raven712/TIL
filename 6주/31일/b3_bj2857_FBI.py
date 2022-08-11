list_ = []
cnt = 0
for i in range(5):
    name = input()
#     list_.append(name)
    if 'FBI' in name:
        print(i + 1, end = ' ')
        cnt += 1
    
if cnt == 0:
    print('HE GOT AWAY!')

# for i in range(5):
