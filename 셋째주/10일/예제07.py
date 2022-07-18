number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total / count)

# count의 줄맞춤이 안돼있고 // 연산자는 몫을 구하는거라 / 로 바꿈