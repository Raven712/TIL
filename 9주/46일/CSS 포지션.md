# CSS 포지션

**참고 : [CSS의 position 속성으로 HTML 요소 배치하기 | Engineering Blog by Dale Seo](https://www.daleseo.com/css-position/)**



- 문서상에서 요소의 위치를 지정하는것.
- static : 모든 태그의 기본값 ( 기준위치 )
  - 일반적인 요소의 배치 순서에 따름 (좌측 상단)
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치됨
- 아래는 좌표 프로퍼티 ( top, bottom , left, right ) 사용해서 이동가능
  - relative
  - absolute
  - fixed
  - sticky



- relative : 상대위치
  - 자기자신의 static 위치를 기준으로 이동 (normal flow 유지)
    - 노멀 플로우? : 내가 요소의 레이아웃을 변경안했을 때, 웹페이지 요소가 자기 자신을 스스로 배치하는 방법- -- > 그 중에서, 노멀 플로우는 웹페이지의 순정.
    - 즉 아무런 CSS를 적용하지 않은 상태.
    - HTML의 요소는 인라인요소와 블록레벨 요소로 나뉨.
      - 블록 레벨요소 : 부모요소의 전체공간을 차지하며 블록을 만듬. (한줄 통째로 차지)
      - 인라인 요소 : 요소를 구성하는 태그에 할당된 공간만 차지함 . (글이 있는곳만 차지하는 것...)
        - 인라인 요소는 크기제어가 가능함.
        - display : block; 과 display : inline-block; 같은걸로. 
          - display는 속성임. (요소를 어떻게 표시할지를 선택하는 속성.)
            - 요소는 태그와 컨텐츠들을 말하고, 속성은 display, href등등..
  - 노멀 플로우 등이 궁금하면 [[CSS\] 보통 흐름 (normal flow) (velog.io)](https://velog.io/@dongho18/CSS-보통-흐름-normal-flow) 참조 ! 
  - 그냥 쉽게 position : relative; top: 20px; left: 50px; << 이렇게 설정하면, 위에서 20픽셀 좌측에서 50픽셀 떨어진곳에 배치가 되는거임. (원래 위치로 부터)



- absolute : 절대위치

  - 배치기준을 상위요소에서 찾음. 
    - 상위 트리로 올라가면서 position 속성이 static이 아닌 첫째 상위요소가 배치기준이 됨.
    - static이 아닌 요소가 없다면, body가 요소배치기준이 됨.
    - 그러나 보통 특정요소의 display 속성을 absolute로 하면, 부모요소의 display 속성을 relative로 지정하는게 관례라고함.

  - position : absolute를 하면, HTML 문서에서 독립돼서 앞뒤에 나온 요소와 상호작용을 하지않게됨.



- fixed : 고정위치

  - 화면을 위아래로 스크롤해도 브라우저 화면의 특정부분에 고정되는 UI를 만들때 사용함.
  - fixed의 속성값 배치기준이 부모요소같은것이 아닌 뷰포트(viewport) - 즉 브라우저 전체화면이 기준이라서 그럼.
    - 즉 fixed의 top, left, bottom, right는 브라우저 상단 좌측 하단 우측을 기준으로 얼마나 떨어진지를 나타냄.

  - position : fixed도 absolute처럼 HTML 문서상에서 독립되어 앞뒤에 나온 요소와 상호작용을 하지않게됨.

  

  

- sticky 
  - 브라우저 화면을 스크롤링 할때 효과가 있음. 
  - <디브> 요소의 부모인 <메인> 을 overflow : auto로 조정해주고, 디브의 포지션을 sticky로 하고 top : 0을 하면, 그 요소가 화면상단에 딱 붙어있게됨.
    - 오버플로우 : 오토 ? : 내용물이 화면에 다 안담길때, 자동으로 스크롤링기능을 만들어주는것.