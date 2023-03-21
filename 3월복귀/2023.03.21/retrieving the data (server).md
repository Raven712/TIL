# retrieving the data (server)

데이터 가져오기

- request 객체 살펴보기
  - print(request)를 하면
  - WSGIRequest: GET '/pong?ball=클라이언트입력값'
  - print(dir(request)) < request라는 객체가 무엇을 가지고있는지 보여줌