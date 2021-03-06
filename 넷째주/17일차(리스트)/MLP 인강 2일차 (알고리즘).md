# MLP 인강 2일차 (알고리즘)



## 선택 정렬

- 제일 작은 데이터부터 정렬시킴
  - 처리되지 않은데이터중 제일앞에 있는 데이터를 제일 작은데이터와 위치변경
    - 계속 반복하는것.. 
    - 탐색할때마다 탐색범위가 줄어듬. 



```python
array = [7, 5 ... 숫자많음]

for i in range(len(array)):
    min_index = i # 가장 작은원소의 인덱스 . 즉 i는 바꾸고자 하는 인덱스 위치(제일앞)
    for j in range(i + 1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] # 스왑 << 이게 히트
print(array)
```



- 일단 스왑은 기억하자
- 위의 방법은 빅오노테이션 O(N^2)임



## 삽입 정렬

- 처리안된 데이터를 하나씩 골라 적절한 위치에 삽입

- 첫째 데이터는 정렬되있다고 생각하고,  그 데이터보다 크다면 우측, 작다면 좌측으로 삽입

- 이렇게 계속 이미 들어간 데이터들과 비교해서 어디넣는게 맞는지 (왼쪽 오른쪽) 생각하며 반복

  

```python
array = [7, 5 ... 위와같음]

for i in range(1, len(array)):
    for j in range(i, 0, -1): #< 인덱스 i부터 1까지 1씩 감소하며 반복
        if array[j] < array[j -1]: # 한칸씩 왼쪽으로 가며 비교
            array[j], array[j -1] = array[j - 1], array[j] #스왑
        else: #자기보다 작은 데이터를 만나면 멈춤
            break
print(array) -> [0,1,2,...]
```

- 시간복잡도 O(N^2)

- 현재리스트가 정렬된상태라면 O(N)까지 줄어듬



## 퀵 정렬

- 기준데이터 설정, 그 기준보다 큰데이터와 작은데이터 위치를 변경
- 첫 데이터를 기준데이터(pivot) 으로 설정함. 

- 계속 양끝에서 (앞쪽은 0말고 1번부터) 두 데이터를 비교해 작은거랑 큰거랑 위치를 변경
  - 계속하면 중앙에서  교차되고, 이때 작은데이터와 피벗데이터 위치를 바꾸면,
  - 피벗왼쪽은 피벗보다 작은데이터, 우측은 큰데이터가 됨. 이게 '분할'
    - 그런데 이 과정을 자꾸 해주면 (왼쪽데이터끼리 이 정렬을 하고... 우측에도.)
      - 계속 반복하면 결국 정렬이 다 됨.

- 이상적인 경우 O(Nlog N )의 횟수 가능. 최악은 O(N^2)





## 시간복잡도

선택정렬 = O(N^2)

삽입 = O(N^2)

퀵 =O(N^2) or O(NlogN)