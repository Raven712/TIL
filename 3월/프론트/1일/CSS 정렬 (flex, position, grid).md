# CSS 정렬 (flex, position, grid)

- flex를 이용해서 정리하자
  - **핵심: 여러태그를 하나로 묶어서 정렬하는것**



## flex

- display: flex;를 시작으로,
  - 나열 방향 : flex-direction: column(수직); // row(수평); 
  - **기본 direction이 row로 지정되어있음!**

- justify-content: center;
  - 부모박스의 가로를 기준으로 가운데 정렬
  - **기본 flex-start로 되어있음!**
- align-items: center;
  - 부모박스의 세로를 기준으로 가운데 정렬
  - **기본 flex-start로 되어있음!**
- 저 두개를 다 적용시키면 중앙에 정렬하는것.



**flex-direction이 바뀌면 justify-content와 align-items의 효과가 바뀌게됨!**



## position

- position: absolute
  - 박스의 절대위치
    - 위치속성을 찍어주면 거기 위치함
- position: relative
  - 부모 박스 기준으로 상대 위치
- position: fixed
  - 화면 기준으로 절대 위치 (스크롤 무시)

아무것도 하지않으면 position: static.

