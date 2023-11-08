# Django 3일_DB 삭제

- 삭제를 하려면 id를 GET해와서 지워야한다.

  - a태그를 통해서 지우는 페이지를 만든다?

    ```django
    {% for i in posting %}
        <li>
          제목 : {{ i.title }} 내용 : {{ i.content }} <a href="">[수정]</a> 
            <a href="{% url '앱이름:delete' i.pk %}">[삭제]</a> 	 
        <!-- href="/board/delete/{{ i.id }}">[삭제]</a> 얘도 되는데 위의 방법으로 하자 -->
            
    <!-- 여기서 pk는 동적인자이므로 urls.py에서 path(delete/<int:pk>, ~~)을 해주고
    	views.py에서도 def delete(request, pk):를 하여 동적인자를 받아와야한다 -->
    <!-- 그다음의 과정은 아래의 박스와 같이 해주면 된다 -->
    	</li>
    {% endfor %}
    ```

  - 이렇게 delete페이지를 만들어주고, 뒤에 올 파라미터를 동적 파라미터로 받아준다.

  - 이제 delete페이지를 만들러 가면되는데, urls.py에서 path를 만들어줄때 -

    - path('delete/< int:pk>', views.delete, name='delete')
      - 이렇게 해줘야한다

  - views에 가서 def를 해줄때,

    ```python
    def delete(request, pk): # path에서 pk라는 인자가 넘어오므로 해줘야함
        board1.objects.get(id=pk).delete()
        redirect('board:main')
        
    # redirect를 하므로 delete라는 html 페이지는 만들 이유가 없다
    ```

    

    