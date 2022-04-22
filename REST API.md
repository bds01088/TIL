# REST API

> #### 알면 좋은 꿀팁
>
> serializer 정의할 때 depth 옵션을 정해주면 참조하는 대상에서 참조되는 대상의 정보를 볼 수 있다.
>
> 참조되는 대상 = nested relationships
>
> 참조하는 대상 = depth

## HTTP (HyperText Transfer Protocol)

- 웹에서 이루어지는 모든 데이터 교환의 기초
  - 요청(request)
  - 응답(response)

- 기본 특성
  - Stateless
  - Connectionless

### HTTP response status codes

1. Infromation responses(1xx)
2. Successful responses(2xx)
3. Redirection messages(3xx)
4. Client error responses(4xx)
5. Server error responses(5xx)



### URL ,URN

#### URL(Uniform Resource Locator)

- 통합 자원 위치
- 네트워크 상에 자원이 어디 있는지 알려주기 위한 약속

#### URN(Uniform Resource Name)

- 통합 자원 이름
- URL과 달리 자원의 위치에 영향을 받지 않는 유일한 이름 역할을 함



### URI (Uniform Resource Identifier)

- 통합 자원 식별자
- 인터넷의 자원을 식별하는 유일한 주소
- 하위 개념
  - URL, URN
- URN의 사용 비중이 매우 낮기 때문에 일반적으로 URL은 URI와 같은 의미로 쓰이기도 함

#### URI의 구조

- Schema (Protocol)
  - 브라우저가 사용해야하는 프로토코ㅠㄹ
  - ex) http(s), data, file, ftp, mailto
- Host (Domain name)
  - 요청을 받는 웹 서버 이름
  - IP address를 직접 사용할 수도 있지만 사용하진 않음
    - google의 IP address : 142.251.42.142
- Port
  - 웹 서버 상의 리소스에 접근하는데 사용되는 기술적인 문(gate)
  - HTTP 프로토콜의 표준 포트
    - HTTP 80
    - HTTPS 443
- Path
  - 웹 서버상의 리소스 경로
- Query (Identifier)
  - Query String Parameters
  - 웹 서버에 제공되는 추가적인 매개 변수
  - &로 구분되는 key-value 목록
- Fragment (Anchor)
  - 자원 안에서의 북마크의 한 종류를 나타냄
  - 브라우저의 해당 문서의 일부분을 보여주기 위한 방법
  - 브라우저에게 알려주는 요소이기 때문에 부분식별자(fragment identifier)라고 부르며
    #뒤의 부분은 요청이 서버에 보내지지 않음



## RESTful API

### API (Application Programming Interface)

> __프로그래밍 언어가 제공하는 기능을 수행할 수 있게 만든 인터페이스__



### REST (REpresentation State Transefer)

> API Server를 개발하기 위한 일종의 소프트웨어 설계 방법론
>
> REST 원리를 따르는 시스템을 RESTful 이란 용어로 지칭함

- REST의 자원과 주소의 지정 방법
  1. 자원 : URI
  2. 행위 : HTTP Method
  3. 표현 : JSON 데이터

- REST의 핵심 규칙
  1. '정보'는 URI로 표현
  2. 자원에 대한 '행위' 는 HTTP Method로 표현



## Response

여태까지는 HTML파일을 넘겨주었지만 이제는 REST로 제작하기 때문에 Json으로 제공한다

### Json Response

> ```python
> from django.http.response import JsonResponse
> def article_json_1(request):
>     articles = Article.objects.all()
>     articles_json = []
>     for article in articles :
>         article_json.append(
>             {
>                 'id':article.pk,
>                 'title':article.title,
>                 'content':article.content,
>                 ~~
>             }
>         )
>     return JsonResponse(articles_json, safe=False)
> ```

- Content-Type entitiy hearder
  - 데이터의 media type을 나타내기 위해 사용됨
- JsonResponse objects
  - JSON-encoded response를 만드는 HttpResponse의 서브 클래스
  - "safe" parameter
    - True(기본값)
    - dict 이외의 객체를 `직렬화(Serialization)`하려면 False로 설정



### Serialization (직렬화)

> ```python
> from django.core import serializers
> from django.http.response import HttpResponse
> def article_json_2(request):
>     articles = Article.objects.all()
>     data = serializers.serialize('json', articles)
>     return HttpResponse(data, content_type='application/json')
> ```

