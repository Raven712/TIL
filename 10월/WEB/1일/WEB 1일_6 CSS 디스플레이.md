# WEB 1일_6 CSS 디스플레이

- **CSS원칙 2**
  - 모든 요소는 박스모델, 좌측상단 배치
  - display에 따라 크기와 배치가 달라진다.



### 인라인요소와 블럭요소

- display: block
  - **줄 바꿈이 일어나는 요소** (마진떄문에)
  - 화면 크기 전체의 가로폭을 차지함
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
- display: inline
  - 줄 바꿈이 일어나지 않는 행의 일부 요소
  - **content 너비만큼 가로폭 차지**
  - width, height, margin-top... 지정 불가
  - 상하 여백은 line-height로 지정



- 대표적인 블록레벨 요소
  - div / ul, ol, li/ p /hr/ form
- 대표적 인라인 요소
  - span / a / img /input / b, em...



- display: inline-block
  - block과 인라인 레벨 요소 특징을 모두 가짐
  - 인라인처럼 한줄 표시가능, 블럭처럼 width, height, margin 지정 가능

- display: none
  - 해당 요소를 화면에 표시x, 공간도 잡아먹지않음
  - visibility: hidden은 요소가 공간은 차지하지만 화면에 표시안하게 하는것