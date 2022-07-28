N = int(input())   
dic_card = {}
for i in range(N):
    card = int(input())
    if card not in dic_card:
        dic_card[card] = 1
    else:
        dic_card[card] += 1
item = []
item = dic_card.items()
item = sorted(item)

count = []

for i in item:
    count.append(i[1])

for i in item:
    if i[1] == max(count):
        print(i[0])
        break
