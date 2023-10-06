## 생각한것
# 이렇게 마구잡이로 for if를 쓰는문제가 맞는건가????????????????


import sys                                                          
input = sys.stdin.readline
# 괄호밸런스 + 괄호사이의 문자밸런스 // 문장끝은 항상 .
# sentence = input().split()

# dic_small = {}          #소괄호
# dic_capital = {}            #대괄호
# for i in sentence:                                                      # i 는 (hi / hell) 이런식 . (hi) 일수도있음
#     if '(' in i:
#         if '(' not in dic_small:
#             dic_small['('] = 1
#         else:                                                             #단순히 괄호만 있는데 아니고 (hi hello) 이런식으로 적혀서, 한뭉치가 단순히 괄호만 있거나 문자만 있는게아님
#             dic_small['('] = dic_small['('] + 1
#     if ')' in i:                                             # elif 사용하면 안될듯 ?? (hi) 는 하나의 i에 괄호가 둘다있으니까 둘다있는지 확인해야함.
#         if '(' not in dic_small:                            # 그렇게생각하니까 단순히 '(' << 이게 하나의 문자열뭉치에 포함됐는지를 볼게아님... 이중for문 써야할듯
#             print('no')
#             break
#         else:
#             if i not in dic_small:
#                 dic_small[')'] = 1
#             else:
#                 dic_small[')'] = dic_small[')'] + 1
#                 if dic_small[')'] > dic_small['(']:
#                     print('no')
#                     break
# print(dic_small)              


#괄호밸런스 맞추기. 문자끝은 항상 . 
#우측괄호가 좌측괄호보다 숫자가 많아지는순간 끝

sentence = input().split()

dic_small = {}        
dic_capital = {}
is_break = True
for i in sentence:          # i는 하나의 문자뭉치, j는 그걸 한글자한글자 보는것
    for j in i:

        if j == '(':
            if j not in dic_small:
                dic_small['('] = 1
            else:
                dic_small['('] += 1

        elif j == ')':
            if j not in dic_small:
                dic_small[')'] = 1
            else:
                dic_small[')'] += 1
            if dic_small[')'] > dic_small['(']:
                print('no')
                is_break = False    # 2중 for문을 탈출하는방법
                break

        elif j == '[':
            if j not in dic_capital:
                dic_capital['['] = 1
            else:
                dic_capital['['] += 1

        elif j == ']':
            if j not in dic_capital:
                dic_capital[']'] = 1
            else:
                dic_capital[']'] += 1
            if dic_capital[']'] > dic_capital['[']:
                print('no')
                is_break = False
                break

    if is_break:
        break