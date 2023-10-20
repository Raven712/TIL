# JS 1일_Event

### 개념

- 네트워크 활동이나 사용자와 상호작용같은 사건 발생을 알리기위한 객체
- 이벤트 발생
  - 클릭, 키보드 누름 등 사용자 행동으로 발생할 수도 있음
  - 특정 메서드를 호출(Element.click())해 프로그래밍적으로 만들기도 가능

### 역할

- "~하면 ~한다."
- 이벤트가 발생하면 함수를 등록한다.

### 

### handler - addEventLister()

- EventTarget.addEventListener(type, listener[ , options])
  - 지정 이벤트가 대상에 전달될 때 마다 호출할 함수 설정
  - type
    - 반응 할 이벤트 유형 (대소문자 구분 문자열)
  - listener
    - 지정된 타입의 이벤트가 발생했을때 알림을 받는 객체 (함수)



- 대상(EventTarget)에 이벤트가 발생하면(type), 할일(listener)을 등록하자
  - EventTarget.addEventListener(type, listener)
  - btn.addEventListener('click', function(){console.log('클릭')}) 이런식



### prevent

- 특정내용을 복사같은걸 못하게 해보자

```html
<h1>복사 ㄴㄴ</h1>

	<script>
        const h1 = document.querySelector('h1')
        h1.addEventListener('copy', function(event){
			event.preventDefault() // 기본동작자체를 막아버림
            console.log('복사 안돼')
        })
	</script>

// 지금은 이전이랑 다르게 이벤트자체가 발생않도록 하고싶은것
그래서 preventDefault() 라는 메서드가 쓰였다
```



