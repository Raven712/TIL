# JS 2일_ECMA Script

**코딩 스타일가이드**

- 대충 코드 가독성-유지보수 할때 규칙



### 변수와 식별자

- 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함
  - 문자, $, _로 시작
  - 대소문자 구분, 클래스 외에는 모두 소문자 시작
  - 예약어 사용 불가(for, if, function)
- 선언, 할당, 초기화
  - **let은 재할당이 가능, const는 재할당 불가능**
  - **let, const 모두 재선언은 불가능 (let foo = 10해놓고 let foo 20 이런거 안됨)**
  - 선언 (Declaration)
    - 변수를 생성하는 행위, 시점
    - let, const 같은거
    - let foo
    - console.log(foo) --> undefined
  - 할당 (Assignment)
    - 선언된 변수에 값을 저장하는 행위, 시점
    - foo = 11
    - console.log(foo) == 11
  - 초기화 (Initialization)
    - 선언된 변수에 처음으로 값을 저장하는 행위, 시점



- 블록 스코프

  - if, for 함수등의 중괄호 내부를 가리킴

  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

  - ```javascript
    let x = 1
    if (x === 1) { // 여기를 블록스코프라 함
        let x = 2
        console.log(x) // 2
    } // 여기까지
    
    console.log(x) // 1
    ```

- var

  - 재선언, 재할당가능, ES6 이전 변수 선언시 사용

  - 함수 스코프

    - function foo() { ~~~ } 여기 안만 적용

  - 호이스팅

    - 변수를 선언 이전에 참조할 수 있는 현상

    - JS 는 모든 선언을 호이스팅함

    - ```javascript
      console.log(a)
      var a = 5
      
      이렇게하는데 5가 나옴 (파이썬이었으면 잘못된코드라 a is undefined..나옴)
      
      하지만 console.log(a)
      let a = 5 이러면 a is undefined 나옴
      그렇다고 let, const가 호이스팅이 안되는건 아님
      ```

      

