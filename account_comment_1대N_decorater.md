# Project 07 - Django

## account, comment, 1:N, decorater

#### !!알게된 주의사항!!

>##### auth와 관련되어 Django 내부적으로 accounts라는 이름이 사용되고 있기 때문에
>
>##### 계정관련 앱의 이름은 accounts로 고정시키자
>
>1. login_required decorator가 settings.LOGIN_URL에 설정된 문자열 기반 절대경로로 redirect 하기 때문에 -> LOGIN_URL의 기본값은 '/accounts/login/'임
>2. 회원정보 수정시 나타나는 비밀번호 변경 url의 기본값이 'accounts/password/'임
>     다만, url 연결점이 저렇다는거지 html이 존재하는 것은 아니므로 html을 생성해주어야함

- 로그인, 비로그인 상태를 구분해서 html의 표시를 달리해주자

- NEXT 파라미터 사용할 시 주의하기

- DTL의 for-empty태그도 있다.

  - ```django
    {% for comment in comments %}
    {% empty %}
    {% endfor %}
    ```


- User모델을 가져오는 방식의 구분

  - __models.py에서__ 유저모델 참조시

    settings.AUTH_USER_MODEL

  - __models.py가 아닌 곳__에서 참조시

    get_user_model()



## 쿠키와 세션

### 쿠키

서버가 사용자의 웹에 전송하여 컴퓨터에 설치되는 작은 기록 정보(데이터조각)

__요청__마다 쿠키를 같이 전송함

#### 사용 목적

1. 세션 관리 : 로그인, 팝업체크, 장바구니 등
2. 개인화 : 사용자 선호, 테마 설정
3. 트래킹 : 행동기록 및 분석

#### 쿠키 lifetime

1. Session cookies
   - 현재 세션이 종료되면 삭제
   - 브라우저가 현재 세션이 종료되는 시기를 정의함
2. Persistent cookies
   - Expires속성에 지정된 날짜 혹은 Max-Age속성에 지정된 기간이 지나면 삭제



### 세션

>  쿠키의 일종

사이트와 특정 브라우저 사이의 `상태`를 유지하는 것

- 서버가 특정 session ID를 발급해줌
- 클라이언트는 발급 받은 session ID를 쿠키에 저장
- ID는 세션을 구별하기 위해 필요하며, 쿠키에는 ID만 저장 => 쿠키에는 key값은 저장하지 않음



## Decorater 사용법

> ```python
> from django.views.decorators.http import
> 								require_http_methods,
>     							require_POST
>         
> from django.contrib.auth.decorators import login_required
> #======================================================
> @require_http_methods(['GET','POST'])
> @require_POST
> @login_required
> ```



## Accounts

### Login

#### AuthenticationForm

> ```python
> from django.contrib.auth.forms import AuthenticationForm
> #============================
> if request.method == 'POST' :
>     form = AuthenticationForm(request, request.POST)
> else :
>     form = AuthenticationForm()
> ```

- 사용자 로그인을 위한 Bulit-in form
- request를 첫번째 인자로 가짐 -> ModleForm이 아닌 Form이기 때문에



#### Login함수

> __login(request, user, backend=None)__
>
> ```python
> from django.contrib.auth import login as auth_login
> #========================
> form = AuthenticationForm(request, request.POST)
> if form.is_valid():
>     auth_login(request, form.get_user())
> ```

- 세션을 만들어줌



#### Logout

> __logout(request)__
>
> ```python
> from django.contrib.auth import logout as auth_logout
> #=========================
> def logout(request):
>     auth_logout(request)
>     return~
> ```

- 요청에 대한 session data를 DB에서 완전히 삭제
- 클라이언트 쿠키에서도 sessionID가 삭제됨



#### Limiting access to logged-in users

- is_authenticated attribute (로그인 되어있으면 True)

  - User model의 속성 중 하나

  ```django
  {% if request.user.is_authenticated %}
  ```

  ```python
  if request.user.is_authenticated :
      return ~
  ```

