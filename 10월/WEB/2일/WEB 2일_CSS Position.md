# WEB 2일_CSS Position

- 문서 상에서 요소의 위치를 지정
- static : 모든 태그의 기본값
  - 일반적 요소의 배치순서에 따름 (좌상단)
  - 부모 요소 내에서 배치될때는 부모 요소의 위치를 기준으로 배치됨
- 아래는 좌표 프로퍼티(top, bottom, left, right)를 이용해 이동가능
  - 1.relative
  - 2.absolute
  - 3.fixed
  - 4.sticky

1. relative

   - 상대위치
   - 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지)

2. absolute 

   - 절대위치

   - 요소를 일반 문서흐름에서 제거 후 레이아웃에 공간을 차지안함

     - normal flow 벗어남

     - ```css
       .relative{
           position: relative;
               top: 50px;
               left: 50px;
       }
       # 이러면, 자기의 원래 위치 대비 top으로부터 50픽셀, left로 부터 50픽셀 이동하겠다는 말 - 즉 아래로 50, 우로 50px 이동시키는것
       
       .absolute {
           position: absolute;
           top: 50px;
           left: 50px;
       }
       # 얘는, 부모/조상 요소를 기준으로 위치.
       normal flow에서 벗어난다는 의미?
       해당요소가 화면에서 없어진다는 판정을 가짐
       즉 absolute 지정한 친구가 원래 좌상단에 있고 하단에 다른 요소가 있었으면
       하단에 있던친구가 좌상단으로 와버림 (앱솔루트는 화면에 없게 되는거니까)
       
       그리고 absolute는 부모요소가 static이 아닌친구를 만날떄까지 기준점을 찾으러가므로
       absolute 적용요소의 바로 상위요소를 기준으로 absolute를 주려면,
       바로상위요소가 static이 아닌 (relative 등)이어야함!!
       ```

     - 즉 absolute는 특정 영역 위에 존재할때 자주 사용함!

     

   - 3. sticky

     - 화면에 고정시켜서 딱 붙일때. 보통 화면 맨위에 있는 요소같은거에 씀

   - 4. fixed

   - - 그냥 화면에 고정시킬때 자주씀
     - 브라우저 기준 우측하단에 위치함

