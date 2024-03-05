# HTML 2

- 태그(약속된 명령어)는 고유한 기능을 가지고 있고
  - 속성과 값으로 부가적인 기능을 구현한다.



### HTML의 핵심

#### - 1. inline / block

- 인라인태그와 블록라인 태그
  - 블록라인 태그 (div, h, hr, p)
    - 줄 하나를 통쨰로 쓰는것
  - 인라인 태그 (span, input, img, a..)
    - 한 줄의 일부영역만 사용하는태그

#### - 2. 종속 태그

- 다른태그와 상호작용을 해야 작동하는것

  - select, ol, ul,  table 태그..

    - select 태그는 자식태그안에 optgroup, option 태그를 추가로 넣어줘야함

    - ```html
      <select>
      	<optgroup>
              <option>어저꾸저쩌구</option>
          </optgroup>    
      </select>
      ```

    - ol태그, ul태그는 자식태그에 li태그들이 필요

#### - 3. HTML 문서구조

- 헤드, 바디태그 나누는것.
- 헤드태그는 검색엔진을 위한 영역 (메타데이터)
  - title태그, meta
- 바디태그는 header, nav, section, article, aside, footer 태그들.