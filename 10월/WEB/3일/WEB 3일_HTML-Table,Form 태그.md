# WEB 3일_HTML-Table,Form 태그

## Table 태그

- thead, tbody, tfoot 이라는 자식요소를 활용함(태그)
  - 테이블의 칼럼명 부분이 thead
    - 칼럼 ID, Name, Major...
  - 내용물은 tbody
    - Id 1,2,3... , 길동,철수...
  - 총계 2명 이런건 tfoot



- tr로 가로줄 구성, 내부엔 th, td로 셀을 구성.
- colspan, rowspan 속성으로 셀 병합
  - colspan="2" ..

```html
<body>
   <table>
       <thead>
           <tr>
               <th>Id</th>
               <th>Name</th>
               <th>Major</th>
           </tr>
       </thead>
       <tbody>
           <tr>
               <td>1</td>
               <td>길동</td>
               <td>경제</td>
           </tr>
       </tbody>
       <tfoot>
           <tr>
               <td>총계</td>
               <td colspan="2">2명</td>
           </tr>
       </tfoot>
       <caption>1반 학생 명단</caption>
    </table>
</body>

<!--대충 이런식-->
```



## Form

- 폼태그는 데이터를 서버에 제출하기 위해 쓰는 태그
  - action : 폼을 처리할 서버의 URL(데이터를 보낼곳)
  - method: form을 제출할때 사용할 http 메서드(get, post)
  - enctype: 메서드가 post인 경우 데이터유형



```html
<form action="/search" method="GET">
    <input type="text" name="q">
 
</form>
```



- input label

  - input에 초점을 맞추거나 활성화 시킴

    - 사용자는 선택영역이 늘어나 편하게 사용할수있음
    - 내용확인을 쉽게하게함

  - ``` id
    <label for="agreement">어쩌구</label>
    <input type="checkbox" name="agreement" id="agreement" value="1">
    
    여기서 for agreement와 id agreement가 일치해야함
    ```



결국 사용자가 입력-선택을 하면

id가 value로 매핑되어 서버로 넘어간다.. 그정도로 이해하자