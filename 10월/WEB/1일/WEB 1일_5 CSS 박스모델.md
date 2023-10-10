# WEB 1일_5 CSS 박스모델

### CSS 원칙

- 첫번째
  - html의 모든 요소들은 박스(네모)임.
  - 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓임.
  - 인라인 (한줄 배치)으로, 블럭(네모네모)으로.. 쌓인다



- 박스모델
  - 박스 하나는 네 영역으로 이루어짐
  - margin
    - 테두리의 바깥 외부여백, 배경색 지정불가
    - css에서 margin의 크기를 조정하려면
      - .margin{margin: 10px} <<마진의 4영역 전부 조절
        - 10px 20px : 상하 10픽셀, 좌우 20픽셀
        - 10px 20px 30px : 상 10, 좌우 20, 하 30
        - 10px 20px 30px 40px : 상10 우 20 하 30 좌 40
  - border
    - 테두리
      - border-width: 2px;
      - border-style: solid / dashed..;
      - border-color: black;
  - padding
    - 테두리 안쪽의 내부여백. 요소에 적용된 배경색, 이미지는 여기까지 적용
      - 
  - content
    - 글, 이미지 등 요소의 실제 내용



- 박스 사이징
  - 기본적으로 모든 요소의 박스 사이징은 content 영역만 지정