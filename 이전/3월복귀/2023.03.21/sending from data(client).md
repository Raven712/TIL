# sending from data(client)

- HTML의 form 요소

  - 데이터가 전송되는 방법을 정의
  - 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit 등) 제공, 사용자로부터 할당된 데이터를 서버로 전송하는 역할 담당
  - 데이터를 어디(action)로 어떤 방식(method)으로 보낼지.

  - 핵심 속성
    - action
      - 입력 데이터가 전송될 URL 지정
      - 데이터가 어디로 보낼 것인지 지정하는것이며, 반드시 유효한 URL이어야함
      - 이 속성을 지정하지않으면 데이터는 현재 form이 있는 페이지의 url로 보내짐
    - method
      - 데이터를 어떻게 보낼지에 대한 정의
      - 입력 데이터의 HTTP request methods를 지정
      - HTML form 데이터는 오직 2가지 방법으로만 전송할 수 있는데 GET, POST로만 가능 (정의안하면 GET)
        - GET은 어떤 데이터를 가져오기위해 보내는 데이터 
        - POST는 차후 배움



- 검색을 하면..
  - https://search.naver.com/search.naver?query=아이유
    - 이런식으로 나오는데, 주소는 https://search.naver.com
      - 주문서는 /search.naver?query=아이유
      - ?는 query parameter
    - 그리고 https://search.naver.com/search.naver? 여기는 form에 정의한 내용
    - query=아이유 여기는 input으로 정의한 데이터