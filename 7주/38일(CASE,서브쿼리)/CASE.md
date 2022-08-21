# CASE

- 특정상황에서 데이터를 변환활용하는것.

  ```python
  CASE
  	WHEN 조건식 THEN 식
      WHEN 조건식 THEN 식
      ELSE 식
  END
  END 를 생략하면 NULL 값이 저장됨
  ```

  

```python
실제론

 ID GENDER
 1    1 뭐 이런식으로 쭉 저장되어있음 (db에)
 2    1
 3    0 
```

- 이걸 성별 남자여자로 하고싶으면 ?( GENDER 를 )

``` python
CASE
	WHEN GENDER = 1 THEN GENDER = '남자'
    WHEN GENDER = 0 THEN GENDER = '여자'
    ELSE
END

SELECT id, gender FROM users ; 에서, gender칸에 CASE 문을 쓰면됨.

-->
SELCET
	id,
    CASE
    	WHEN gender = 1 THEN '남자'
        WHEN gender = 2 THEN '여자'
        --- (ELSE) 넣지않으면 ELSE해당되는게 NULL로 출력됨.
    END --- (AS 성별) 까지 붙이면 CASE로 출력되는 필드가 성별로 출력됨.
FROM users
LIMIT 5;
```



***참고*** DISTINCT : 그냥 특정 필드의 구성이 어떻게되어있는지 알려줌

ex) SELECT DISTINCT smoking FROM healthcare; --> smoking의 구성요소 1, 2, 3이 출력됨.



하여튼 이런식으로 CASE WHEN age <= 18  18 < age <= 30 이런식으로 구분해서 청소년 청년 등으로 구별할수있음. ! 