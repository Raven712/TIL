word = input()
count = 0
# dic_ = {
#     'c=' : 'c',
#     'c-' : 'c',
#     'dz=' : 'd',              기본적으로 알파벳은 모두 +1 
#     'd-' : 'd',           # -가 있는경우 pass, =가 있는경우 앞앞이 d 앞이 z인경우 -1 else pass
#     'lj' : 'l',               j인 경우 앞이 l이거나 n이면 -1
#     'nj' : 'n',
#     's=' : 's',
#     'z=' : 'z',
# }
for i in range(len(word)):
    if word[i] == '-':
        pass
    elif word[i] == '=':
        if i >= 2 and word[i - 2] == 'd' and word[i - 1] == 'z':
            count -= 1
            # if word[i - 2] == 'd' and word[i - 1] == 'z':
            #     count -= 1
        else:
            pass
    elif word[i] == 'j':
        if i >= 1 and word[i - 1] == 'l' or 'n':                        
            pass
        # if i >= 1:
        #     if word[i - 1] == 'l' or 'n':
        #         pass
        #     else:
        #         count += 1
        # else:
        #     count += 1
    else:
        count += 1

    # if word[i] == '=':
    #     pass
    # elif word[i] == '=' and word[i - 1] =='z':
    #     if 
    # else:
    #     if word[i] == 'j':
    #         if word[i - 1] == 'l' or 'n':
    #             pass
    #         else:
    #             count += 1
    #     else:
    #         count += 1
    
print(count)