- 데이터 구조나 객체 상태를 동일하거나 다른 컴퓨터 환경에 저장하고,
  나중에 재구성할 수 있는 포맷으로 변환하는 과정

- Serializers in Django
  - Queryset 및 Model Instance와 같은 복잡한 데이터를 JSON, XML 등의 유형으로 쉽게 변환 할 수 있는 Python 데이터 타입으로 만들어 줌

- 주어진 모델 정보를 활용하기 때문에 필드를 직접 만들어 줄 필요가 없음



~~이걸 쓸거임~~

### Django REST Framework

> Django REST framework(DRF) 라이브러리를 사용한 JSON 응답
>
> ```python
> from .serializers import ArticleSerializer
> from rest_framework.decorators import api_view
> from rest_framework.response import Response
> @api_view()
> def article_json_3(request):
>     articles = Article.objects.all()
>     serializer = ArticleSerializer(articles, many=True) #many 기본값음 false
>     #many는 단일객체가 아닐때 사용
>     return Response(serializer.data)
> ```
>
> ```python
> #serializers.py
> from rest_framework import serializers
> from .models import Article
> 
> class ArticleSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = Article
>         fields = '__all__'
> ```

#### 설치 과정

```shell
$ pip install djangorestframework
```

```python
# settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

- 브라우저에서 열면 HTML 문서로 넘겨준다.

- 요청으로 열면 JSON 형태로 받을 수 있다.

  - ```python
    #$ pip install request
    import requests
    response = requests.get('http://~~~')
    #print(type(response.json()))
    articles_list = response.json()
    for article in articles_list:
        print(article.get('title'))
    ```

#### Django ModelForm VS DRF Serializer

##### Django 

- Response : HTML
- Model : ModelForm

##### DRF

- Response : JSON
- Model : Serializer



## Single Model

### DRF with Single Model

- 단일 모델의 data를 직렬화하여 JSON으로 변환하는 방법

- API 개발을 위한 핵심 기능을 제공하는 도구 활용
  - DRF built-in form
  - Postman(https://www.postman.com/)
    - 브라우저 대신 사용
    - API 구축, 사용을 위해 도구를 제공하는 API플랫폼

```python
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404
from .serialzers import ArticleListSerializer, ArticleSerializer
from .models import Article

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ARticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        #is_valid에 raise_exception=True 설정하면 밑에 코드 쓸 필요가 없음
    	#return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    
    if request.method == 'GET':
        serializer = ArticleSerializer(article):
            return Response(serializer.data)
    elif request.method == 'DELETE':
        article.delete()
        data = {
            'delete' : f'데이터 {article_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        serializer = ArticleSerializer(article, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
```



## 1:N Relation

```python
from .models import Comment
from .serializer import CommentSerializer

@api_view(['GET'])
def comment_list(request):
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Resopnse(serializer.data)

@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        comment.delete()
        data = {
            'comment' : f'데이터 {comment_pk}번이 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

#urls.py
#path('articles/<int:article_pk>/comments/', views.comment_create)
@api_view(['POST'])
def comment_create(request, article_pk):
    article= get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        #form과는 다름
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
```

### Read Only Field(읽기 전용 필드)

> ```python
> #serializers.py
> class CommentSerializer(serializers.ModelSerializer):
>     class Meta:
>         model = Comment
>         fields = '__all__'
>         read_only_fields = ('articles',)
> ```

- 어떤 게시글에 작성하는 댓글인지에 대한 정보를 form-data로 넘겨주지 않았기 때문에
  직렬화하는 과정에서 article필드가 유효성 검사를 통과못함
- 이때 읽기 전용 필드 설정을 통해 직렬화하지 않고 반환 값에만 해당 필드가 포함되도록 설정한다.



### Serializer 커스텀

- Serializer는 기존 필드를 override하거나 추가 필드를 구성할 수 있음
  1. PrimaryKeyRelatedField
  2. Nested relationships

#### PrimaryKeyRelatedField

- 단순히 comment_pk값(들)만 가져옴

> ```python
> #serializers.py
> class ArticleSerializer(serializers.ModelSerializer):
>     #1:N이라 한 게시글에 여러 댓글을 가져오므로 many=True
>     comment_set = serializers.PrimaryKeyRealtedField(many=True, read_only=True)
>     #추가칼럼이므로 여기서 read_only를 설정
>     #만약 related_name을 수정하고싶다면 위의 칼럼이름 변경하고, 그 이름도 models.py에서 related_name을 똑같이 수정해주면 된다
> ```

#### Nested relationships

- 모델 관계상 `참조된 대상`은 `참조하는 대상`의 표현(응답)에 포함되거나 중첩될 수 있음
- 모델을 가져오는 것으로 결과에는 해당 comment의 모든 정보를 다 가져온다.

> ```python
> #serializers.py
> class CommentSerialier(serializers.ModelSerializer):
>     class Meta:
>         model = Comment
>         fields = '__all__'
>         read_only_fields = ('aritcle',)
> 
> class ArticleSerializer(serializers.ModelSerializer):
>     #1:N이라 한 게시글에 여러 댓글을 가져오므로 many=True
>     comment_set = CommentSerializer(many=True, read_only=True)
>     #클래스 정의가 먼저 되어야지 아래에서 호출이 가능하므로 Nested relationships을 사용하려면 참조된 대상(article)의 정의가 아래쪽에 와야한다.
>     class Meta:
>         model = Article
>         fields = '__all__'
> ```



### 새로운 파생 칼럼 생성

> ```python
> class ArticleSerializer(serializers.ModelSerializer):
>     comment_set = CommentSerializer(many=True, read_only=True)
>     #########################################
>     #article.comment_set.count() 중에서 모델 뒷부분만 적으면 됌
>     comment_count = serializer.IntegerField(source='comment_set.count', read_only=True)
>     #########################################
>     
>     class Meta:
>         model = Article
>         fields = '__all__'
> ```



## Django-seed

### 설치

```shell
$ pip install django-seed
```

```python
#settings.py
INSTALLED_APPS = [
    'articles',
    'rest_framework',
    'django_seed',
    ~~
]
```

### 실행

```shell
$ python manage.py seed AppName --number=20
ex) $ python manage.py seed articles --number=20
#20개 생성
```



## M:N 

```python
#models.py
class Card(models.Model):
    articles = models.ManyToManyField(Article, related_name='cards')
    name = models.CharField(max_length=100)
    
#######################################################################
#serializer의 세분화를 위해 폴더로 만들고 articles, comments, cards를 따로 만들어준다
#serializer.card.py
from ..models import Card
from rest_framework import serializers

class CardSerializer(serializers.ModelSerializer):
    class Meta :
        model = Card
        fields = '__all__'
        
#########################################################
#article에서도 card에 대한 정보를 보고 싶다면
class ArticleSerializer(serializers.ModelSerializer):
	comment_set = CommentSerializer(many=True, read_only=True)
	comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    #다만 참조하는 cardserializer가 모든 필드를 표시한다.
    cards = CardSerializer(many=True, read_only=True)
class Meta:
     model = Article
     fields = '__all__'
```



## Swagger

### drf-yasg 라이브러리

```shell
$pip install drf-yasg
```

```python
#settings.py
INSTALLED_APPS = [
    ~~
    'jango.contrib.staticfiels',
    'drf_yasg',
]

#urls.py
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    ~~~
    ~~~~
    ~~~
    #정규표현식이 아닌 주소
    #path('swagger/', schema_view.with_ui('swagger')),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
   re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   ...
]
```



## Fixtures

> 앱을 처음 설정할 때 미리 준비된 데이터로 데이터베이스를 미리 채우는 것
>
> 원격저장소에는 DB를 올리지않기 때문에 fixtures를 올려 기초 데이터를 공유할 수 있다

- 데이터베이스의 serialized 된 내용을 포함하는 파일 모음
- django가 fixtures파일을 찾는 경로
  - app/fixtures/

### DumpData

> ```shell
> $python manage.py dumpdata [app_label[.ModelName]]
> ```
>
> ```shell
> #--indent 옵션을 주지 않으면 한 줄로 작성됨
> #"auth앱의 user모델 데이터를 indent 4칸(tab)의 user.json 파일로 출력"
> $python manage.py dumpdata --indent 4 auth.user > user.json
> $python manage.py dumpdata --indent 4 articles.article > article.json
> $python manage.py dumpdata --indent 4 articles.comment > comments.json
> $python manage.py dumpdata --indent 4 accounts.user > users.json
> ```



### LoadData

Fixture의 내용을 검색하여 데이터베이스에 로드

> ```shell
> $python manange.py loaddata articles.json comments.json users.json
> ```

- templates와 마찬가지로 설정할 수 있다
  - 2중 폴더를 통해 json의 이름이 같은 파일들을 다루기 위해
  - accounts/fixtures/accounts/user.json 같은 느낌으로 사용하자

#### 주의사항

fixtures는 직접 생성하는 것이 아닌 dumpdata로 생성하는 것임

직접 json만들면 에러가 생길 수 도 있음



## Improve Query

### QuerySets are lazy

- 쿼리셋은 게으르다
- Django는 쿼리셋이 '평가(evaluated)' 될 때까지 실제로 쿼리를 실행하지 않음
- DB에 쿼리를 전달하는 일이 웹 애플리케이션을 느려지게 하는 주범 중 하나이기 때문

### 평가(evaluated)

- 쿼리셋에 해당하는 DB의 레코드들을 실제로 가져오는 것
  - == hit, access, Queries database
- 평가된 모델들은 쿼리셋의 내장 캐시에 저장되며,
  덕분에 우리가 쿼리셋을 다시 순회하더라도 똑같은 쿼리를 DB에 다시 전달하지 않음

#### 캐시 (cache)

- 데이터나 값을 미리 복사해 놓는 임시 장소
- 캐시에 데이터를 미리 복사해놓으면 계산이나 접근시간 없이 빠르게 데이터에 접근 가능

#### 쿼리셋이 평가되는 시점

1. Iteration
   - QuerySet은 반복 가능하며 처음 반복할 때 데이터베이스 쿼리를 실행
   - 매 반복마다 쿼리를 실행하면 느려지기 때문에
   - 평가는 한번만 이루어지며 그 뒤에는 캐시에 저장된 것을 가져와서 반복함
2. bool()
   - bool 컨텍스트에서 QuerySet을 테스트하면 쿼리가 실행

#### 캐시와 쿼리셋

- 각 쿼리셋에는 데이터베이스 액세스를 최소화하는 '캐시'가 포함되어있음
  1. 새로운 쿼리셋이 만들어지면 캐시는 비어있음
  2. 쿼리셋이 처음으로 평가되면 데이터베이스 쿼리가 발생

> 쿼리셋이 캐시되지 않는 경우
>
> 1. 쿼리셋 객체에서 `특정 인덱스`를 반복적으로 가져오면 매번 쿼리 평가함
>
>    ```python
>    queryset = Article.objects.all()
>    print(queryset[5])
>    print(queryset[5])
>    ```
>
> 2. 그러나 쿼리 셋 전체가 이미 평가된 경우 캐시에서 확인할 수 있다
>
>    ```python
>    [article for article in queryset]
>    print(queryset[5])
>    print(queryset[5])
>    ```



### 필요하지 않는 것을 검색하지 않기

- .count()
  - 카운트만 원하는 경우
  - len(queryset) 대신 QuerySet.count() 사용하기
- .exists()
  - 값이 존재하는지 확인할 경우
  - if queryset 대신 QuerySet.exist() 사용
- 다만 항상 붙인다고 해서 최적화가 이루어지는 것은 아니므로
  최적화는 상황에 맞게 사용해야한다.

- Annotate를 자주 써서 쿼리 평가하는 것을 최소화하자



### Annotate

> 한번에 모든 것을 검색하기

1. select_related()
   - 1:1 또는 1:N 참조 관계에서 사용
   - DB에서 INNER JOIN활용
2. prefetch_related()
   - M:N 또는 1:N 역참조 관계에서 사용
   - DB가아닌 Python을 통한 JOIN

#### select_related()

- foreign key & one-to-one 관계에서만 사용 가능

  - 게시글의 작성자 가져오기

    - ```python
      articles = Article.objects.select_related('user')
      ```

#### prefetch_related()

- M:N & 1:N 역참조 관계에 사용 가능

  - 댓글 목록을 모두 출력하기

    - ```python
      articles = Article.objects.prefetch_related('comment_set')
      ```

#### 복합 활용

- 댓글에 더해서 해당 댓글을 작성한 사용자 이름까지 출력 해보기

  - ```django
    {% for comment in article.comment_set.all %}
    	<p>{{comment.user.username}} : {{comment.content}}</p>
    {% endfor %}
    ```

  - ```python
    from django.db.models import Prefetch
    
    articles = Article.objects.prefetch.related(
        Prefetch('comment_set', queryset=Comment.objects.select_related('user'))
    )
    ```
