# OOP (객체 지향 프로그래밍) #2



### 기본 문법

- 클래스 정의
  - class ~~~

- 인스턴스 생성
  - my_instance = myclass()
- 메서드 호출
  - my_instance.my_method()
- 속성
  - my_instance.my_attribute <<< 속성은 () 없음



**CamelCase(대문자로 단어구문) = 클래스, snake_case(언더바로 단어구분) = 변수와 함수에 적용**



```python
class Person:
    def talk(self)
```



- 객체 비교하기
  - ==
    - 동등한
    - 변수가 참조하는 객체가 내용이 같다면 true
  - is



- - a = [1,2,3] 
  - b= a
  - b[0] = 'hi
  - print(a)
  - print(b) 라면 ? --> a,b 둘다 ['hi', 2, 3] 이 됨!! a도 바뀐다..
    - 왜? 변수엔 주소값이 있는데, 이게 메모리에 저장됨. b = a할때는 주소값을 가져오는거라서..
    - 따로 하려면, a의 값을 복사해서 b로 옮겨야됨
      - 방법은 b = list(a) 혹은 b = a[::]로 슬라이싱 하면 값만 옮겨옴

```python
a = [[1,2], 2, 3]
b = list(a)
b[0][0] = 'hi'

print(a)
print(b) 하면 어떻게 될까
--> 둘다 [[hi, 2], 2, 3] 됨
--> 일차원상의 리스트는 나눴는데 2차원상의 주소를 못바꿈..(얕은복사)

어케 따로할까
b = copy.deepcopy(a) 로 '깊은복사'를 하면됨
깊은복사는 모든 주소를 따로 가짐
```



그래서 == 는 내용이 같냐의 여부를 따지고

is 는 주소까지 따지는것.. (참 거짓여부를 따질떄)





### 인스턴스

- 인스턴스 메서드
  - 인스턴스 변수를 사용하거나 인스턴스 변수에 값을 설정하는 메서드
  - 호출시, 첫째 인자로 인스턴스 자기자신(self)이 전달됨..
    - self? 
      - 인스턴스 자기자신
      - 매개변수 이름으로 self를 첫째 인자로 정의 (약속 ?)

- 생성자 메서드
  - 인스턴스 객체가 생성될때 자동으로 호출되는 메서드
  - 인스턴스 변수들의 초기값을 설정.. 
    - `__init__(self):` << 인스턴스가 생성될때 작업을 하는것..?? <-> 소멸자는 `__del__`

 

- self

  ``` python
  class Person:
      def __init__(self, name):
          #인스턴스의 이름을 name으로 해주세요 (self.name)
          self.name = name
          
  iu = Person('아이유') --> #'아이유'가 __init__(self, name):의 name에 들어가고, 그게 self.name = name의 뒷쪽 name에 들어감..
  print(iu.name) -> 아이유 
  ```

  
