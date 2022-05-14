# Vue.js

### SPA

> Single Page Application (단일 페이지 어플리케이션)

- 현재 페이지를 동적으로 렌더링함으로써 사용자와 소통하는 웹 어플리케이션
- 단일 페이지로 구성되며 서버로부터 최초에만 페이지를 다운로드하고, 이후에는 동적으로 DOM을 구성
- 연속되는 페이지 간의 사용자 경험 향상
- 동작 원리의 일부가 CSR(Client Side Rendering)의 구조를 따름

### CSR

> Client Side Rendering

- 서버에서 화면을 구성하는 SSR 방식과 달리 클라이언트에서 화면을 구성
- 최초 요청 시 HTML, CSS, JS 등 데이터를 제외한 각종 리소스를 응답받고, 이후 클라이언트에서는 필요한 데이터만 요청해 JS로 DOM을 렌더링 하는 방식
- 즉, 처음엔 뼈대만 받고 브라우저에서 동적으로 DOM을 그림

##### 장점

1. 서버와 클라이언트 간 트래픽 감소
2. 사용자 경험 향상

##### 단점

1. SSR에 비해 전체 페이지 최정 렌더링 시점이 느림
2. SEO(검색 엔진 최적화)에 어려움이 있음 (최초 문서에 데이터 마크업이 없기 때문)

### SSR

> Server Side Rendering

- 서버에서 클라이언트에게 보여줄 페이지를 모두 구성하여 전달하는 방식
- JS 웹 프레임워크 이전에 사용되던 전통적인 렌더링 방식

##### 장점 

1. 초기 구동 속도가 빠름
2. SEO(검색 엔진 최적화)에 적합

##### 단점

1. 모든 요청마다 새로운 페이지를 구성하여 전달
   - 사용자 경험 하락, 트래픽 증가

### SSR & CSR

- 두 방식의 차이는 최종 HTML 생성 주체가 누구인가에 따라 결정
- 즉, 실제 브라우저에 그려질 HTML을 서버가 만들면 SSR, 클라이언트(사용자)측에서 만들면 CSR
- Django에서 axios를 활용한 로직의 경우 대부분은 서버에서 완성된 HTML을 제공하지만 => SSR,
  특정요소 (좋아요/팔로우)만 JS(AJAX&DOM조작)를 활용 => CSR



## Concepts of Vue.js

### MVVM Pattern

> 어플리케이션 로직을 UI로부터 분리하기 위해 설계된 디자인 패턴

- 구성요소
  1. Model : {key:value}
  2. View : HTML
  3. ViewModel : Vue

- Model
  - JavaScript Object
  - Vue Instance 내부에서 data라는 이름으로 존재
  - data가 바뀌면 View(DOM)가 반응
- View
  - Vue에서 View는 DOM(HTML)이다
- ViewModel
  - View와 Model 사이에서 Data와 DOM에 관련된 모든 일을 처리

### 선언적 렌더링

```JS
<div id='app1'>
    {{ message}}
    </div>
<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
   		message:'안녕하세요',
	}
})
```

### 조건문

```js
<div id='app1'>
    <p v-if='seen'> 보인다</p> 
    </div>
<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
    	seen : True,
	}
})
```

### 반복문

```js
<div id='app1'>
    <ol>
    	<li v-for="todo in todos">
            {{todo.text}}
        </li>
	</ol>
</div>
<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
		todos : [
        	{text:'가'},
        	{text:'나'},
        	{text:'다'},
        ]
	}
})
```

### 사용자 입력 핸들링

```JS
<div id='app1'>
    <p>{{ message}}</p> 
	<button v-on:click="reverseMessage">거꾸로만들기</button>
	<input v-model="message" type="text">
    </div>
<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
    	message : '안녕하세요'
	},
	methods : {
		reverseMessage : function (){
        	this.message = this.message.split('').reverse().join('')
	    }
    }
})
```

- 반드시 Vue생성에 들어가는 객체의 method는 __에로우함수를 사용하면 안된다!__

- this.message가 작동하는 이유는?

  - Vue객체에서 해당 객체의 내용을 받을 때, 언패키징을 한번해서

    ```js
    // 이 객체가
    {
        el : '#app1'
        data : {
        	message : '안녕하세요'
    	},
    	methods : {
    		reverseMessage : function (){
            	this.message = this.message.split('').reverse().join('')
    	    }
        }
    }
    //이렇게 받아짐
    {
        el : '#app1',
        message : '안녕하세요',
        reverseMessage : function (){
         	this.message = this.message.split('').reverse().join('')
        },
    }
    //이때는 this는 reverseEMssage라는 메소드 안에 포함되어 있으므로 사용가능하다
    //reverseMessage는 콜백함수가 아니다
    ```