- The login_required decorater

  - login_required decorator가 settings.LOGIN_URL에 설정된 문자열 기반 절대경로로 redirect 시켜줌
  - `next`변수에 이동하고자 했던 url을 임시저장해준다.

  <hr>

  __next 사용법__

  로그인 html에 form의 action이 비어있어야 사용 가능

  ```python
  def login(request):
      #=========
      	if form.is_valid():
              auth_login(request, form.get_user())
              #or 연산자를 이용하여 next가 없다면 app_name:html_name으로 리다이렉트
              return redirect(request.GET.get('next') or 'app_name:html_name')
  ```

  > @require_POST인 곳에 @login_required를 통해 next를 사용해서 요청이 간다면
  >
  > redirect는 get요청 밖에 못하므로 POST데이터의 손실이 일어난다
  >
  > 그러므로 @login_required는 get만 처리가능한 view함수에서만 사용
  >
  > post처리하는 곳은 is_authenticated 사용하자

  <hr>



### 회원가입

#### UserCreationForm

> ```python
> from django.contrib.auth.forms import UserCreationForm
> #================
> if request.method == "POST":
>     form = UserCreationForm(request.POST)
>     #=======~
> else :
> 	form = UserCreationForm()
> ```

주어진 username과 password로 권한 없는 새 user를 생성하는 __ModelForm__

3개의 필드 보유 (username, password1, password2)

- 회원가입 후 자동 로그인

  ```python
  if request.method == "POST":
      form = UserCreationForm(request.POST)
      if form.is_valid():
  	    user = form.save()
          ##########################
          auth_login(request, user)
          ##########################
  ```

  

### 회원탈퇴

> ```python
> @require_POST
> def delete(request):
>     if request.user.is_authenticated:
> 	    request.user.delete()
>         #세션도 같이 지우기 위해서 로그아웃해줌
>         #로그아웃을 먼저 하게 되면 request에서 user정보가 사라져 삭제가 안됌
>         #먼저 탈퇴 후 로그아웃해주자
>         auth_logout(request)
>     return ~
> ```



### 회원정보 수정

#### ~~UserChangeForm~~ CustomUserChangeForm

> ```python
> #CustomUserChangeForm을 설정한다면 기존 UserChangeForm은 사용할 필요 없다
> #from django.contrib.auth.forms import UserChangeForm
> from .forms import CustomUserChangeForm
> 
> def update(request):
>     if request.method == "POST" :
>         form = CustomUserChangeForm(request.POST, instance=request.user)
>         if form.is_valid():
>             form.save()
>             return ~
>     else:
>         form = CustomUserChangeForm(instance=request.user)
> ```

사용자 정보 및 권한을 변경하기 위해 admin 인터페이스에서 사용되는 __ModelForm__

- admin 인터페이스에 적용되는 ModelForm이기 때문에 그대로 사용하면 일반 사용자가 봐선 안되는 옵션들도 같이 나타난다.

- ##### 그러므로 forms.py에서 나타낼 fields들을 조정해주어야한다

  ```python
  #forms.py
  from django import forms
  from django.contrib.auth.forms import UserChangeForm
  from django.contrib.auth import get_user_model
  
  #UserChangeForm 상속받음
  class CustomUserChangeForm(UserChangeForm):
      class Meta:
          #유저 모델을 가져와야함
          #get_user_model은 현 프로젝트에서 사용하는 유저클래스를 리턴해주는 함수
          model = get_user_model()
          #fields는 DB에서 확인하자
          fields = ('email', 'first_name', 'last_name')
  ```



### 비밀번호 변경

장고에서는 회원정보 수정에서 비밀번호 변경을 할 수 없고, 따로 페이지를 만들어서 해야한다.

회원정보 수정에서 비밀번호 변경 url을 기본값으로 'accounts/password'로 가지고 있다.

#### PasswordChangeForm

- ModelForm이 아니라 Form이며 `user을 첫번째 인자`로 가진다.

> ```python
> from django.contrib.auth.forms import PasswordChangeForm
> from django.contrib.auth import update_session_auth_hash
> 
> def change_password(request):
>     if request.method == 'POST':
>         form = PasswordChangeForm(request.user, request.POST)
>         if form.is_valid():
>             user = form.save()
>             ################
>             update_session_auth_hash(request, user)
>             ################
>             return ~
>     else :
>         form = PasswordChangeForm(request.user)
> ```

