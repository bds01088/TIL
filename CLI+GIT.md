# CLI

## GUI vs CLI

1. GUI (그래픽 유저 인터페이스)
   그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식
2. CLI (커맨드 라인 인터페이스)
   터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식

### CLI를 사용하는 이유

1. GUI에서 새폴더 만들기 : 우클릭 - 새로만들기 - 폴더 - 폴더명
2. CLI에서 새폴더 만들기 : mkdri 폴더명
                파일 옮기기 : mv 옮길대상 담을파일명/

### CLI에서 중요한 점은 작업 위치(경로)

루트 디렉토리(/) -> windows의 경우 일반적으로 c드라이브를 의미
홈 디렉토리(~) -> 사용자의 폴더

#### 상대경로

./ = 현재 작업하고 있는 폴더를 의미
../ = 현재 작업하고 있는 폴더의 상위 폴더

tip. ctrl + L 하면 화면 초기화

### 명령어

#### cd 폴더명 : 현재 작업중인 디렉토리를 변경하는 명령어

tip. 폴더명 tab으로 자동완성
cd : 홈 디렉토리로 이동
cd .. : 상위폴더로 이동

#### ls (list segments) : 현재 작업중인 디렉토리의 폴더/파일 명을 보여주는 명령어

ls -a : 숨겨진것 까지 모두 보여주는 명령어
ls -l : 길게 출력
ls -a -l : 두옵션 같이 사용하기

#### mkdir (make directory) : 폴더 생성하는 명령어

mkdir 폴더명 (ex. mkdir folder1 folder2 folder3 ----)
폴더 이름 사이에 공백 넣으려면 따옴표로 묶어서 입력 (ex. mkdir "my folder")

#### touch : 파일을 생성하는 명령어

touch 파일명
폴더 생성과 동일한 생성방법
숨김파일로 생성하고싶다면 파일명 앞에 .붙이기

#### start 또는 open : 폴더 / 파일을 여는 명령어

#### rm (remove) : 삭제

GUI는 휴지통으로 보내지만
CLI는 완전삭제(shift+del)
rm 파일.확장자 : 파일 삭제
rm -r 폴더명/ : 폴더 삭제 (-r : recursive)

#### mv (move) : 이동

mv 이동시킬 파일or폴더 이동할 폴더
위치 이동할 폴더가 없다면 파일명 변경으로 작동 (ex. mv text.txt til.txt -> 파일명 변경하는거)

#### 이름 이메일 설정

git config --global user.name 이름
git config --global user.email 이메일

#### git init : 현재 작업중인 directory git으로 관리하는 명령어

주의사항 : 이미 master로 관리중인 폴더 내에서 절대로 git init 금지

#### git status : working directory와 staging area에 있는 파일들의 현재 상태를 확인

상태

* untracked : git이 관리하지 않는 파일
* tracked : git이 관리하는 파일
  a. unmodified : 최신상태
  b. modified : 수정되었지만 staging area에 반영되기 전
  c. staged : staging area에 반영된 상태

#### git add : staging area에 추가하는 명령어

git add 파일이름.확장자
git add 폴더/
git add . : 현재 디렉토리에 속한 모든 파일/폴더 추가

#### git commit : staging area에 올라온 파일들의 변경 사항을 하나의 버전으로 저장하는 명령어

커밋 메세지는 현재 변경사항을 기록하는 용도
git commit -m "커밋 메세지"

#### git log : 커밋의 내역을 조회하는 명령어

옵션

* --oneline : 한줄로 축약해서 보여줌

* --graph : 브랜치와 머지 내력을 그래프로 보여주는 명령어

* --all : 모든 브랜치의 내역

* --reverse : 커밋 내역의 순서를 반대로 보여주는 명령어