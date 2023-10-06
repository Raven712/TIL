# Variable routing

- 사용자와 상호작용하는.  (사용자 입력에 따라 페이지가 다르게 출력되는 것.)
- **URL 주소를 변수로 사용하는것**.
  -  그것을 view함수의 인자로 넘길수 있음. (views.py에 def welcome... 한것)

- 변수값에 따라 하나의 path()에 여러페이지 연결가능.

## 그래서 어케함

- {{어쩌구}} << 이거.

- html의 form과 action을 이용해서 .
- HTML form의 속성들
  - action: 입력데이터가 어느 url로 갈지 지정
  - method: 나중에 ()





***

html의 form 태그에 대해 알아보자.

- ```html
  <form action="">
      <input type="text"><br>
      <input type="submit">
  </form>
  ```

***

- Variable Routing이 뭘까
  - routing : 길을 만든다 ? 
  - 

***

### Client가 데이터를 보내는것.

- HTML form element
  - 데이터가 전송되는 방법을 정의
  - 웹에서 사용자 정보를 입력하는 여러 방식(text, button, submit  등)을 제공하고,
    - 사용자로부터 할당된 데이터를 서버로 전송하는 역할을 담당.