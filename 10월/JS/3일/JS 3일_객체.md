# JS 3일_객체

- JS의 객체는 키: 값(value)의 쌍으로 표현
- 속성(property)의 집합임
- key는 문자열만 가능
  - value는 모든 타입 (함수포함) 가능
- 객체 요소 접근은 점, 대괄호로 가능



```javascript
const me = {
    name : 'kim',
    phone : '01012345678',
    'samsung' : {
        galaxy : 'gal 10s+',
        buds : 'gal buds pro',
    },
}

console.log(me.name)
console.log(me['samsung'].galaxy)
이런게 된다.

메서드 (객체의 속성이 참조하는 함수, 아래에선 function() 전체)
내부에서 this라는걸 쓸수도 있는데
ex)

const me = {
    firstName : 'Kimyung',
    lastName : 'Kim',
    getFullName : function() {
        return this.firstName + this.lastName
    }
}
this는 여기서 객체를 의미함 // 애로우 펑션은 쓰면 안된다
// me.getFullName()

```

