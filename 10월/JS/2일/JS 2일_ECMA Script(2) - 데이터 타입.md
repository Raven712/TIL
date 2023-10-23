# JS 2일_ECMA Script(2) - 데이터 타입

## 데이터 타입

- JS의 모든 값은 특정한 데이터 타입을 가짐

  - 원시타입, 참조타입으로 분류(Primitive / Reference)

  - Primitive

    - 객체가 아닌 기본타입

    - 변수에 해당 타입의 값이 담김

    - Num, String, Boolean, undefined, null, Symbol

      ```javascript
      let message = '안녕하세요'
      let greeting = message
      message = 'Hello'
      console.log(greeting)
      --> Hello가 아니고 안녕하세요가 출력됨
      ```

      

  - Reference

    - 객체타입의 자료형

    - 변수에 해당 객채의 참조값이 담김

    - Objects-Array, Function...

      ```javascript
      let message = ['안녕하세요']
      let greeting = message
      message[0] = 'Hello'
      console.log(greeting)
      --> ['Hello'] 출력
      ```

- 문자열 타입의 템플릿 리터럴(Template Literal) - f스트링 친구

  - ES6부터 지원

  - 따옴표 대신 backtick(``)으로 표현

  - ${ expreesion } 형태로 표현식 삽입가능

    ```javascript
    const firstName = 'Kimyung'
    const lastName = 'Kim'
    cosnt fullName = `${firstName} ${lastName}` 
    console.log(fullName) // Kimyung Kim
    ```

### 연산자

- ++, -- 라는게 있음
  - 그냥 1을 올리고, 1을 내리는거.
- 일치 비교 연산자 (===)
  - == 대신 === 쓴다고 생각하면 된다
  - const a = 1
  - const b = true
  - console.log(a === b) ----> True

- 논리 연산자
  - and : &&
  - or : || (엔터위에거)
  - not : !
- 삼항 연산자
  - 가장 왼쪽 조건식이 참이면 콜론 앞의 값을 사용하고, 아니면 뒤의 값 사용
  - console.log(true ? 1 : 2) /-->1
  - console.log(false ? 1 : 2) --> 2