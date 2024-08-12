# CSS 정렬(flex-position..)

### flex

- display:flex;로 시작
  - 박스를 수직나열: flex-direction: column; --> 얘를 하면 justify-content와 align-item이 바뀜
  - 수평: flex-direction: row;
- justify-content: center;
  - 부모박스의 가로기준으로 가운데 정렬
- align-items: center;
  - 부모박스의 세로기준으로 가운데 정렬

- 정렬 옵션
  - space-between, around, evenly..



### position

- position: absolute, relative, fixed
  - absolute: 박스의 절대위치를 지정해주는 방식
  - relative: 부모박스 기준으로 상대위치
  - fixed: 화면기준 절대위치 (내비바같은것들)