point_sum = 0
sum_ = 0

dic_ = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0
}
for i in range(20):
    subject, point, grade = input().split()
    point = float(point)
    if grade == 'P':
        pass
    else:
        sum_ += (dic_[grade] * point)
        point_sum += point
average = sum_ / point_sum
print(round(average,6))