# Java Script

## DOM(Document Object Model)

>  문서(HTML 조작)

- HTML, XML과 같은 문서를 다루기 위한 프로그래밍 인터페이스
- 문서를 구조화하고, 구조화된 구성요소를 하나의 객체로 취급하여 다루는 __논리적 트리 모델__
- 문서가 객체(object)로 구조화되어 있으며 key로 접근 가능 (__Key & Value__)
- 주요 객체
  - `window` : DOM을 표현하는 창(`브라우저 탭`), `최상위 객체`(작성시 생략 가능)
  - document : 페이지 컨텐츠의 Entry Point 역할을 하며, <head>, <body> 같은 요소들을 포함
  - navigator, location, history, screen

### DOM 조작

- DOM 조작 순서
  1. 선택
  2. 변경
- DOM 관련 객체의 상속 구조
  - EventTarget : Event Listener를 가질 수 있는 객체가 구현하는 DOM 인터페이스
  - Node : 여러 가지 DOM 타입들이 상속하는 인터페이스
  - Element / Document
    - Element : document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
      부모인 Node와 그 부모인 EventTarget의 속성을 상속
    - Document : 브라우저가 불러온 웹페이지를 나타냄
      DOM 트리의 진입점 역할을 수행
  - HTML Element
    - 모든 종류의 HTML 요소
    - 부모 Element의 속성 상속

### DOM - 선택

- document.querySelector(selector)
  - 제공한 선택자와 일치하는 element __하나__ 선택
  - 제공한 CSS selector를 만족하는 __첫 번째 element 객체를 반환__ (없다면 null반환)
- document.querySelectorAll(selector)
  - 제공한 선택자와 일치하는 여러 element를 선택
  - 지정된 셀렉터에 일치하는 NodeList를 반환
    - NodeList : index로만 각 항목에 접근 가능하다(list와 비슷함)
      그렇기 때문에 forEach라는 메서드 사용 가능
- ~~그 외~~ -> 잘 사용하지 않음
  - getElementByID(id)
  - getElementsByTagName(name)
  - getElementsByClassName(names)

#### selecter만 사용하는 이유

> 선택자 모두 사용 가능하고, 더 구체적이고 유연하게 선택 가능하기 때문
>
> ```js
> const h1 = document.querSelector('h1')
> const id = document.querySelector('#id')
> const clas = document.querySelectorAll('.class')
> ```

### DOM - 변경

- document.createElement()

  - 작성한 태그 명의 HTML 요소를 생성하여 반환

- Element.append()

  > ```js
  > const ulTag = document.querySelector('ul')
  > const new1 = document.createElement('li')
  > new.innerText = '리스트1'
  > 
  > ulTag.append(new1,)
  > ```

  - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
  - 여러개의 Node 객체, DOMString을 추가할 수 있음

- Node.appendChild()

  > ```js
  > const ulTag = document.querySelector('ul')
  > const new1 = document.createElement('li')
  > new.innerText = '리스트1'
  > 
  > ulTag.appendChild(new1)
  > ```

  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입
    (Node만 추가 가능 -> 마크업(MarkUp)적인 요소만 추가 가능하다는 뜻)
  - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동

- Node.innerText

  - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현(해당 요소 내부의 raw text)

```js
li1.innerText = '<strong>TEXT</strong>'
li2.innerHTML = '<strong>TEXT</strong>'
//<storng>TEXT</strong>
//TEXT - 굵게 나옴
```

- ~~Element.innerHTML~~

  - 요소(element) 내에 포함된 HTML 마크업을 반환
  - XSS 공격에 취약해서 사용 잘 안함

- ChildNode.remove()

  - Node가 속한 트리에서 해당 Node를 제거

- Node.removeChild()

  > ```js
  > const p = document.querySelector('ul')
  > const c = document.querySelector('ul > li')
  > const r = p.removeChild(c)
  > //r에는 p에서 제거된 c 값이 담겨있음
  > ```

  - 자식 Node를 제거하고 제거된 Node를 반환
  - Node는 인자로 들어가는 자식Node의 부모Node에 사용

- Element.setAttribute(name, value)

  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성 추가
  - Element.classList.add()를 통해 추가__만__ 해줄 수 도 있다

- Element.getAttribute(attributeName)

  > ```js
  > const header = document.query.Selector('#id')
  > header.getAttribute('class')
  > ```

  - 해당 요소의 지정된 값(문자열)을 반환
  - 인자(attributeName)는 값을 얻고자 하는 속성의 이름

