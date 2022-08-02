# 괄호가 () [] 두개있고  짝이 각자 다 맞아야하며 )이 먼저나오는경우가 한번이라도 있으면 안된다.
# 문장의 끝은 . << 이거다.
# 입력 종료는 . 하나만 들어오면 종료다


sentence = ''
while sentence != ['.']:
    sentence = input().split()

    count_l = 0
    count_r = 0
    count_L = 0
    count_R = 0
    is_break = False
    for i in sentence:
        for j in i:
            if is_break = True:
                break
            if j == '(':
                count_l += 1
            elif j == ')':
                count_r += 1
                if count_r > count_l:
                    print('no')
                    is_break = True
            elif j == '[':
                count_L += 1
            elif j == ']':
                count_R += 1
                if count_R > count_L:
                    print('no')
                    is_break = True
        
    if count_l == count_r and count_L == count_R:
        print('yes')
    else:
        if is_break == True:
            continue
        else:
            print('no')
