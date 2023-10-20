# JS 1일_DOM(2)

**BOM이란?**

- 브라우저 창, 프레임 제어하는 수단
  - window.print() 이런식



**JS Core**

- 프로그래밍 언어
- 조건문반복문 이런거 하는거..?



## DOM 조작

- ```html
  <body>
      <!-- script 영역이 JS 코드를 작성하는 영역 -->
      <script>
          console.log('hello, js')
          alert('js 학습 시작')
      </script>
      
  </body>
  ```

- console.log('~~')

  - ?

- const n = document.createElement('요소')

  - ('요소') 를 만들고, n에 할당함

- n.innerText = '~~'

  - 그 요소 안에 '~~' 라는 텍스트를 넣어줌

- const body = document.querySelector('body')

  - body 태그를 선택자로 가져온다

- body.appendChild(n)

  - body 태그에 n을 자식 요소로 추가

- 이러면 html을 손대지않고도 무언가 작동시킬수있음



### Const

- JS 변수 선언 키워드, 변경이 불가능함
- let은 변경이 가능함 (재할당 가능)
- Var는 옛날에 쓰던거(ES6 이전?)

### Select

- document.querySelector('#title')
  - id가 title인것을 선택한다는 뜻
- document.querySelector('h2')
  - h2태그를 선택한다 (가장 앞에있는 h2)

- document.querySelectorAll('h2')
  - h2태그를 모두 선택한다
- document.getElement(s)ById(''), Classname('')...
  - 복수가 될수있냐없냐에 따라 s가 붙고안붙고

### Create

- const a = document.createElement('a')

  - a 태그 생성

- a.innerText = '어쩌구저쩌구'

  - 내용을 어쩌구저쩌구로 넣음

- 이걸 body에 넣어보자

  - const body = document.querySelector('body')

  - body.appendChild(a)

- innerhtml은 보안떄문에 안쓴다



### Delete

- body.removeChild(a)
  - body의 a태그를 없앰
- title.remove()
  - title 태그 자체를 없앰



## 속성 붙이기

```html
const a = document.createElement('a')
로 a를 선언하고
a.innerText = '네이버'
const body = document.querySelector('body')
로 가져와서
body.appendChild(a) 
로 a를 자식요소로 넣고

a를 a태그로 만들어보자
a.setAttribute('href', 'https://www.naver.com')
console.log(a.getattribute('href'))
로 확인하면 나옴
```

