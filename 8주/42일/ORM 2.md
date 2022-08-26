# ORM 2



- 장르, 앨범, 아티스트의 관계

```python
class Genre(models.Model):
    name = models.CharField(max_length = 30)
class Artist(models.Model):
    name = models.CharField(max_length = 30)
	debut = models.DateField()
    
    # 장르는 앨범을 0~N개 가짐
class Album(models.Model):
    name = models.CharField(max_length = 30)
    genre = models.ForeignKey('Genre', on_delete = models.CASCADE)
	# 앨범에 있어서 장르 아이디는 FK인데, 캐스케이드?
    # 근데 이걸 genre로 하면 필드가 genre_id로 기록이 됨! (foreignkey는 이렇게됨.)
    # 즉 genre_id 이렇게하면 안됨 !
    
   	artist = models.ForeignKey('Artist', on_delete = models.CASCADE)
```

- models.ForeignKey 필드
  - 2개의 필수위치 인자
    - Model class : 참조하는 모델
    - on_delete : 외래 키가 참조하는 객체가 삭제되었을때 처리방식
      - Cascade : 부모객체(참조된 객체)가 삭제됐을때 이를 참조하는 객체도 삭제함.
        - ex) 글이 지워지면 댓글도 지워져야함.
      - Protect : 삭제되지않음
        - ex) 댓글이 있으면 글을 지우지못함
      - Set_Null : Null 설정
      - Set_Default : 기본 값 설정



- 앨범의 아디가 1인것의 장르 이름은? (참조)
  - album = Album.objects.get(id = 1)
  - album.genre	              ( genre의 객체 (인스턴스) ) -> 앨범의 장르니까 인스턴스
  - album.genre.name

- id가 1인 장르의 모든 앨범을 어떻게 가져올까? (역참조)
  - g1 = Genre.objects.get(id = 1)
  - g1.album_set.all()           --> 역참조는 _set 다는게 국룰 (앨범의 인스턴스가 담긴 쿼리셋)
    - 1이 트로트라면 , 이 말은 트로트인 앨범들 (쿼리셋)
  - print(g1.album_set.all().query)