- ##### 암호 변경 시 세션 무효화 방지

  - 비밀번호를 변경하면 세션 값이 완전히 달라지기 때문에 로그아웃 상태로 돌아간다.
  - `update_session_auth_hash(request, user)`
    - 현재 요청과 새 session hash가 파생될 업데이트 된 사용자 객체를 가져오고, session hash를 적절하게 업데이트함



## Foreign Key (Comment)

다른 테이블의 행을 `식별 할 수 있는` 키 => 꼭 PK가 아니더라도 Unique여도 가능 (참조 무결성)

### ForeignKey

- 2개의 위치 인자 필요

  1. 참조하는 Model class

  2. on_delete

     - FK가 `참조하는 객체`가 사라졌을 때 FK를 `가진 객체`를 어떻게 할지 정의

     - 데이터 무결성을 위해 매우 중요

       데이터 무결성 : 데이터의 정확성과 일관성을 유지, 보증하는 것
       무결성 제한의 유형

        1. 개체 무결성(Entity integrity)

           모든 테이블은 PK를 가져야하며, 고유한 값이고 빈 값은 허용하지 않음

        2. 참조 무결성(Referential inegrity)

           FK값이 DB의 특정 테이블의 PK값을 참조하는 것

        3. 도메인 무결성(Domain integrity)

           정의된 범위에서 DB의 모든 칼럼들이 선언되도록 규정

     - 가능한 값

       * CASCADE, PORTECT, SET_NULL, SET_DEFAULT, SET(), DO_NOTHING ...

       

- migrate 작업 시 필드 이름에 _id를 추가하여 열 이름을 만듬 (name -> name_id)

- [참고] 재귀관계(자신과 1:N) 

  - ```python 
    models.ForeignKey('self', on_delete=models.CASCADE)
    ```



### Comment Model 만들기

> ```python
> #models.py
> class Comment(models.Model):
>     #1:N관계에서는 속성이름을 단수로 사용
>     article = models.ForeignKey(Article, on_delete=models.CASCADE)
>     content = ~
> ```

#### 데이터 삽입

pk값 자체를 넣어주면 _id로 넣어야하고

comment.article_id = article.pk

객체를 넣어주려면 그냥 넣어주면 된다

comment.article = article



### 1:N 관계

- __역참조(comment_set)__

  - 1에서 N을 찾는 것

  - article.comment_set을 사용하여 가져온다

    - article.comment_set.all() : 모두 가져옴

  - 만약 comment_set이라는 이름이 마음에 안들면

    - ```python
      article=models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
      ```

      related_name으로 변경가능하다.

      ex) article.comments.all()

- 참조
  - N에서 1을 찾는 것
  - comment.article로 사용 가능



### Comment Form

현재 comment 모델에서 fields는 article(FK), content로 이루어져있고, 이를 폼으로 구현하면 article을 선택하는 드랍다운이 표시된다. 이것은 우리가 보는 게시글에 대해 댓글을 작성하는 것이므로 선택하는 옵션이 존재하지 않아야하므로 form에서 fields를 조정해주어야한다.

### Comment Create

Form에서 article(FK) 값을 제외시켰기 때문에 댓글 작성시 article(FK)값이 넘어오지 않아서 에러가 발생한다. 때문에 추가적인 데이터 삽입을 하기 위해 save함수의 commit인자를 False로 한다.

> ```python
> from .forms import CommentForm
> 
> def comments_create(request, pk):
>     article = Article.objects.get(pk=pk)
>     comment_form = CommentForm(request.POST)
>     if comment_form.is_valid():
>         ######################
>         comment_form.save(commit=False)
>         comment.article = article #또는 comment.article_id = pk 가능
>         comment.save()
>         ######################
>     return ~
> ```

### Comment Delete

댓글 삭제시 detail페이지로 redirect하려면 article.pk가 필요하기 때문에

삭제 URL은 variable routing을 2번 사용해주는 것이 필요하다.

```python
#urls.py
path('comments/<int:article_pk>/delete/<int:comment_pk>/', views_Comment_delete, name='comment_delete')
```



## Customizing Authentication in Django

### User 모델 대체하기

~~순서 못외울때는 Customizing Authentication in Django 공식문서 참고~~

Django의 내장 User 모델이 제공하는 인증 요구사항이 적절하지 않을 때
Django는 AUTH_USER_MODEL값을 제공하여 재정의(Override)를 가능하게 함