- Key값을 통해 접근도 가능하다

  - classList 같은것도 key값을 통해 접근하는 방식이다
  - header.style.cursor = 'pointer' 같은 방식으로 수정 또는 조회 가능



## BOM(Browser Object Model)

> navigator, screen, location, frames, history, XHR 조작

- 자바 스크립트가 브라우저와 소통하기 위한 모델
- 브라우저의 창이나 프레임을 추상화해서 프로그래밍적으로 제어할 수 있도록 제공하는 수단
  - 버튼, url 입력창, 타이틀 바 등 브라우저 윈도우 및 웹페이지 일부분을 제어 가능
- window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭

## JavaScript Core(ECMAScript)

> 브라우저(BOM & DOM)을 조작하기 위한 명령어 약속(언어)

- Data Structure(Object, Array), Conditional Expression, Iteration 조작

### 식별자 정의와 특징

- 식별자는 반드시 문자, 달러($) 또는 밑줄(_)로 시작
- 대소문자를 구분하며, 클래스명 외에는 모두 소문자로 시작

- 예약어 사용 불가능
  - ex) for, if, function
- 카멜 케이스 (camelCase)
  - 변수, 객체, 함수에 사용
- 파스칼 케이스 (PascalCase)
  - 클래스, 생성자에 사용
- 대문자 스네이크 케이스 (SNAKE_CASE)
  - 상수에 사용
    - 상수 : 개발자의 의도와 상관없이 변경될 가능성이 없는 값을 의미

### 변수

#### ~~var~~

> 레거시 코드에서 사용되고 있기 때문에 삭제는 못하고 있는 상황

- 재선언, 재할당 모두 가능
- ES6 이전에 변수를 선언할 때 사용되던 키워드
- `호이스팅`되는 특성으로 인해 문제 발생하므로 `사용금지`됨
  - 변수를 `선언 이전에` 참조할 수 있는 현상
- 함수 스코프

#### let

- 재할당 할 예정인 변수 선언 시 사용
- __재할당 가능__
- `재선언` 불가능
- 블록 스코프

#### const

> 선언할 때 할당을 무조건 해주어야함
>
> 아니면 재선언이 불가능하여 값을 기입하지 못한다

- 재할당 할 예쩡이 없는 변수 선언 시 사용
- __재할당 불가능__
- `재선언` 불가능
- 블록 스코프

>__선언과 할당__
>
>선언 : 변수를 생성하는 행위
>
>```js 
>let number
>const people
>```
>
>할당 : 선언된 변수에 값을 저장하는 행위 === `=`을 사용하는 행위
>
>```js
>number = 0
>//const는 선언시 할당 해야한다
>const people = 1
>```

> __블록 스코프__
>
> 중괄호 내부를 가르킴
>
> 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능



## 데이터 타입

> 원시 타입 (Primitive type)
>
> 참조 타입 (Reference type)

### 원시 타입

- 객체(object)가 아닌 기본 타입

- 변수에 해당 타입의 실제 값을 담음

- 다른 변수에 복사할 때 `실제 값`이 복사됨

  - ```js
    let message = "hi"
    let greeting = message
    message = 'hello'
    console.log(greeting)
    //'hi'가 출력된다
    ```

- 종류

  - Number

    - 정수, 실수 구분 없는 하나의 숫자 타입
    - NaN : 계산 불가능한 경우 반환되는 값
    - NaN, Infinity, -Infinity도 숫자타입임
    - ex) 'angle'/1004 = > NaN

  - String

    - 템플릿 리터럴 사용 가능

    - ```js
      `${expression}`
      ```

  - undefined

    - 값이 없음을 나타내는 데이터 타입
    - 선언 후 직접 값 할당을 하지 않으면 undifined가 할당됌

  - null

    - 값이 없음을 __의도적으로 표현__할 때
    - 타입은 원시타입에 포함되지만, `typeof연산자의 결과는 객체(object)로 표현됨`

  - Boolean

    - 자동 형변환
      1. undefined = 항상 거짓
      2. null = 항상 거짓
      3. number = 0, -0, NaN 거짓 | 나머지 모든 경우 참
      4. string = 빈 문자열 거짓 | 나머지 모든 경우 참
      5. object = 항상 참

### 참조 타입

- 객체(object)타입의 자료형

- 변수에 해당 객체의 `참조 주소값`이 담김

- 다른 변수에 복사할 때 `참조 주소값`이 복사됨

  - ```js
    let message = ["hi"]
    let greeting = message
    message[0] = 'hello'
    console.log(greeting)
    //'hello'가 출력된다
    ```



