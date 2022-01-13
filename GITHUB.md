# Github



## 원격 저장소와 로컬 저장소 연결

### Repsoitory 생성

* git remote

  * ```git
    git remote add origin https://github.com/bds01088/TIL.git
    ```

    origin 은 별명임

* git push



### .gitignore

touch .gitignore 로 파일생성하고 텍스트로 연결해서 열고

깃에서 관리하지않는 파일들 이름+확장자로 적어놓으면 관리 안함

관리안할 파일들과 동일한 위치거나 그 상위 위치에 존재해야함

프로젝트 시작할 때 가장 먼저 생성하는게 편함

* 원격 저장소에도 파일이 있고, 로컬에도 이미 있고, 이미 트래킹중인 파일을 로컬에서만 더이상 추적하지 않도록 설정

```bash
$ git update-index --assume-unchanged {File name}
```

* 로컬에 있는 파일 변동 추적 멈춤
* 원격 저장소에 해당 파일이 이미 있다면 그 파일 삭제(원격 저장소에 push 할때 삭제)

``` bash
$ git rm --cached {file name}
```

* 로컬, 원격 저장소 모두 파일 삭제 후 추적 중지
  * git에 삭제되었다는 정보가 남겨지지않음

```bash
$git rm {file name}
```

tip. [gitignore.io](gitignore.io) 라는 사이트에서 원하는 언어들의 파일을 관리 안하도록 하는 자동생성 사이트가 있음



