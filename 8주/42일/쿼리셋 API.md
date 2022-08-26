# 쿼리셋 API



- gt
  - Entry.objects.filter(id__gt = 4) ---> greater than 의 의미 
    - 즉 여기선 where id > 4 와 같은의미
    - 반대로 말하면 filter(id > 4) 이런건 안된다는것? (인자가 조건식이면안됨)



- gte
  - Entry.objects.filter(id__gte = 4) -- > greater than equal (이상)
    - where id >= 4

- 그럼 미만은? lt. 
- 이하는 lte.  (less than)



- in
  - Entry.objects.filter(id__in = [1, 3, 4])
  - Entry.objects.filter(headline__in = 'abc') 
    - 포함관계 ( id가 [1,3,4]에 있다면 --> where id IN [1,3,4] )



- startswith
  - Entry.objects.filter(headline__startswith = 'Lennon')
    - where headline LIKE 'Lennon%' 과 같음.  (레논으로 시작하는지)



- istartswith
  - Entry.objects.filter(headline__istartswith = 'Lennon')
    - WHERE headline ILIKE 'Lennon%'; 과 같음. 
    - I ??
      - 대소문자 구분안한다는말

- endswith 는 %가 앞에있는것.



- contains
  - Entry.objects.get(headline__contains='Lennon') 
  - 포함이니끼 where headline LIKE '%Lennon%'; 과 같음
    - 마찬가지로 icontains도 있음



- range
  - 그냥 range 함수와 같음
  - Entry.objects.filter(date__range = (start_date, end_date) )
    - Where date BETWEEN start_date AND end_date; 와 같다.



- 복합
  - qs = Blog.objects.filter(name__contains = 'Cheddar')
  - entries = ENtry.objects.filter(blog__ in = inner_qs)
    - where blog.id IN (SELECT id FROM ... WHERE NAME LIKE '%Cheddar%');



- 다른것
  - Entry.objects.all()[0]
    - SELECT ... LIMIT 1;

- 다른것
  - Entry.object.order_by('id')
    - SELECT ... ORDER BY id; 와 같음