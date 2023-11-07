# Django 2일(2) Model

- CRUD를 하기위해 가장먼저 해야할게 models.py 만들기



- class DB이름(models.Model): 
  - 으로 Model을 상속받는것으로 DB를 만듬, Todo List를 만드는 예시를 보자.

```django
class Todo(models.Model):
	content = models.CharField(max_length = 80) 
				# content라는 필드는 CharField이며, 속성은 최대길이 80란 뜻
				# html 파일의 input에서도 maxlength 속성을 넣어주자
				# input type ~ maxlength="80"
				# 이런식으로 프론트와 백엔드의 조건을 맞추는걸 유효성 검사라고 한다
	completed = models.BooleanField(Default = False)
				# completed 필드는 불리언 필드, 속성의 디폴트는 False
	priority = models.IntegerField(Default=3)
	created_at = models.DateField(auto_now_add=True)
				# auto_now_add 속성은 생성일자의 속성에 보통 사용됨 
				# 수정일자는 auto_now
	deadline = models.DateField(null=True)
				# 마감기한(deadline)에 대해서, null이 허용되도록(True) 해놓은 것.
				# 원래 null=false가 Default임
```

이렇게 모델을 작성하고,

- python manage.py makemigrations(mm이 단축어)
- python manage.py migrate(m이 단축어) 를 하면 DB가 등록이 된다.



```html
<form action="">
  <input type="text" name="index" maxlength="80">
  <input type="submit" value="할 일 추가">
</form>
```

