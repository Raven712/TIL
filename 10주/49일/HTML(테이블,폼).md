# HTML

- 테이블 태그와 폼 태그



### 테이블

- thead, tbody, tfoot 요소가 테이블의 자식요소로 있음. (모두가 필수요소는 아님)

  ```html
  <table>
     <thead> <!-- 헤더 -->
         <tr>
             <th>아이디</th>
             <th>이름</th>
         </tr>
      </thead> 
    		<tr>
              <td>1</td>
              <td길동</td>
      	</tr>
      <tbody> <!-- 바디 -->
      </tbody>
      	<tr>
              <td>총계</td>
              <td colspan="2">2명</td>
      </tr>
      <tfoot>
      </tfoot> <!-- 푸터-->
  </table>
  ```

  

  colspan="2" < 열 병합하기.





### 폼

- 정보를 서버에 제출하기위해 사용하는 태그
- action
  - 폼을 처리할 서버의 URL ( 데이터 보낼 곳 )
- method, enctype ... 

```html
<form action="/search" method="GET">
    <input type="text" type="checkbox" name="q" value="html">    <!-- q: 쿼리의 약자로 쓰인것 -->
</form>
```

- 인풋
  - name, value, required .... 
  - 타입 - 체크박스 : 다중선택하는 체크박스.
  - type="radio" : 단일선택.