## For 문

### for

> ```js
> for (initialization; condition; expression) {
>     // do something
> }
> // 이 방식에서는 i는 let으로만 사용해야한다
> for (let i = 0; i < length(something); i++){
> }
> ```

- 세미콜론으로 구분되는 세 부분으로 구성
- initialization : 반복문 최초 진입 시 1회만 실행되는 부분
  - 주로 반복하면서 변화되는 변수 지정할 때 사용
- condition : 매 반복 시행 __전__ 평가되는 부분
- expression : 매 반복 시행 __이후__ 평가되는 부분

### for ... in ...

> ```js
> for (variable in object){
>     // do something
> }
> //이건 object
> //파이썬에서 dict와 유사
> const capitals = {
>     korea : 'seoul',
>     france : 'paris',
>     USA : 'washington D.C.'
> }
> // 이 방식에서는 const변수로도 가능하다
> for (const sudo in capitals){
>     console.log(capital) // korea, france, USA
> }
> ```

- 객체(object)의 `속성(key)`들을 순회할 때 사용
- 배열도 순회 가능하지만 권장하지는 않음
  - 배열에 사용할 경우, 배열의 값(value)를 출력하는 것이 아닌 인덱스(key)를 출력한다

### for ... of ...

> ```js
> for (variable of iterables){
>     // do something
> }
> //이건 array
> const fruits = ['A', 'B', 'C']
> for (const X of fruits){
>     console.log(X) // A, B, c
> }
> ```

- __반복 가능한(iterable)__ 객체를 순회하며 값을 꺼낼 때 사용
- for in과 다르게 객체의 값(value)들을 가져온다

### for문 안의 변수 const, let 사용 차이

- 기본 for문에는 i 값 자체가 계속 재할당이 되면서 조건문을 통과해야하므로
  i += 1이라는 재할당이 필수적이므로 let만 사용하여야한다.

- for of / for in의 경우, 참조 가능한 object 형태의 데이터들에게서 그 주소값들을 받아와 반복문을 실행하며, 한번 반복문이 끝나면 블록스코프의 성질에 의해 변수가 삭제된다.

-  ##### 그렇기 때문에 반복문을 한번씩 돌 때마다 변수가 새로이 재선언되는 것이다.

- 다만 for of나 for in 문에서도 `변수가 재할당이 필요한 경우`에는 let으로 선언해주어야한다.



## 함수

- 함수 선언식

  -  호이스팅이 발생한다.

  ```js
  function name(args){
  }
  function add(num1, num2){
      return num1+num2
  }
  add(1,2)
  ```

- 함수 표현식

  - 익명함수으로 사용 가능해진다.

  ```js
  const name = function (args){
  }
  const add = function (num1, num2){
      return num1, num2
  }
  add(1,2)
  ```

- 매개변수와 인자의 개수 불일치 허용

### Rest Parameter & Spread Operator

- rest parameter(...)를 사용하면 함수가 정해지지 않은 수의 매개변수를 배열로 받음
- rest parameter로 처리하였을 때 인자가 넘어오지 않는다면, 빈 배열로 처리
- spread operator(...)를 사용하면 배열 인자를 전개하여 전달 가능
- python의 *와 똑같이 작동한다
- packing unpacking을 한다고 보면 됌

### Arrow Function

> ```js
> const arrow = function (name) {
>     return 'hello'
> }
> 
> const arrow = name => 'hello'
> ```

- 함수를 비교적 간결하게 정의할 수 있는 문법
- function 키워드 생략 가능
- 함수의 매개변수가 단 하나 뿐이라면, 괄호 () 생략 가능
- 함수 몸통이 표현식 하나라면 괄호 {}와 return 생략 가능



## Method

### 문자열

> 문자열은 변경 불가능하므로 교체된 __임시값__을 반환한다

- includes : 특정 문자열의 존재여부를 참/거짓으로 반환
  - string.includes(value)
- split : 문자열을 토큰 기준으로 나눈 배열 반환
  - string.split(value)
  - value가 없을 경우 기존 문자열을 그대로 배열에 담아 반환
  - value가 '' 일 경우 하나하나의 문자로 나눈 배열 반환
- replace : 해당 문자열을 대상 문자열로 교체하여 반환
  - string.replace(from, to)
  - replaceAll : 해당 문자열을 모두 대상 문자열로 교체하여 반환
- trim : 문자열의 좌우 공백 제거하여 반환
  - string.trim()
  - trimStart : 왼쪽 공백만 제거
  - trimEnd : 오른쪽 공백만 제거

