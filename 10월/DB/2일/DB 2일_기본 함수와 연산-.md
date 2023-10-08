# DB 2일_기본 함수와 연산-

- 문자열 함수
  - SUBSTR(문자열, start, length) : 자르기.
    - 시작 인덱스는 1, 마지막 인덱스는 -1
  - TRIM, LTRIM, RTRIM : 문자열 공백 제거
  - LENGTH(문자열) : 길이
  - REPLACE(문자열, 패턴, 변경값) : 패턴에 일치하는 부분 변경
    - SELECT REPLACE(phone, '-', '') FROM users LIMIT 5;
      - 전화번호의 하이픈을 공백으로 바꿔서 5명 추출.
  - UPPER(문자열), LOWER(문자열) : 대소문자 변경
  - || : 문자열 합치기
    - SELECT last_name || first_name 이름 FROM users  LIMIT 5;
      - 성+이름을 이름으로 명명해서 5명 출력
      - 굳이 AS를 붙이지 않는듯





- 숫자열 함수

  - ABS(숫자) : 절댓값

  - ROUND(숫자) : 반올림

  - SIGN(숫자) : 부호 (양1, 음 -1, 0 0)

  - CEIL(숫자) : 올림

  - FLOOR(숫자) : 내림

    