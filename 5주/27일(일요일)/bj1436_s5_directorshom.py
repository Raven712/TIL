N = int(input())

#666 1666... 6660.. 6669 .. 7666 .. 10666 11666 16660..16669 ... 65666 66600 .. 66699 67666 .. 
# s = 0
# s1 = 0
# s2 = False
# for i in range(100000000): 
#     s_ = list(str(i))
#     for j in range(len(s_)):
#         if s_[j] == '6':
#             s1 += 1
#         else:
#             s1 = 0
#         if s1 == 3:
#             print(i)
#             s += 1
#             break
#             s2 = True
#     if s2 == True:
#         break
#     if s == 10000:
#         print(s)                      ==> 1만번쨰 N은 247만보다 작음
#         break
# n = 1
# while True:
#     if n == 10001:
#         break
#     if n < 10001:
s = 0
s1 = 0
s2 = False
for i in range(3000000):
    s_ = list(str(i))
    for j in range(len(s_)):
        if s_[j] == '6':
            s1 += 1
            if s1 == 3:
                s += 1
                s1 = 0
                break
        else:
            s1 = 0
        
    if s1 < 3:
        s1 = 0
    if s == N:
        print(i)
        break

### 답:
# i = 666
# cnt = 0
#이딴짓 할필요 없이 그냥 while True:
# if '666' in str(i):
    #cnt += 1
    #if cnt == n:
    #   print(i)
    #   break
# i += 1 이렇게 하면됨.. 666에서 숫자를 1씩 더해가면서 숫자전체에 666이 있는지없는지 확인하면 되는거였음