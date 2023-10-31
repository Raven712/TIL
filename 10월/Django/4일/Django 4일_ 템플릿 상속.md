# Django 4일_ 템플릿 상속



1. 부모 템플릿을 만듬.
   - {% extends '' %} 
     - 템플릿 상속에 관련된 태그
     - 반드시 템플릿 최상단에 작성되어야함
   - body 태그에는 아래와 같은 태그를 넣음
     - {% block content %}
     - {% endblock content %}

```html
{% extends 'base.html' %}

{% block content %}
 코드작성
{% endblock content %}

이러면 base.html의 css, html 형식을 전부 가져오고
base.html에서 block content~ endblock content로 설정한 body영역에 코드를 작성하게되는것
```

