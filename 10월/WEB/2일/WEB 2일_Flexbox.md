# WEB 2일_Flexbox

- flex-direction
  - 메인축 기준 방향설정
  - 역방향 경우 HTML 태그 선언 순서와 시각적으로 다름
    - row (메인축 방향이 ->)
    - row-reverse(<- )
    - column(메인축이 아래로)
    - column-reverse(메인축 방향이 아래에서 위로)



- flex-wrap

  - 아이템이 컨테이너를 벗어나는 경우 해당영역 내에 배치되도록 설정
  - 즉 컨테이너 영역을 안벗어나게함
    - wrap
    - nowrap

- flex-direction & flex-wrap

  - flex-flow: 두개를 합한 요약어
    - flex-fow: row wrap; (direction은 row, wrap은 wrap)

  

- justify-content

  - 메인 축을 기준으로 공간 배분
  - flex-start (메인축 기준 처음부터)
  - flex-end(중간부터, 끝까지 도달하도록)
  - center(중앙)
  - space-between(처음, 중간, 끝을 채우는식)
  - space-around(아이템마다의 간격이 다 동일)
  - space-evenly(아이템마다 간격이 동일, 조금 다름)



- align-items
  - 크로스 축을 기준으로 정렬
  - stretch: 늘리기..
  - flex-start
  - flex-end
  - center
  - baseline



- flex-grow: 남은 영역을 아이템에 분배
  - grow-1 / grow-1이면 두 아이템이 1:1비율로 영역을 가짐
- order: 배치 순서
  - order-2 / order-1 .. 
  - order:3 이런것도 되는듯?
  - order: -1;
    - 음수는 기존 아이템보다 맨 앞에 배치하는것