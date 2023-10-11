# WEB 2일_CSS Layout

- Flexbox에 대해 자세히 알아보자

- 행과 열 형태로 아이템을 배치하는 1차원 레이아웃 모델
- 축
  - main axis(메인 축)
    - flex-direction: row
      - 
  - cross axis(교차 축)
- 구성요소
  - Flex Container(부모 요소)
    - flexbox 레이아웃을 형성하는 가장 기본적인 모델
    - flex item이 놓인 영역
    - display 속성을 flex 혹은 inline-flex로 지정
  - Flex item(자식 요소)
    - 컨테이너 속에 속한 컨텐츠(박스)
    - 부모에 flex를 지정하면 자식은 flex item들이 됨



**왜 쓰나?**

- 이전까진 normal flow를 벗어나려면 position 같은걸 써야했음
  - 그래서 수동값 부여없이 수직정렬이 힘들었고
  - 아이템의 너비와 높이, 간격을 동일하게 배치하기 힘들었음

## Flex의 속성

- 배치 설정
  - flex-direction
  - flex-wrap
- 공간 나누기
  - justify-content(main axis)
  - align-content (cross axis)
- 정렬
  - align-items (모든 아이템을 cross axis 기준으로)
  - align-self(개별아이템)