from collections import deque
N = int(input())
card = list(range(1, N + 1))


card2 = deque(card)
while len(card2) != 1:
    print(card2[0], end = ' ')
    card2.popleft()
    card2.append(card2[0])
    card2.popleft()
left = list(card2) 
print(left[0])     