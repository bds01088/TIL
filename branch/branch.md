# Branch



## git branch 명령어

- 브랜치 `생성, 삭제, 조회` 명령어

```bash
#브랜치 조회
$ git branch #별표시가 있는게 현재 브랜치라는 뜻

#원격 저장소의 브랜치 목록 확인
$ git branch -r

#브랜치 생성
$ git branch {브랜치이름}

#브랜치 삭제
#병합된 브랜치 삭제임(수정내역을 합치고 난 후에 삭제 가능)
$ git branch -d {브랜치이름}

#병합안된 브랜치 강제 삭제
$ git branch -D {브랜치이름} #주의하기
```



## git switch

- 현재 브랜치에서 다른 브랜치로 `HEAD`를 이동시키는 명령어
- `HEAD`는 현재 브랜치를 가리키는 포인터

```bash
#다른 브랜치로 이동
$ git switch {다른 브랜치이름}

#브랜치 생성과 동시에 이동
$ git switch -c {다른 브랜치이름}



```

- **주의사항** 

  git switch 하기 전에 commit 했는지 파악