## Basic syntax of Vue.js

### Vue instance

- 모든 Vue 앱은 Vue 함수로 새 인스턴스를 만드는 것부터 시작
- Vue 인스턴스를 생성할 때는 Options객체를 전달해야함
- Options들을 사용하여 원하는 동작을 구현
- Vue Instance === Vue Component

### Options

- el 
  - Vue 인스턴스에 연결할 기존 DOM요소

- data
  - Vue  인스턴스의 데이터 객체 == Model
  - 인스턴스의 상태 데이터를 정의하는 곳
- methods
  - Vue 인스턴스에 추가할 메서드
  - 주의 : 화살표 함수를 사용하면 안된다

## Template Syntax

> 렌더링 된 DOM을 기본 Vue 인스턴스의 데이터에 선언적으로 바인딩할 수 있는 HTML 기반 템플릿 구문 사용

### Interpolation(보간법)

- Text
  - {{message}}
- Raw HTML
  - <v-thml="rawHtml"><>
- Attributes
  - \<v-bind:id="dynamicId"> <>
- JS 표현식
  - {{number +1}}

### Directive

- v-접두사가 있는 특수 속성
- 속성 값은 단일 JS 표현식이 됨(v-for은 예외)
- 표현식의 값이 변경될 때 반응적으로 DOM에 적요하는 역할을 함

#### 전달인자

- `:`(콜론)을 통해 전달인자를 받을 수도 있음

#### 수식어

- `.`(점)으로 표시되는 특수 접미사
- directive를 특별한 방법으로 바인딩 해야 함을 나타냄

```JS
// 두개의 결과는 같다
<div id='app1'>
    <p>{{ message}}</p>
    <p v-text='message'></p>
    </div>
<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
   		message:'안녕하세요',
	}
})
```

```Js
/*
<strong>안녕하세요</strong>
<strong>안녕하세요</strong>
안녕하세요
*/
<div id='app1'>
    <p>{{ message}}</p>
    <p v-text='message'></p>
    <p v-html='message'></p>
    </div>
<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
   		message:'<strong>안녕하세요</strong>',
	}
})
```

##### v-show

```js
//false는 display가 none이 됌
//html에 존재하지만 나타나지는 않는 상태
<div id='app1'>
    <p v-show='isTrue'>True</p>
    <p v-html='isFalse'>False</p>
    </div>
<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
   		isTrue : true,
        isFalse : false,
	}
})
```

##### v-if, v-else-if, v-else

```js
<div id='app1'>
    <p v-if='seen'>seen is True</p>
    <p v-if='myType === "A"'>A</p>
	<p v-else-if='myType === "B"'>B</p>
	<p v-else-if='myType === "C"'>C</p>
	<p v-else>not A/B/C</p>
    </div>
<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
   		seen : false,
        myType : 'A',
	}
})
```

- v-show와 v-if

  - show는 실제로 렌더링이 되지만 눈에 보이지 않는 것

  - if는 전달인자가 false인 경우 렌더링이 되지 않음

  - 자주 변경되는 요소라면 show, 
    자주 변경되지 않는 요소라면 if로 정해주는게 
    렌더링 비용을 감소시킬 수 있다.

##### v-for

- 원본 데이터를 기반으로 여러번 렌더링
- item in items 구문 사용
- item 위치의 변수를 각 요소에서 사용할 수 있음
  - 객체의 경우는 key
- v-for 사용 시 __반드시 key 속성__을 각 요소에 작성
- v-if와 함께 사용하는 경우 v-for가 우선순위가 더 높음
  - 단, 가능하면 if와 for를 동시에 사용하지 말 것

```js
<div id='app1'>
    <h2>String</h2>
	<div v-for='char in myStr'>
        {{char}}
    </div>
    <h2>Array</h2>
	<div v-for='fruit in fruits'>
        {{fruit}}
    </div>
	<div v-for='(fruit, idx) in fruits' :key='idx'>
        {{idx}}, {{fruit}}
    </div>
	<div v-for='todo in todos' :key='`todo-${todo.id}`'>
		<p> {{todo.title}} - {{todo.completed}}</p>
    </div>
    <h2>Object</h2>	
	<div v-for='{value, key} in myObj'>
        {{key}} - {{value}}
    </div>
</div>
<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
   		seen : false,
        myType : 'A',
	}
})
```

