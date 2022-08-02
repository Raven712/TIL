# 수첩1 : 진짜본거
# 수첩2 : 봤다고 말한거
# 수첩2에 있는게 수첩1에 있으면 1출력, 없으면 0 출력 (각각의 수에 대하여.)

T = int(input())
for i in range(T):
    N = int(input()) # 수첩1의 정수개수

    diary1 = set(map(int, input().split())) # len(diary1) = N

    M = int(input()) #수첩2의 정수개수

    diary2 = list(map(int, input().split())) #len(diary2) = M


    # 순서가 상관없으니 << ㄴㄴ 상관있음
    # 딕셔너리나 세트를 쓰는게 맞겠다. << 그런데 세트는 자동정렬이 있어서 쓰면안되겠다. <<<< ㄴㄴ 세트는 순서가 매번 바뀐다 순서상관있음 <<<< 이걸 막으려면 frozenset를 쓰면된다 !!! 근데 자동정렬되는듯

    # 리스트에 중복이 있으면 지워야한다. 입력된 순서대로 비교해야한다.
    diary_checked = {}

    for i in diary2:
        # if i in diary_checked:
        #     continue
        if i in diary1:
            # diary_checked[i] = 1
            print(1)
        else:
            print(0)