프로젝트의 __첫 migrate 실행 전__ 커스터마이즈를 진행해야한다.

#### AUTH_USER_MODEL

기본값 : auth.User -> auth앱의 User모델

accounts앱의 models에 User라는 클래스가 정의되어있어야한다.

다만 나는 결국 쓸것이기 때문에 setting부터 작성하기로 했다.

> ```python
> #settings.py
> AUTH_USER_MODEL = 'accounts.User'
> ```

#### accounts/models

처음 pass로 지정해주고 프로젝트를 진행하면서 칼럼들을 추가하면서 진행 가능하다.

> ```python
> #account/models.py
> from django.db import models
> from django.contrib.auth.models import AbstractUser
> 
> class User(AbstractUser):
>     pass
> ```

#### accounts/admin

커스텀한 유저모델은 admin사이트에 자동으로 뜨지 않기 때문에 추가해주어야한다.

> ```python
> #account/admin.py
> from django.contrib import admin
> from django.contrib.auth.admin import UserAdmin
> from .models import User
> 
> admin.site.register(User, UserAdmin)
> ```



### UserCreationForm & UserChangeForm

위 두가지는 auth_User모델을 기본값으로 참조하고 있기 때문에, 커스터마이즈 User모델을 사용할 경우 에러가 발생한다. 해결하기 위해 참조하는 모델값을 커스텀 User모델로 대체해준다.

##### UserChangeForm은 이전에 이미 form형태를 변경하였기 때문에 상관 없다.

UserCreationForm을 변경해보자

> ```python
> #accounts/forms.py
> from django.contrib.auth.forms import UserCreationForm
> ##################################################
> from django.contrib.auth import get_user_model
> ##################################################
> 
> class CustomUserCreationForm(UserCreationForm):
>     
>     class Meta(UserCreationForm.Meta):
>         model = get_user_model()
>         fields = UserCreationForm.Meta.fields + ('email',)
> ```

##### get_user_model()

현재 프로젝트에서 활성화 된 User모델을 가져온다.

지금 활성화된 User모델은 settings.py에 지정된 accounts.User을 참조하도록 한다.



## User-Article (1:N)

`User-Comment (1:N)관계도 동일하게 진행한다.`

### User모델 참조하기

1. settings.AUTH_USER_MODEL
   - User 모델에 대한 외래키 또는 다대다 관계를 정의 할 때 사용
   - __models.py에서__ User모델을 참조할 때 사용
   - return 값 = str
2. get_user_model()
   - 현재 활성화된 User모델 반환
   - __models.py가 아닌 다른 모든 곳__에서 유저 모델을 참조할 때 사용
   - return 값 = object

##### 구분되는 이유

장고에서 app이 실행되는 순서때문에 model이 이미 실행되지 않았는데 앱에서 get_user_model을 가져오면 에러가 뜨기 때문.



### aritcle 모델 및 from 수정

> ```python
> #article/models.py
> from django.conf import settings
> 
> class Article(models.Model):
>     ###############################################
>     user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
>     ###############################################
>     title ~
>     content ~
> ```

> ```python
> #article/forms.py
> class ArticleForm(forms.ModelForm):
>     
>     class Meta:
>         model = Article
>         #####################
>         exclude = ('user')
>         #####################
> ```

> ```python
> #article/views.py
> def create(request):
>     if request.method == 'POST':
>         ~
>         if form.is_valid():
>             ###################################
>             article = form.save(commit=False)
>             article.user = request.user
>             article.save()
>             ###################################
>             ~
> ```



### Delete, Update

작성자와 요청자가 같을때만 가능하도록 한다

> ```python
> #article/views.py
> def delete(request, pk):
>     #########################
>     if request.user == article.user:
>         article.delete()
>     #########################    
> ```





## 느낀점 

생각보다 의사소통하는 것은 개발자에게 중요한 것 같다.

의외로 혼자 모를때 마다 흘끗하면서 코드 보는 것 보다는 네비게이터가 말하는데로 코드를 듣고 짜면

더 이해가 잘되는 느낌이다.



## 의문점

1. 작성된 모델들은 왜 admin.py에 admin.site.register을 작성해야하는가?
   - 아마도 admin페이지에서 표시하기 위해서?
