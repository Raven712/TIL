### 1. 모든 테이블의 이름을 출력하세요.
```sql
sqlite> .table

albums          employees       invoices        playlists
artists         genres          media_types     tracks
customers       invoice_items   playlist_track
```

### 2. 모든 테이블의 데이터를 확인해보세요.
| 공백은 있는지 NULL은 있는지 데이터 타입은 어떤지 등등 데이터를 직접 확인해보세요.


### 3. 앨범(albums) 테이블의 데이터를 출력하세요.
| 단, `Title`을 기준으로 내림차순해서 5개까지 출력하세요.
```sql
sqlite> SELECT * FROM albums ORDER BY title DESC LIMIT 5;


AlbumId  Title                         ArtistId
-------  ----------------------------  --------
208      [1997] Black Light Syndrome   136
240      Zooropa                       150
267      Worlds                        202
334      Weill: The Seven Deadly Sins  264
8        Warner 25 Anos                6
```

### 4. 고객(customers) 테이블의 행 개수를 출력하세요.
| 단, 컬럼명을 `고객 수`로 출력하세요.
```sql
sqlite> SELECT COUNT(*) AS '고객 수' FROM customers;


고객 수
----
59
```

### 5. 고객(customers) 테이블에서 고객이 사는 나라가 `USA`인 고객의 `FirstName`, `LastName`을 출력하세요.
| 단, 각각의 컬럼명을 `이름`, `성`으로 출력하고, `이름`을 기준으로 내림차순으로 5개까지 출력하세요.
```sql
sqlite>  SELECT [Firstname] AS '이름', [lastname] AS '성'  FROM customers WHERE Country = 'USA' ORDER BY '이름' DESC LIMIT 5;

이름        성
--------  ------
Frank     Harris
Jack      Smith
Michelle  Brooks
Tim       Goyer
Dan       Miller
```

### 6. 송장(invoices) 테이블에서 `BillingPostalCode`가 `NULL` 이 아닌 행의 개수를 출력하세요.
| 단, 컬렴명을 `송장수`로 출력하세요.
```sql
SELECT COUNT(*) AS '송장수' FROM invoices WHERE [BILLINGPOSTALCODE] IS NOT NULL;

송장수
---
384
```

### 7. 송장(invoices) 테이블에서 `BillingState`가 `NULL` 인 데이터를 출력하세요.
| 단, `InvoiceDate`를 기준으로 내림차순으로 5개까지 출력하세요.
```sql
SELECT * FROM invoices WHERE [BILLINGSTATE] IS NULL ORDER BY [INVOICEDATE] DESC LIMIT 5;


InvoiceId  CustomerId  InvoiceDate          BillingAddress                            BillingCity   BillingState  BillingCountry  BillingPostalCode  Total
---------  ----------  -------------------  ----------------------------------------  ------------  ------------  --------------  -----------------  -----
412        58          2013-12-22 00:00:00  12,Community Centre                       Delhi                       India           110017             1.99
411        44          2013-12-14 00:00:00  Porthaninkatu 9                           Helsinki                    Finland         00530              13.86
410        35          2013-12-09 00:00:00  Rua dos Campeoes Europeus de Viena, 4350  Porto                       Portugal                           8.91
404        6           2013-11-13 00:00:00  Rilska 3174/6                             Prague                      Czech Republic  14300              25.86
403        56          2013-11-08 00:00:00  307 Macacha Guemes                        Buenos Aires                Argentina       1106               8.91
```

### 8. 송장(invoices) 테이블에서 `InvoiceDate`의 년도가 `2013`인 행의 개수를 출력하세요.
| `strftime`를 검색해서 활용해보세요.
```sql
select count(*) from invoices where strftime('%Y', invoicedate) = '2013';

count(*)
--------
80
```

### 9. 고객(customers) 테이블에서 `FirstName`이 `L` 로 시작하는 고객의 `CustomerId`, `FirstName`, `LastName`을 출력하세요.
| 단, 각각의 컬럼명을 `고객ID`, `이름`,`성`으로 출력하고, `고객ID`을 기준으로 오름차순으로 출력하세요.

```sql
SELECT [CustomerId] AS '고객ID', [FirstName] AS '이름', [LastName] AS '성' FROM customers  WHERE FIRSTNAME LIKE 'L%';


고객ID  이름        성
----  --------  ---------
1     Luis      Goncalves
2     Leonie    Kohler
45    Ladislav  Kovacs
47    Lucas     Mancini
57    Luis      Rojas
```

