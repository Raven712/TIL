# JS 2일_ECMA Script(3) - 조건문, 반복문

- if, else if, else로 돌아감

```javascript
if (조건) {
    실행할 코드
} else if (조건2) {
    실행할 코드 2
} else {
    실행할 코드 3
}
```

- switch 문
  - 표현식의 결과값을 이용한 조건문

```javascript
switch(expression) {
    case 'first value' : {
        실행할 코드
        [break]
    }
    case 'second value' : {
        실행할 코드
        [break]
    }
    [default: {
     	실행 코드
     }]
}

// 표현식의 결과값과 case문의 오른쪽 값을 비교
break, default문은 선택적 사용

예를들면
const nation = 'Kor'
switch(nation) {
    case 'Kor': {
        console.log('안녕하세요')
    }
    case 'France': {
        console.log('Bonjour')
    }
    default: {
        console.log('Hello')
    }
}
이 스위치문은 Break를 만나지않아서 모두 출력됨
case마다 Break를 걸어주면 한개만 출력될것임
```



## 반복문

- for... in,  for.. of 같은게 있음
- ;으로 구분되는 세부분 구성
  - for (initialization, condition, expression) { 함수 }
    - initialization
      - 최초 반복문 진입시 1회만 실행되는것
    - condition
      - 매 반복시 평가되는 부분
    - expression
      - 매 반복 시행후 평가되는 부분

```javascript
for (let i = 0; i < 6; i++) {
    console.log(i) // 0,1,2,3,4,5
}
```

- for ... in

  - 객체의 속성(key)를 순회할떄 사용

  - 배열도 순회가능하지만 권장x

  - 실행 코드는 중괄호 안에 작성

  - ```javascript
    for (variable in object) {
        실행할 코드
    }
    const capitals = {
        kor: 'seoul'
        fran: 'paris'
        usa: 'washington'
    }
    for (let capital in capitals) {
        console.log(capital) // kor, fran, usa
    }
    // for of로 순회하면 오류가 난다
    ```

- for ... of

  - 반복가능 객체 순회할때

  - ```javascript
    for (variable of iterables) {
        실행코드
    }
    const fruits = ['딸', '바', '키']
    for (let fruit of fruits) {
        fruit = fruit + '!'
        console.log(fruit)
    }
    
    // for in으로 객체순회하면 인덱스 번호가 나옴
    ```

    