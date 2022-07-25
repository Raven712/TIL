N = int(input())
sample = list(map(int, input().split()))
min = sample[0]
max = sample[0]
for i in sample:
    if i >= max:
        max = i
    if i < min:
        min = i
print(min, max)

