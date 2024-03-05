# CSS 2(박스 모델)

- HTML태그들은 다 박스모델.
  - 박스의 내용 contents
  - 박스의 안쪽여백 padding
  - 박스의 기준이 되는 바깥 테두리 border
  - 박스의 바깥여백 margin

- border-box
  - border 고정, 컨텐츠 크기 변함
- content-box
  - 컨텐츠사이즈 고정, border의 크기가 변함

**그래서 결국 border-box가 편할것. 디폴트는 박스사이징이 contents-box로 되어있음 !!**

- 컨텐츠박스는 사이즈가 틀어져버리니까..