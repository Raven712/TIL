# CSS

- 특성(프로퍼티)
  - color, background-color, font-size..
- 사용법
  1. html에 style 속성 넣어서 바로 쓰기
     - <a style="background-color 어쩌구.."
  2. 스타일 태그에 입력
     - head에 클래스를 만들어서 입력하기
     - .list { ~~어쩌구} 해놓으면 class=list에 모두 적용됨
  3.  파일만들어서 쓰고 불러오기
     - link href=css파일 어쭈구..

- 선택자
  - 전체 선택자 *
  - 태그 선택자 (div {~~})
  - 클래스 선택자 (.list 처럼)
  - 아이디 선택자( #list)

### 박스모델

- html태그는 모두 박스모델로 이뤄짐
  - margin: 박스의 바깥여백
  - border: 박스의 기준이 되는 바깥 테두리
  - padding: 박스의 안쪽 여백
  - contents: 박스의 내용

- border-box와 content-box
  - 보더박스를 움직이면 박스크기 유지, 컨텐트박스 사이즈를 움직이면 컨텐트는 크기고정, 박스가 커짐
    - 보통 보더박스로 설정을 해서 박스크기를 유지시켜줘야한다