# REST API

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

