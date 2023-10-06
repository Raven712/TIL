import time
start = time.time()

n = int(input())
record = {}
for i in range(1, n + 1):
    rec = list(input().split())
    record[rec[0]] = rec[1]

# name = []
# name_L = []
# for i in record:
#     if i[1] == 'leave':
#         name_L.append(i[0])         
#     if i[0] not in name_L:
#         name.append(i[0])
# name = sorted(name)
name = []
for i in record:
    if record[i] == 'enter':
        name.append(i)

name = sorted(name)[::-1]

for i in name:
    print(i)

print("time :", time.time() - start)