##### v-bind

- 태그가 가지고 있는 기본속성에 Vue가 가지고 있는 옵션값을 부여하고 싶을때 사용

```js
<style>
    .active{
        color:red;
    }
	.my-background-color {
        background-color : yellow;
    }
</style>    
<div id='app1'>
	<img v-bind:src="imageSrc" alt="">
    //v-bind 생략 가능
	<img :src="imageSrc">
    <div :class="{active : isRed}">
        클래스바인딩
	</div>
	<h3 :class="[activeRed, myBackground]">
        hello
	</h3>
	//bind붙으면 js표현식 사용해야함
	<p :style="{fontSize: fonSize+'px'}">
        this
	</p>
</div>
<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
        fontsize : 16,
   		imageSrc:'https://~~',
        isRed = True,
        activeRed : 'active',
        myBackground : 'my-background-color',
	}
})
```

##### v-on

- 요소에 이벤트 리스너를 연결함
- 약어 : @
  - v-on:click => @click

```js
<body>
    <button v-on:click="alertHello">BTN</button>
	//v-on: 축약어로 @ 사용가능
    <button @click="alertHello">BTN</button>
	//기본동작방지
	<form action="" @submit.prevent="alertHello">
        <button>GO</button>
	</form>
	//키 별칭 사용
	<input type='text' @keyup.enter="log">
    //log 콜백함수의 첫번째 인자인 event 대신에 asdf로 넘겨준다는 뜻
  	<input type='text' @keyup.enter="log('asdf')">
        
    {{message}}
    <button @click='changeMessage'>change message</button>
</body>    

<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
        message : 'Hello',
	},
	methods:{
		alertHello : function (){
	        alert('hello')
    	},
        log : function (something){
            console.log(something)
        },
        changeMessage() {
            this.message = 'NewMessage'
        }
	}
})
```

##### v-model

- HTML form 요소의 값과 data를 양방향 바인딩

```js
<body>
    //단방향
    {{message}}
	<input type='text' @input="chaneMessage">
    //양방향
    {{message}}
    <input type='text' v-model="message">
</body>    

<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
        message : 'Hello',
	},
	methods:{
        changeMessage( event ) {
            this.message = event.target.value
        }
	}
})
```

##### Computed & Method

```js
<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
        message : 'Hello',
	},
	methods:{}, // 메소드의 같은 경우 데이터 그 자체 변경시 (setter 함수)
    computed :{
        //데이터에 의존하는 계산된 값 => 파생변수 (getter 함수)
        //method와 달리 변수 그자체로 쓰일 수 있다.
        //실행시 changedMessage 로만 입력 가능
        //method의 경우 changeMessage()로 실행해야만함
        //return이 반드시 있어야한다 
        changedMessage( event ) {
            return this.message.split('').reverse().join('')
        }
    }
})
```

- computed => 선언형 프로그래밍
  - 계산해야 하는 목표 데이터를 정의
- watch => 명령형 프로그래밍
  - 데이터가 바뀌면 특정 함수(콜백 함수)를 실행

##### filter

- 텍스트 형식화를 적용할 수 있는 필터
- 필터는 자바스크립트 표현식 마지막에 `|`와 함께 추가되어야 함
- 연결 사용(chaining) 가능

```js
<body>
    <div id='app1'>
        {{ numbers | getOddNumbers | getUnderTen}}
    </div>

<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
		numbers:[1,2,3,4,5,6]
	},
	filters:{
        getOddNumbers(array){
            return array.filter(num => num%2)
        },
        getUnderTen(array){
            return array.filter(num => num <10)
        }
	},
    //컴퓨티드로 편리하게 사용가능
    computed :{
        getOddAndUnderTen(){
            return this.number.filter(num => num%2 && num < 10)
        }
    }
})
```



### Lifecycle Hooks

- 각 Vue 인스턴스는 생성될 때 일련의 초기화 단계를 거침
- 그 과정에서 사용자 정의 로직을 실행할 수 있는 Lifecycle Hooks도 호출됨

```js
<script>
    const app1 = new Vue({
    el : '#app1'
    data : {
		numbers:[1,2,3,4,5,6]
	},
    method :{
        getImg : function(){
            axios.get(URL)
            .then(response =>{
                this.imgSrc = response.data.message
            })
        }
    }
    //생성될때 기초값 넣어주는 방법
    created : function(){
        this.getImg()
    }
})
```

