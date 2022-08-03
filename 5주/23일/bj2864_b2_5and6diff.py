# 5를 볼때 5로볼수도, 6으로볼수도. 6볼때도 6or5 이지

# 수 두개입력, 합중 최소 최대 둘다출력
# 문자열로된 숫자를 하나하나 for로 돌리면서 5,6이 있다면.. 5로 다 바꿔서 min에 적용, 6으로 다 바꿔서 max에 적용 ..  이렇게하는게맞을까?
# 이렇게하면 십, 백단위 구분하기가 힘들어보인다. 근데 replace를 쓰면?

A, B = input().split()
sum_min = 0
sum_max = 0

min_A = int(A.replace('6', '5'))
min_B = int(B.replace('6', '5'))
max_A = int(A.replace('5', '6'))
max_B = int(B.replace('5', '6'))

sum_min = min_A + min_B
sum_max = max_A + max_B

print(sum_min, sum_max)