### 배열(Arrays)

> 키와 속성들을 담고 있는 참조 타입의 객체(object)
>
> 순서를 보장함
>
> 대괄호[]를 이용하여 생성
>
> 길이는 array.length로 접근가능

- reverse : 원본 배열의 요소들의 순서를 반대로 정렬

- push&pop : 배열의 가장 뒤에 요소를 추가/제거

- unshift&shift : 배열의 가장 앞에 요소를 추가/제거

- includes : 배열에 특정 값이 존재하는지 판별 후 참/거짓 반환

- indexOf : 배열에 특정 값이 존재하는지 판별 후 인덱스 반환

  - 가장 첫번째로 찾은 요소의 인덱스 반환
  - 없으면 -1 반환

- join : 배열의 모든 요소를 구분자를 이용하여 연결

  - array.join([separtator])
  - 구분자 생략 시 쉼표로 연결 후 반환

- 배열 내부에서 배열 전개

  - spread operator(...) 사용

  - ```js
    const array = [1,2,3]
    const newarray = [0,...array, 4]
    console.log(newarray) //[0,1,2,3,4]
    ```

#### CallBack 함수를 받는 것이 특징인 메소드들

> 콜백 함수는 3가지 매개변수로 구성
>
> array.forEach((element, index, array) => {})
>
> ​	element : 배열의 요소
>
> ​	index : 배열 요소의 인덱스
>
> ​	array : 배열 자체

- forEach : 배열의 각 요소에 대해 콜백 함수를 한번씩 실행

  ```js
  const fruits = ['A','B','C','D']
  fruits.forEach((fruit, index) => {
      console.log(fruit, index)
      // A 0
      // B 1
      //~~
  })
  ```

  - return 값이 없는 메소드

- map : 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환

  ```js
  const numbers = [1,2,3,4,5]
  const doubleNums = numbers.map((num) => {
      return num*2
  })
  console.log(doubleNums) //[2,4,6,8,10]
  ```

- filter : 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환

  ```js
  const numbers = [1,2,3,4,5]
  const oddNums = numbers.filter((num, index) => {
      return num%2
  })
  console.log(oddNums) // [1, 3, 5]
  ```

- reduce : 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환

  ```js
  array.reduce((acc, element, index, array) => { 
  }, initialValue)
  
  const numbers = [1,2,3,4,5]
  const result = numbers.reduce((acc, num) => {
      return acc + num
  }, 0)
  console.log(result) // 15
  
  const result = numbers.reduce((acc, num) => {
      return acc + num
  }, '')
  console.log(result) // '12345'
  ```

  - reduce의 콜백함수는 acc 값이 더 붙어있다
  - acc : 이전 callback 함수의 반환 값이 누적되는 변수
  - initialValue(Optional) : 최초 callback 함수 호출시 acc에 할당되는 값
    default는 배열의 첫째 값
    - 빈 배열일 경우 intialValue값이 할당 안되어있다면 에러 발생

- find : 콜백 함수의 반환 값이 참이면 첫번째 해당 요소를 반환
  - 없으면 undefined 반환
- some : 배열의 요소 중 하나라도 판별 함수를 통과하면 참을 반환
  - 빈 배열은 항상 거짓 반환
- every : 배열의 모든 요소가 판별 함수를 통과하면 참을 반환
  - 빈 배열은 항상 참 반환

### 객체(Objects)

> 객체는 속성의 집합이며, 중괄호 {} 내부에 key와 value 쌍으로 표현
>
> key는 문자열만 가능
>
> 객체 요소 접근시 . 또는 []로 가능 (다만, key이름에 띄어쓰기가 있다면 대괄호 접근만 가능)

- JSON : js의 객체와 유사하나 실제로는 `문자열 타입`

  - JSON.parse( json ) : json => 자바스크립트 객체

  - JSON.stringify( object ) : 자바스크립트 객체 => json

    ```js
    const jsonData = JSON.stringify({
        coffee : 'americano',
        icecream: 'cookie'
    })
    console.log(typeof jsonData) //string
    
    const parsedData = JSON.parse(jsonData)
    console.log(typeof parseData) // object
    ```

#### 객체와 메소드

```js
const me = {
    first : 'John',
    last : 'Doe',
    //이 아래의 this는 메소드 안의 this가 아니기 때문에 NaN 반환
    full : this.first + this.last
    //메소드 안의 this는 객체를 의미하기 때문에 me.first+me.last를 반환함
    getFullName : funciton (){
        return this.first + this.last
    }
}
```

