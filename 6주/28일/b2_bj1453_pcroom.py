N = int(input())

seat = list(map(int, input().split()))

seat_s = set()
count = 0
for i in range(N):
    if seat[i] not in seat_s:
        seat_s.add(seat[i])
    else:
        count += 1

print(count)