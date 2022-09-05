#  Flexbox 2

- 수평, 수직 정렬

```html
div {
	display: flex;
	align-items: center; <!-- 아이템들이 flex로 인해 flex-container내부에 꽉차져있는걸 수평정렬--> 
	justify-content: space-around; <!-- 아이템들을 수직정렬하면서 좌우 간격도 맞춤 -->
}
```

- align-items
  - flex item이 교차축 어디에 놓일지 제어함.  (flex의 기본 메인축이 row이므로 column 기준이 되는것)
  - align-items: stretch (교차축으로 쭈욱 늘리기.)
  - align-items: center; (교차축 중앙에 배치시키기. 즉 교차축 (y축)의 중간, xy 좌표공간에서 (n,0) 정도로 이해하면 편함)
  - align-items: start; (교차축의 시작점 (flex-container의 y축 제일 상단))
  - align-items: end; ( 제일 하단. )



- justify-content
  - flex 요소의 수평방향 정렬방식을 설정하는것.
  - justify-content: flex-start; (기본 설정이며, 플렉스 컨테이너의 앞쪽부터 배치하는것. 띄움 없음)
  - justify-content: flex-end; (뒤쪽부터.)
  - justify-content: center; (가운데부터, 마찬가지로 띄움 없음)
  - justify-content: space-between ( 요소들 사이에서만 여유공간이 생김. )
    - (1 2 3 4 5)
  - justify-content: space-around ( 요소들 앞뒤, 사이 모두 여유공간이 생김.)
    - ( 1  2  3  4  5 )