# OOTP 2일차

클래스의 속성을 알고싶으면?

```python
class Person:
    species = '사람'
    
Person.species #하면 됨. () 없이
```



- 인스턴스와 클래스간의 이름공간
  - 클래스 정의시 클래스와 해당이름공간 생성
  - 인스턴스 만들면 인스턴스 객체와 이름공간생성
  - 인스턴스에서 특정속성에 접근하면, 인스턴스-클래스 순으로 탐색
    - 빌트인 함수 print에 글로벌영역에서 print = 2 할당시키면 빌트인함수가 안되는것과 같음



- 클래스 메서드

  - @classmethod로 정의  // @ : 데코레이터(함수꾸미는것)

  - ```python
    class Person:
        @classmethod
        def class_method(cls, ~~~)
       
    ```



- 스태틱 메서드
  - 인스턴스 변수, 클래스 변수를 건드리지 않는 메소드