# HTML 새로정리



```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>			 << 메타데이터들.
</head>
<body>
    
</body>
</html>
```

- html : 문서 최상위요소
- head : 문서 메타데이터 요소. (제목, 인코딩, 스타일 등.)

- body : 문서 본문 요소 (실제 화면구성과 관련된것)



### head

- <타이틀> : 브라우저 상단타이틀
- <메타> 문서 레벨 메타데이터 요소

- <링크> : 외부리소스 연결요소 (CSS, favicon 등 - 파비콘 : 즐겨찾기 이미지아이콘. favorite icon)

- <스크립트> : 스크립트 요소(JS 파일코드 등)
- <스타일> : CSS 직접 작성한것.



```html
<head>
	<title>HTML 수업</title>
	<meta charset="UTF-8">
	<link href="style.css" rel="stylesheet">
	<script src="javascript.js"></script>
	<style>
	p {
		color: black;
        }
    </style>
</head>
```

***



### 요소(element)

HTML의 요소는, -> 여는태그  닫는태그 ( <> 들 ) 그리고 내용으로 구성됨.

- 닫는태그 없는 태그들도 있음. br hr img input link meta



### 속성(attribute)

- 태그 부가적 정보설정.
- id, class, title , style등이 있음. 



```html
<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="UTF-8">
	<title>Document</title>
</head>
<body>
	<!-- 이것은 주석입니다. -->
	<h1>나의 첫번째 HTML</h1>
	<p>이것은 본문입니다.</p>
	<span>이것은 인라인요소</span>
	<a href="https://www.naver.com">네이버로 이동!!</a>
</body>
</html>
```

HTML 코드 예시





### 인라인, 블록요소

- HTML 요소는 인라인 / 블록 요소로 나뉨.
- 인라인 요소는 글자처럼 취급
- 블록 요소는 한줄 모두 사용



태그들

- <에이> : 하이퍼링크 걸기.
- <비> : 굵은글씨. 스트롱이랑 비슷함
- <아이> : 이탤릭체. em이랑 비슷함.
- <비알> : 줄 바꿈
- <이미지(img)> : 이미지. src속성으로 이미지표현, alt속성은 주석
- <스팬> : 그냥 인라인 컨테이너



- <피> : 문단 ( 패러그래프 )
- <에이치알> : 수평선. 문단레벨요소에서 주제분리
- <오엘, 유엘> : 순서 있/없는 리스트
- <디브> : 의미없는 블락 컨테이너