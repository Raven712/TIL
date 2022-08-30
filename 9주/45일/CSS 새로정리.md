# CSS 새로정리



h1 { color: blue; font-size: 15px; } 

- h1 : 선택자
- color : blue --> 선언
- font-size -- >속성
- 15px -- > 값.



CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택함.

```html
!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<title>Document</title>
    <style>
		h1 {					
			color: blue;		<<<< 여기가 내부참조로 CSS를 정의한것. 국룰
			font-size: 100px;
        }
</head>
<body>
</body>
</html>
```

위의 방법이 아니면 그냥 css 파일을 따로만들어서 그걸 참조하는식이 있음.



<헤드> 내부에서 <링크 rel = "stylesheet" href= "css파일명" > 이렇게. css파일에 스타일이 존재하는것.

```html
h1 {					
	color: blue;		<<<< 여기가 내부참조로 CSS를 정의한것. 국룰
	font-size: 100px;
}
```

저것만 css파일에 존재하느것



### CSS 기초선택자

- 요소 선택자
  - HTML 태그를 직접 선택

- 클래스 선택자 
  - . 으로 시작함
- 아이디선택자
  - #으로 시작함..



## CSS 기본 스타일

**크기단위**

- 픽셀 - 고정적인 단위
- % - 퍼센트.

- em
  - 바로 위 부모요소에 대한 상속영향 받음.
  - 배수단위, 요소에 지정된 사이즈에 상대적인 사이즈 가짐.
- rem
  - 상속 영향 안받음.
  - 최상위 요소(html) 사이즈 기준으로 배수단위를 가짐

뭔말?

- 일단 텍스트 크기 조절할떄 쓰는 상대길이들임. (em, rem)
- 해당요소 글꼴 크기가 1em
- rem은 html의 폰트사이즈가 1 rem. html의 폰트사이즈가 10픽셀이면 1rem = 10px



- p{ color : rgba(0, 0, 0, 0.5) } 일때  ,a << 이건 투명도.



**기타 CSS 문서표현들은 MDN 문서를 찾아보는게 좋음.**



**CSS 적용 우선순위가 있긴함. important는 건들면 안된다 ? **



