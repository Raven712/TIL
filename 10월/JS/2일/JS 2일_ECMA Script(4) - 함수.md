# JS 2일_ECMA Script(4) - 함수

## 함수

- 함수는 일급 객체에 해당
  - 변수 할당가능
  - 함수의 매개변수로 전달 가능
  - 반환 값으로 사용가능



- 함수 선언식, 표현식 두가지 방법으로 함수를 정의함



### 함수 정의

- 이름과 함께 정의하는 방식 // 함수 표현식 권장됨 (선언식은 호이스팅이 발생함)

- ```javascript
  function name(args) {
      실행코드
  }
  function add(num1, num2) {
      return num1 + num2
  }
  
  함수 표현식
  - 함수를 표현식 내에서 정의하는것
  - 이름 생략, 익명함수 정의가능
  - 표현식으로 사용하길 권장한다더라
  - 표현을 var로 하면 변수가 선언전 undefined로 초기화되어 다른 에러가 발생함
  
  const add = function (num1, num2) {
      return num1 + num2
  }
  // 함수를 변수에 저장하는 느낌
  
  // 파이썬과 차이 : 매개변수와 인자 개수 불일치를 허용함
  const Args = function (arg1, arg2, arg3) {
      return [arg1, arg2, arg3]
  }
  
  Args(1) // [1, undefined, undefined] 로 나와줌
  Args(1, 2) // [1, 2, undefined]
  ```

- Rest parameter

  - ...을 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받음

    ```javascript
    const rest = function (arg1, arg2, ...restArgs) {
        return [arg1, arg2, restArgs]
    }
    rest(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
    ```

    

- Spread operator

  - ... 을 사용하면 배열 인자를 전개해 전달가능

  - ```javascript
    const add = function (arg1, arg2, arg3) {
        return arg1 + arg2 + arg3
    }
    const num = [1, 2, 3]
    add(...num) // 6
    ```

    

### Arrow Function

- ```javascript
  const arrow1 = function (name) {
      return 'hello, ${name}'
  }
  
  // 1. function 키워드 삭제
  const arrow2 = (name) => {return 'hello ${name}'}
  
  // 2. 매개변수가 1개일때 () 생략가능
  const arrow3 = name => {return 'hello, ${name}'}
  
  // 3. 함수 바디가 return을 포함한 표현식 1개일때 {} & return 삭제가능
  const arrow4 = name => 'hello ${name}'
  ```

- 