### 10. 고객(customers) 테이블에서 각 나라의 고객 수와 해당 나라 이름을 출력하세요.
| 단, 각각의 컬렴명을 `고객 수`,`나라`로 출력하고, 고객 수 상위 5개의 나라만 출력하세요.

```sql
SELECT COUNT(*) AS '고객 수', country AS '나라' FROM customers GROUP BY country ORDER BY count(*) desc limit 5;


고객 수  나라
----  -------
13    USA
8     Canada
5     France
5     Brazil
4     Germany
```

### 11. 앨범(albums) 테이블에서 가장 많은 앨범이 있는 Artist의 `ArtistId`와 `앨범 수`를 출력하세요.
```sql
select artistid, max(cnt) from (SELECT artistid, COUNT(*) as cnt FROM ALBUMS GROUP BY ARTISTID)

artistid  max(cnt)
--------  --------
90        21
```

### 12. 앨범(albums) 테이블에서 보유 앨범 수가 10개 이상인 Artist의 `ArtistId`와 `앨범 수` 출력하세요
| 단, 앨범 수를 기준으로 내림차순으로 출력하세요.

```sql 
SELECT COUNT(*) AS '앨범 수', artistid FROM albums group by ARTISTID HAVING count(*) > 10 ORDER BY COUNT(*) DESC;


앨범 수  ArtistId
----  --------
21    90
14    22
11    58
```

### 13. 고객(customers) 테이블에서 `State`가 존재하는 고객들을 `Country` 와 `State`를 기준으로 그룹화해서 각 그룹의 `고객 수`, `Country`, `State` 를 출력하세요.
| 단, `고객 수`, `Country` 순서 기준으로 내림차순으로 5개까지 출력하세요.

```sql 
SELECT COUNT(*) AS "고객 수", COUNTRY, STATE FROM customers WHERE STATE IS NOT NULL GROUP BY COUNTRY, STATE ORDER BY "고객 수" DESC, COUNTRY DESC LIMIT 5;


고객 수  Country  State
----  -------  -----
3     USA      CA
3     Brazil   SP
2     Canada   ON
1     USA      WI
1     USA      WA
```

### 14.  고객(customers) 테이블에서 `Fax` 가 `NULL`인 고객은 'X' NULL이 아닌 고객은 'O'로 `Fax 유/무` 컬럼에 표시하여 출력하세요.
| 단, `CustomerId`와 `Fax 유/무` 컬럼만 출력하고, `CustomerId` 기준으로 오름차순으로 5개까지 출력하세요. 

```sql 
SELECT CUSTOMERID, CASE
WHEN FAX IS NULL THEN 'X'
WHEN FAX IS NOT NULL THEN 'O'
END
AS 'FAX 유/무'
FROM customers
ORDER BY CUSTOMERID ASC LIMIT 5;


CustomerId  FAX 유/무
----------  -------
1           O
2           X
3           X
4           X
5           O

```

### 15. 점원(employees) 테이블에서 `올해년도 - BirthDate 년도 + 1` 를 계산해서 `나이` 컬럼에 표시하여 출력하세요.
| 단, 점원의 `LastName`, `FirstName`, `나이` 컬럼만 출력하고, `EmployeeId`를 기준으로 오름차순으로 출력하세요.

| cast(), strftime(), 오늘 날짜를 구하는 함수를 검색하고, 활용해보세요.

```sql 
sqlite>  select Lastname, Firstname, DATETIME('NOW', 'LOCALTIME') - CAST(BIRThDATE AS INTEGER) + 1 AS "나이" FROM employees ORDER BY employeeid;



LastName  FirstName  나이
--------  ---------  --
Adams     Andrew     61
Edwards   Nancy      65
Peacock   Jane       50
Park      Margaret   76
Johnson   Steve      58
Mitchell  Michael    50
King      Robert     53
Callahan  Laura      55
```

### 16. 가수(artists) 테이블에서 앨범(albums)의 개수가 가장 많은 가수의 `Name`을 출력하세요.
| artists 테이블과 albums 테이블의 `ArtistId` 활용하세요.
```sql 
```

### 17. 장르(genres) 테이블에서 음악(tracks)의 개수가 가장 적은 장르의 `Name`을 출력하세요.
| genres 테이블과 tracks 테이블의 `GenreId` 활용하세요.
```sql 
```


### 자유롭게 문제를 만들어 보시고, 디스코드 채널에 공유해보세요!
