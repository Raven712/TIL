# GIT(분산 버전 관리 시스템)

버전? : 컴퓨터 소프트웨어의 특정 상태

파일 변경사항 추적, 여러사용자 파일 조율



#### ★ 1번통 : working directory , 2번통 staging area , 3번통 버전 (commit)



### . << "모든" (rm -rf '.git' < 이하모든git 다삭제)



##### 명령어

1. git init (해당폴더 마스터로 ..)
2. git status (폴더에 있는일 추적)
3. commit (버전기록)



1. 작업
2. 변경된 파일 모으기(add) --> 스테이징에이리어에 잠시두기
3. 버전으로 남김(commit) --> 기록하기

스테이징에이리어?왜필요할까

지금버전에 등록할 변경점만 스테이징에이리어에 옮기고 버전으로 만들고 하려고

( 버전기록파일 모으는용도 ?)



#### add

git add 파일이름

워킹디렉토리 내용(1번통)을 스테이징에이리어(2번통)로 추가

- untracked 상태를 staged 로 바꿈
- modified도 staged로



#### commit 

git commit -m '커밋메시지'



git은 파일을 modified, staged, committed로 관리

- 모디 : 파일이 수정된 상태.
- 스테 : 곧 커밋할상태
- 커맛 :ㅇㅇ



#### git status (워킹디렉토리, 스테이징에이리어)

nothing to commit (스테이징에이리어 비었다)

working tree clean : 변경된것도 없다 (1번통도 그대로다)

untracted file (파일이 1통에 있다. 즉 한번도 git으로 관리되지않은파일)



#### git log ( 레포지토리 )

- 저장된 커밋조회
- 로그조회(버전조회)

git log -1 : 최근한개 보여줌

git log --oneline : 한줄로 표시

git log -2 --oneline : 최근 두개를 한줄로 표시

