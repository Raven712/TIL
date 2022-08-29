# HTML 정리



- 태그는 요소임. (여는태그, 컨텐츠, 닫는태그 < 전부다 요소)
  - 요소는 속성을 가질수있음. (class도 속성)
  - 속성은 요소이름, 등호(속성 이름 뒤), 인용부호 ( " " )가 필수적임
  - <a href="https://google.com"></a>



- HTML 문서 구조

  ```html
  <!DOCTYPE html>   << 그냥 동작하게 하는것
  <html> << html 요소. 이 요소가 페이지 전체의 컨텐츠를 감쌈. 루트요소라고도 불림
    <head> << html 페이지에 포함된 모든것 (페이지 조회자에게 보여줄것 + 보여주지 않을 것)의 컨테이너
      <meta charset="utf-8"> << utf-8이라는 문자셋을 이 문서에 사용하겠다는 뜻. (거의 모든언어 사용가능해짐)
      <title> 제목 </title> << 로드되는 브라우저의 탭에 제목이 표시됨
    </head>  
    <body>
      <img src="https://search.pstatic.net/common/?src=http%3A%2F%2Fblogfiles.naver.net%2FMjAyMTA2MTJfMTIy%2FMDAxNjIzNDU2Njg5MzEx.VBM_aDr1ADD1XpCo29sT1FyEBpqcbATJQqeJqTYyazog.9AyO2aeqL62gBhkGHjv_PKVJ8x1spngwiEihJcMbN1gg.JPEG.rhaxoddl3590%2FIMG_5493.JPG&type=sc960_832" alt="Dog">  
    </body>    
  </html>
  ```

  alt : 이미지를 볼수없는 사람에게 설명하기 위한 주석같은것



- HTML의 제목은 <h1> ~ <h6> 까지 6개 있음 ( # 같은것)

- 문단은 <p> .

- 목록은 <ul> , <ol> 이 있고, 사용은 이런식으로 함 (unordered ordered)

  ```html
  <p> 목록 </p>
  <ul>
    <li>1</li>
    <li>2</li>
    <li>3</li>   
  </ul>
  ```



- 연결은 <a> 로 함. (하이퍼링크 걸기?  타이포라의 [제목] (url주소) 같은것)

  ```html
  <a href="url 주소">제목</a>   //// href 자체가 hypertext reference
  ```

  