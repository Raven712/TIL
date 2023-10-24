# JS 2일_ECMA Script(5) 문자열

- 메서드가 다양함

  - includes, split, replace, trim..

  - ```javascript
    string.includes('value')
    문자열에 value가 존재하는지 판별 후 True / False 반환
    
    string.split('value')
    value가 없으면 문자열 그대로를 배열에 담아 반환 
    value가 빈 문자열 ('') 이면 각 문자로 나눈 배열 반환
    	ex) 'a cup'.split('') //['a', '', 'c', 'u', 'p']
    value가 기타 문자열이면 해당 문자열로 나눈 배열 반환 (' ' 같은거)
    string.split(' ')
    
    string.replace(from, to)
    	from이 있을때 1개만 to 로 교체해서 반환
    string.replaceAll(from, to) // 전부다 바꾸기
    
    string.trim() // 파이썬의 strip. 문자열 시작과 끝의 모든 공백 없앰
    string.trimStart() , string.trimEnd()
    ```



## 배열 (Array)

- 배열 길이는 array.length로 접근

  - console.log(numbers[0])
  - 다만 파이썬처럼 -1 같은 인덱스는 활용불가

- 메서드

  - reverse
  - push, pop
  - unshift, shift
  - includes
  - indexOf
  - join // 파이썬은 문자열 메서드인데 JS는 배열 메서드임
    - array.join([seperator])
      - seperator 생략시 쉼표가 기본

- 배열순회 메서드 - 메서드를 호출시 인자로 callback 함수를 받는것이 특징

  - forEach
  - map
  - filter
  - reduce
  - find
  - some
  - every..

- forEach를 살펴보면

- ```javascript
  const fruits = ['딸', '바', '멜']
  
  fruits.forEach(function(fruit) {
      console.log(fruit)
  })
  //딸
  //바
  //멜
  
  //map(int, input().split()) 이랑 비슷한거임
  //map은 int함수를 다 적용시켜주는거고..
  //forEach는 익명함수를 만들어서 각각의 인덱스를 넣어준다는거
  //console.log('딸') ('바') ('멜') 을 각각 실행시켜준것
  
  array.forEach((element, index, array) => {
      실행코드
  })
  // element : 배열 요소
  // index : 배열요소 인덱스
  // array : 배열 자체    
  
  위의 fruit쪽은 배열요소만 넣고 뒷부분을 안넣은것 뿐
  JS는 그래도 돌아가니까 저렇게 나온거임   
                
  array.map((element, index, array)) => {
      실행코드
  })    
  ```

- reduce

  - array.reduce((acc, element, index, array) => {
  - 실행코드} , initialValue)
    - acc
      - 이전 콜백함수의 반환값이 누적되는 변수
    - initialValue
      - 최초 콜백함수 호출시 acc에 할당되는 값, 디폴트는 배열의 첫째값

  ```javascript
  const num_ = [1, 2, 3]
  
  const result = num_.reduce((acc, num) => {
      return acc + num
  }, 0)
  
  --> 피보나치 수열을 JS로 나타낸것
  ```
  
  