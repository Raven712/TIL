# CSS

- 특성 (property)
  - color, font-size, border-radius...



### 기본 문법

```css
선택자 {
 속성: 값;
}
```

#### 사용법

1. html 태그 속성에 입력

   - a style="~~~~" 이런식으로.. //하지만 너무 비효율적

2. style 태그에 입력

   - 헤드쪽에 style태그 만들어서 만들어주기.

     클래스를 만들어서 붙여주는것

3. css파일 불러오기

   - 사실 이게 제일나음



#### CSS 선택자

- 전체 선택자 * (모든것에 다적용)

- 태그 선택자

- class 선택자

- id 선택자 로 나뉜다 정도로 알자.

  ```css
  * {
      color: purple;
  } 
  
  div {
      color: aquamarine;
  }
  
  .container {
      color: bisque;
  }
  
  #userInfo {
      color: blueviolet;
  }
  ```

  