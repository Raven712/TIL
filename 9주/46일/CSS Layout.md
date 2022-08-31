# CSS Layout

- CSS 원칙

  - normal flow
    - 모든 요소는 네모 (박스모델) , 좌측상단 배치
    - 디스플레이에 따라 크기-배치가 달라짐.

  - position으로 위치기준 변경
    - relative, absolute, fixed, sticky..

***

### CSS 레이아웃 종류

- display
- position
- float
- flexbox - 배치하기 좋음 ? 
- grid
- 기타.



### Float

- 어떤 요소를 감싸거나 , 좌 우측에 배치를 하기가 힘듬.
  - 신문의 기사 사진 큰거. 근데 바로 옆에 글들이 있는것들..
  - 일단은 있다는것만 알고 넘어가자. Flexbox를 배움.

### Display

- block, inline, inline-block 등.

### Flexbox

- CSS flexible box layout

- 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
  - 축이라는 개념이 있음.
  - 부모요소에 flex container를 지정하면 자식요소들이 알아서 아이템들이 된다.
  - 저 flex container 안에는 2개의 축이 생김.
    - 메인 축, 교차 축.
    - 축의 방향을 정할수있음 (flex-direction : row --> 메인축의 방향이 행방향.)



#### Flexbox의 구성요소

- 부모요소와 자식요소.
  - 부모요소 : flexbox 레이아웃을 형성하는 기본적인 모델.
    - flex item(자식요소) 가 놓인 영역.
    - display 속성을 flex 혹은 inline-flex로 지정. (이 속성을 부모에게 주는거임.)



- 그래서 플렉스박스를 왜쓰나
  - 기존엔 노멀플로우를 float나 position으로 벗어났는데, 하기어려웠던게 있음
    - 수직정렬, 아이템 너비-높이-간격을 동일하게 배치하기



#### flexbox 시작

- .flex-container {
  - display : flex;}  <-- 부모요소에 display: flex 혹은 inline-flex



#### Flex 속성

- 배치설정

  - flex-direction (배치 설정)

    - 메인 축 기준방향 설정
    - 역방향은 HTML 태그 선언순서와 시각적으로 다르다 ..?
    - row (좌 - > 우 배치) , row-reverse(우 -> 좌) / column(상 -> 하), column-reverse(하 -> 상). 
      - 예를들어 flex-direction이 row라면, 메인축이 좌 -> 우방향이고, 교차축은 column 방향. vice versa

  - flex-wrap

    - 아이템들이 컨테이너 밖으로 안나가게 해주는것.

  - justify-content(메인 축) (공간 나누기)

    - 메인축을 기준으로 공간배분하기.
    - flex-start(왼쪽에 모으기), flex-end(우측에 모으기), center(중앙에), space-between(1 2 3)
    - space-around( 1  2  3 ), space-evenly( 1 2 3 )

  - align-items(모든 아이템을 교차축 기준으로 정렬 ?)

    - justify-content랑 반대임. 교차축기준으로 정렬이니까
    - stretch(늘리기), flex-start / flex-end , center, baseline

  - align-self(개별 아이템들을 교차축 기준으로 정렬하는것.)

    

- 기타 속성

  - flex-grow : 남은 영역을 아이템에 분배
    - <디브 class="flex_item grow-1 order-3"1</디브>
    - <디브 class="flex-tiem grow-1">2</디브> 
      - 저렇게 하면, 1과 2가 같은 비율로 남은 영역을 가지는것. 



**활용**

```html
.container{
	display: flex;
	justify-content: center;			<!-- 중앙배치하기 -->
	align-items: center;
}

#layout_1 {
	display: flex;
	flex-direction: column;
	flex-wrap: wrap;					<!-- 카드배치 -->
	justify-content: space-around;
	align-content: space-around;
} 

#layout_2 {
	display: flex;
	flex-direction: row;
	flex-wrap: wrap;					<!-- 카드배치2.(가로) -->
	justify-content: space-around;
	align-content: space-around;
}

<!-- 그러나 이차원배치(카드배치)는 grid로 하는편이라고 함 -->
```



- 팁 : 개발자도구 쓸때 flex 쓰면 버튼이 있어서 코드쓸필요도없음.