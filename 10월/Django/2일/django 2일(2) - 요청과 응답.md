# django 2일(2) - 요청과 응답

- 웹을 통한 요청은 URL을 통해,
- 응답은 문서 (HTML)로 받는것.



- URL -> VIEW -> Template 순의 작성 순서로 코드작성, 데이터 흐름 이해하기
  - 1. 주문서 정의 ---> URL (urls.py에 담기)
    2. 로직 구현 ---> views.py
    3. HTML 페이지 구성 ---> template (html파일들)