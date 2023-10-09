# DB 3일_2_ORM조작

**기본적으로 python manage.py shell_plus로 들어가야함**



```django
Create

- Genre.objects.create(name='발라드') 

- genre = Genre()
- genre.name = '인디밴드'
- genre.save
# 두가지는 똑같은 행위
# INSERT INTO Genre VALUES (인디밴드);

Read
- Genre.objects.all()
# SELECT * FROM Genre;
- Genre.objects.get(id=1)
# SELECT * FROM Genre WHERE PRIMARY KEY = 1;

Update
객체를 활용해서
genre = Genre.objects.get(id=1)
genre.name = '트로트'
genre.save()

Delete
마찬가지로 객체활용
genre = Genre.objects.get(id=1)
- genre.delete()
```