- 메소드는 객체의 속성이 참조하는 함수

#### 속성명 축약

```js
const books = ['A', 'B']
const magazines = ['C','D']
const bookshop ={
    books,
    magazines,
}
console.log(bookshop)
/*
{
	books : ['A', 'B'],
	magazines : ['C','D']
}
*/
```

- key와 할당하는 변수의 이름이 같다면 축약 가능

#### 메소드명 축약

- function 키워드 생략 가능

#### 계산된 속성

```js
const key = 'regions'
const value = ['a','b','c','d','e']
const ssafy = {
    [key] : value,
}
console.log(ssafy) // {regions:Array(5)}
console.log(ssafy.regions) //["a","b","c","d","e"]
```

- 객체를 정의할 때 key의 이름을 표현식을 이용하여 동적으로 생성 가능

#### 구조 분해 할당

```js
const userInfo {
    name : 'a',
    ID : '1234',
    phone : '0101',
    email : 'sdaf@com'
}
const name = userInfo.name
const {name} = userInfo
const ID = userInfo.ID
const {ID} = userInfo
```

- 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법

#### Spread operator

- 객체 내부에서 객체 전개 가능



## this

- class  내부의 생성자 함수
  - this는 생성되는 객체를 가리킴
- 메소드(객체`.메소드명() 으로 호출 가능`한 함수)
  - this는 해당 메소드가 소속된 객체를 가리킴
- 그외에는 모두 window를 가리킴

```js
const obj = {
    pi : 3.14,
    radiuses : [1,2,3,4,5],
    printArea : function (){
        this.radiuses.forEach(function (r) {
            console.log(this.pi *r*r)
        }.bind(this)) //여기서 forEach의 콜백함수의 경우 메소드가 아니므로 콜백함수에 담긴 this는 window를 가리키게 된다. 이를 방지하기 위해 forEach의 콜백함수뒤에 .bind(this)를 달아주어야한다.
    },
}
const obj = {
    pi : 3.14,
    radiuses : [1,2,3,4,5],
    printArea : function (){
        this.radiuses.forEach((r) => {
            console.log(this.pi *r*r)
        })
    },
}
```



## lodash

lodash cdn을 가져와 사용가능하며

언더바를 식별자로 사용하여 몇가지 기능들을 사용할 수 있게 해준다.

```js
_.shuffle()
_.sample()
_.range()
등등
```



## Event

> 네트워크 활동이나 사용자와의 상호작용 같은 사건의 발생을 알리기 위한 객체
>
> __대상(a)에 특정 이벤트(b)가 발생`하면`, 할 일(c)을 등록`한다`__
>
> a.addEventListener(b, c)
>
> ```js
> const btn = document.querySelector('button')
> btn.addEventListener('click', function (event) {
>     alert('버튼이 클릭되었습니다.')
> })
> 
> const onColorInput = function (event){
>     const userInput = event.target.value
>  const h2Tage = document.querySelector('h2')
>     h2Tage.style.color = userInput
> }
> colorInput.addEventListener('input', onColorInput)
> ```

- target.addEventListener(tyepe, listener[, options])
  - 지정한 이벤트가 대상에 전달될 때마다 `호출할 함수`를 설정
  - 이벤트를 지원하는 모든 객체(Element, Document, Window 등)를 대상으로 지정 가능
  - type : 반응할 이벤트 유형(대소문자 구분 문자열로 입력)
  - listener
    - 지정된 타입의 이벤트가 발생했을 때 알림을 받는 객체
      EventListener 인터페이스 혹은 JS function 객체(`콜백 함수`)여야 함
- event 객체는 addEventListener함수가 보내주는 객체이다.
  사용하지 않는다면 안받아도 상관없다

### Event 취소

> __event.preventDefault()__

- 현재 이벤트의 기본 동작을 중단
  - ex) a태그의 클릭 시 링크로 이동 / form 태그의 데이터 전송 같은 것을 막음
- 이벤트를 취소할 수 있는 경우, 이벤트의 전파를 막지 않고 그 이벤트를 취소함

#### Event 취소가 불가능한 경우

- event의 속성에서 cancelable 값이 True인 경우에만 기본 내장 event취소가 가능하다
- scroll 같은 경우에는 cancelable 값이 false이므로 event.preventDefault를 설정해주어도 취소 불가능 하다

### Event 리셋

> event.target.reset()

### EventBubbling

> 하위요소에서 발생한 이벤트가 상위요소까지 전파되는 것

- 버블링을 막기 위해서 event.stopPropagation() 사용