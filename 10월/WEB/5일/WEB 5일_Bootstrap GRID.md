# WEB 5일_Bootstrap GRID

- 반응형 디자인, 일관성 있는 요소 배치 등에 쓰임



### 기본 요소

- Column: 실제 컨텐츠를 포함하는 부분
- Gutter: 칼럼과 칼럼 사이의 공간 (사이간격)
- Container: Column들을 담고있는 공간



- container, rows, column 으로 컨텐츠를 배치하고 정렬함

- **반드시 기억해야할 2가지**
  - 12개의 컬럼
  - 6개의 grid breakpoints
    - breakpoint: 화면 너비에 따라 배치를 어떻게 하는지에 대한 중단점

```html
<div class="container">
    <div class="row">
        <div class="col">
        </div>
        <div class="col">
        </div>
        <div class="col">
        </div>
    </div>
</div>
위의경우 12개의 컬럼영역을 3개의 div가 나눠서 써서, col-4와 같아지고,
만약 col-6 이런걸 따로 적어넣으면, 12개의 컬럼중 6개의 컬럼영역 즉 절반의 영역을 차지함..
만약 숫자를 명시한 컬럼의 합이 한줄에 12를 넘어가면 아래로 흘러내리게됨

그리고
<div class="col-12 col-sm-6 col-md-4">
</div>
이런식으로 하면, breakpoint의 sm미만 영역에선 12컬럼, sm기준 영역에선 6컬럼을 차지하는 div
md에선 4... 이런식이 됨
```



## Offset

- offset-md-1~12
  - 그리드 영역을 띄워놓는것
  - md는 중앙기준, 아무것도 적지않으면 그냥 자신 다음에 offset이 숫자만큼 생기는것

## Gutter

- g-0: 거터를 없앤다
- gx -12345.. : 거터를 x축 ~만큼..