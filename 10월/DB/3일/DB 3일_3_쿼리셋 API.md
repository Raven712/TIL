# DB 3일_3 _쿼리셋 API

- gt (~보다 큰것)
  - Entry.objects.filter(id__gt=4)
    - SELECT * FROM Entry WHERE id > 4;

- gte(~이상)
  - Entry.objects.filter(id__gte=4)

- lt (미만)
- lte(이하)



- in (특정값 내에서 여러개 선택. 조건내에 있는게 일치하면 true)
  - Entry.objects.filter(id__in=[1, 3, 4])
  - Entry.objects.filter(headline__in='abc')
    - SELECT * FROM Entry WHERE id IN (1, 3, 4);
    - SELECT * FROM Entry WHERE headline IN ('a', 'b', 'c';)
      - 헤드라인에 a,b,c중 하나가 있으면 read해옴



- startswith (~로 시작, LIKE)
  - Entry.objects.filter(headline__startswith='Lennon')
    - SELECT * FROM Entry WHERE headline LIKE 'Lennon%';

- istartswith (ILIKE, 대소문자 구분x LIKE)

- contains

  - Entry.objects.get(headline__contains='Lennon')
    - SELECT * FROM Entry WHERE headline Like '%Lennon%';

  

- range

  - Entry.objects.filter(pub_date__range=(start_date, end_date))
    - SELECT * FROM Entry WHERE pub_date BETWEEN start_date AND end_date;



- 활용
  - Entry.objects.all()[0]
    - SELECT * FROM Entry LIMIT 1;
    - 슬라이싱[N : M]을 하면 LIMIT OFFSET 같이한것과 같은효과
  - Entry.objects.order_by('id')
    - SELECT * FROM Entry ORDER BY id;
    - 내림차순은 Entry.objects.order_by('-id')