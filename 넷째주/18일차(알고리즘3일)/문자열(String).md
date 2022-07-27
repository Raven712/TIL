## 리스트, 리스트 컴프리헨션

리스트 컴프리헨션좀 쓰자

numbers = []

for i in range(5):

number.append(i) 이걸 numbers = [i for i in range(5)] 하면 끝낼수있다.... 

[i for i in range(10) if i % 2 == 0] 이런것도 된다





# 문자열(String)

- 문자열은 immutable, iterable 임. (변경불가, 순서는 있음)



### 문자열 슬라이싱

- 슬라이싱은 a[2:-4] 처럼 양수~ 음수구간을 슬라이싱하는것도 된다



### 메서드

- .split() -> 문자를 특정기준으로 나눠 리스트로 반환. 안넣으면 공백기준

  - 스플릿의 복잡도.. ?

    

- .strip() -> 문자 양쪽끝을 지운 새로운 문자열 반환. 안넣으면 공백기준 

  - word = 'hello worlddd' -> word.stirp(d) ='hello worl' ---> 원본은 안변한다

    

- .find(찾는 문자)

  - 특정문자가 처음으로 나타나는 **위치(인덱스)** 반환임 ..

  - 찾는문자가 없으면 -1 반환

    

- .index(찾는 문자)

  - 마찬가지지만, 찾는문자가 없으면 오류발생



- .replace(기존문자, 새로운 문자)
  - 문자열의 기존문자를 새로운 문자로 바꿔서 새로운 문자열 반환 <<<<< 
  - word.replace('happy', 'angry') 이런식



- .join()
  - ()안의 내용 원소 사이에 특정문자를 삽입한 새로운 문자열 반환
  - word = 'happy'
  - print(' '.join(word)) -> 'h a p p y'



### 아스키 코드

- 

