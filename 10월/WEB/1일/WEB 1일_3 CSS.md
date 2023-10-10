# WEB 1일_3 CSS

## CSS

- 캐스케이딩 스타일 시트
  - 위에서부터아래로 흐르는 스타일시트



- h1 태그를 꾸며보자

- ```html
  <style>
      h1 {
          color: blue; <!-- color는 속성(property), blue는 값(value)! -->
          font-size: 15px;
      }
  </style>
  이렇게 할수도있고, 태그 자체를 <h1 color 뭐시기> 이렇게 꾸밀수도 있는데
      
  제일 좋은건 css파일을 따로만들어서 head태그에 link로 넣는게 좋다
     
  ```

```html
하지만 태그 선택자를 바꾸면, 여러가지 h1 태그들이 한번에 바뀌기 때문에
보통은 클래스를 만들어서 쓴다.

<style>
    .title-brown {             ----- 여기서 .은 클래스를 의미한다!
        color: brown;
    }
    .title-yellow {
        color: yellow;
    }
</style>
<h1 class="title-brown">갈색</h1>

이런식으로 해주는게 더 일반적이다.

그리고 우선 지정순위가 다른데 (ID > CLASS > 태그)
CLASS가 지정되면, 태그에서 아무리 바꿔도 CLASS에서 지정된게 먼저 지정된다
(CLASS에서 갈색, 태그에서 파란색하면 갈색적용임) // 그러나 일반적으로 클래스로만 스타일링한다.

그리고 클래스가 둘이상 지정되면, CSS STYLE에서 늦게 쓰인것 (CASCADING 이라서)이 적용된다.
위의 예시에선, 클래스를 brown, yellow 둘다 적용시키면 아래에 있는 yellow 클래스가 적용된다.
```



- 개발자 도구로 보기
  - computed