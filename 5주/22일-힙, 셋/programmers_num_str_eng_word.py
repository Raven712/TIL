# def solution(s):
#     answer = 0
#     s = input()
#     num = {'0' : 1, '1' : 1, '2' : 1, '3' : 1, '4' : 1, '5 ': 1, '6' : 1, '7' : 1, '8': 1, '9' : 1}
#     # for i in range(len(s)):
#     #     while s[i] not in num:
#     eng = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}

#     word = []
#     for i in range(len(s)):
#         if s[i] in num:
#             print(s[i], end = '')
#         else:
#             while s[i] not in num: 
#                 word.append(s[i])                                                     망함
#                 i += 1
#             word2 = ''.join(word)
#             print(eng[word2], end = '')
#     return answer


# def solution(s):
#     answer = []
#     num = {'0' : 0, '1' : 1, '2' : 2, '3' : 3, '4' : 4, '5 ': 5, '6' : 6, '7' : 7, '8': 8, '9' : 9}
#     eng = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' : 3, 'four' : 4, 'five' : 5, 'six' : 6, 'seven' : 7, 'eight' : 8, 'nine' : 9}
#     word = []
#     for i in s:
#         if i in s:
#             answer.append(i)
#         else:
#             word.append(i)
#             word2 = ''.join(word)
#             if word2 in eng:
#                 answer.append(eng[word2])
#                 word2 = ''
#                 word = []
#     return ''.join(answer)

# print(solution('one4seveneight'))