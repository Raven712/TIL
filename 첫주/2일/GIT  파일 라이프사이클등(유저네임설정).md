# GIT ? 파일 라이프사이클등

untracked: 커밋된적없음

unmodified: 커밋됨, 수정x

modified: 수정o 

--

staged: add 된 상태 (untracked, modified를 ..)

commit을 하면  ? unmodified 상태가 됨

unmodified 파일을 지우면, untracked가 됨

**웬만하면 커밋은 막하면안됨(중간세이브용이 아니다?). 사용가능하기떄문에 ? **





***

## Git 설정파일 (config) ---> 

- 사용자 정보 (commit author) :커밋위해 반드시필요
  - git config --global user.name "username"
  - git config --global user.email "a@email.com"

- 설정확인
  - git config --global --list