# 참여도 수치화 // 100이상이 합이면 ㅇㅇ 미만은 ㄴㄴ

Soongsil, Korea, Hanyang = map(int, input().split())
dic_ = {}
list_ = []
list_.append(Soongsil)
list_.append(Korea)
list_.append(Hanyang)
dic_[Soongsil] = 'Soongsil'
dic_[Korea] = 'Korea'
dic_[Hanyang] = 'Hanyang'

if Soongsil + Korea + Hanyang >= 100:
    print('OK')
else:
    print(dic_[min(list_)])