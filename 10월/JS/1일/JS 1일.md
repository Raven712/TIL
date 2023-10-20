# JS 1일

- 변수, 데이터타입, 조건, 반복, 함수, 특징을 알면 다른언어 배우기 쉽다

## 인트로

- 브라우저를 조작할 수 있는 유일한 언어가 JS
- 화면을 동적으로 만들기 위함

- jquery란걸 썼었는데 es6+ 이후 표준화가 되어 거의 이걸씀



- 바닐라 JS
  - 바닐라(아이스크림의 기본), 기본이라는 밈
  - jquery 이런거 쓰지말고 JS 쓰라는 그런의미인듯
- node.js
  - 프론트 하려면 필수적으로 배워야 하는내용 (지금은 안배움)
  - JS의 Runtime 환경을 제공
    - js를 특정환경에서 실행해서 쓸수있게 해주는거
    - 예전엔 브라우저에서밖에 안됐다고함



## DOM(Document Object Model)

**브라우저에서 할 수 있는 일**

- DOM 조작
  - 문서(HTML)조작
- BOM 조작
  - navigator, screen, location, frames, history..
- JavaScript Core (ECMAScript) - 프로그래밍 문법
  - 데이터 구조, Conditional Expression..



**DOM이란?**

- HTML, XML 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
- 문서를 구조화하고 구조화된 구성 요소를 하나의 객체 취급해 다루는 논리적 트리모델
  - html 파일이 head>title / body>h1... 이런식으로 간것도 트리모델. 
  - 그 최상위에 document가 있고,  아래에 html, 그 아래에 head... 이런식이라는 말
- 문서가 구조화 돼있으며 각 요소는 객체 취급
- 주요 객체
  - window: DOM을 표현하는 창 (가장 최상위 객체)
  - document: 페이지 컨텐츠의 Entry Point 역할, body태그 등 많은 다른 요소를 포함
  - navigator, location, history, screen



**DOM 해석**

- 파싱(parsing)
  - 구문 해석
  - 브라우저가 문자열을 해석해 DOM tree로 만드는 과정