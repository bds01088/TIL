# Vue in NodeJS

## 설치

### NPM(Node Package Manager)

> pip와 같은 것

```bash
$ npm install -g @vue/cli
```

- -g는 글로벌에 모두 깐다는 뜻
- 기본적으로 npm은 각각의 가상환경에만 설치하는 걸로 정해져있음



### 모듈이 존재하지 않을 경우

```bash
npm install
```

https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=on21life&logNo=221361358946

- 백엔드에서 install requirements와 같은 느낌이다
- 모듈을 각각 설치한게 다를 수도 있기 때문에 package.json에 기록된 것을 새로 설치하는 명령어이다



### 프로젝트 생성

> git-bash가 아닌 vscode terminal로 진행
>
> git-bash에서는 제대로 작동하지 않음

```bash
$ vue create my-first-app
# vue create 프로젝트명
```

하고 나면 vue의 어떤 버전을 쓸건지 선택하는게 나옴

```bahs
$ Default ([Vue 3] babel, eslint)
  Default ([Vue 2] babel, eslint)
```

여기서 방향키로 Vue2를 가리킨 후 엔터

#### 생성 후

```bash
$ cd my-first-app
$ npm run serve
```

프로젝트 파일로 이동한 뒤에 서버 실행이 가능해진다.



### 프로젝트 구성

#### Babel

> Compiler

- 구버전과 현버전의 언어를 이해시키도록 번역해주는 컴파일러

#### Webpack

> 무근본의 영향
>
> Module Bundler

- 모듈의 수가 많아지고 모듈 간의 의존성(연결성)이 깊어지면서 문제 해결에 어려움이 나타남
- 이러한 현상을 해결하기 위해 모듈간의 의존성 문제를 묶음정리해주는 파일



## 프로젝트 구조

- src/assets
  - 정적 파일들이 담기는 곳 (img같은거)
- src/components
  - 하위 컴포넌트들이 존재하는 곳
  - 컴포넌트 = vue객체
- src/App.vue
  - 최상위 컴포넌트
  - 가장 최상의 캔버스
- src/main.js
  - webpack이 빌드를 시작할 때 가장 먼저 불러오는 entry point
  - 실제 단일 파일에서 DOM과 data를 연결했던 것과 동일한 작업이 이루어지는 곳
  - Vue 전역에서 활용할 모듈을 등록할 수 있는 파일

- package.json / package-lock.json
  - requirements.txt와 동일한 역할
  - 다만 자동으로 작성된다는 장점이 있다
  - 또 버전을 기록하는 점이 있다



## Props & Emit Events

> Vue app은 중첩된 컴포넌트 트리로 구성됨
>
> props는 부모가 자식에게로, events는 자식이 부모에게로

### Component

> 이름 작성은 카멜케이스(CamelCase)
>
> 1. 템플릿
> 2. 스크립트
> 3. 스타일

- 뼈대 작성 : vue + 자동완성 => Vetur확장프로그램이 해줌

#### 부모 component (App.vue)

```vue
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 3. 보여주기 -->
    <!-- <TheAbout :my-message="parentData"/> -->
    <the-About 
      :my-message="parentData" 
      @child-input-change="parentGetChange">
    </the-About>
  </div>
</template>

<script>
//1. 불러오기(import)
import TheAbout from './components/TheAbout.vue'
export default {
  name: 'App',
  //2. 등록하기(register)
  components: {
    TheAbout,
  },
  //data는 반드시 function으로 작성
  data : function() {
    return {
      parentData : "This is Parent Data"
    }
  },
  methods: {
    parentGetChange: function(inputData) {
      console.log('왜불러', inputData)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
```

#### 자식 component (TheAbout.vue)

```vue
<template>
  <!-- template 안에는 반드시 하나의 element만 사용 가능-->
  <!-- 그러므로 div를 써서 모든 요소를 포함시키자 -->
  <div>
    <h1>{{ myMessage }}</h1>
    <p>div쓰면 여러개 가능</p>
    <input 
      type="text" 
      v-model="childInputData"
      @keyup.enter="childInputChange"
    >
  </div>
  
</template>

<script>
export default {
  name: 'TheAbout',
  props:{
    myMessage: String
  },
  data: function(){
    return {
      childInputData:""
    }
  },
  methods : {
    childInputChange : function(){
      console.log("Enter!", this.childInputData)
      //부모 컴포넌트에게 첫번째 인자는 이벤트 발생, 2번째인자부터 넘겨주는 데이터지만
      //왠만하면 context처럼 하나의 인자로만 넘겨주자
      this.$emit('child-input-change', this.childInputData)
    }
  }
}
</script>

<style>
</style>
```



### Props

- 부모(상위) 컴포넌트의 정보를 전달받기 위한 사용자 지정 특성
- 자식(하위) 컴포넌트는 props 옵션을 명시적으로 선언해야 함

1. 부모 컴포넌트에서 자식 컴포넌트를 import해온다.

2. 부모 컴포넌트의 templates에 자식 컴포넌트를 사용한다

3. templates에 사용된 자식 컴포넌트에게 바인딩된 데이터를 내려준다.

   ```vue
   <the-About 
         :my-message="parentData" 
   </the-About>
   ```

4. 자식 컴포넌트에서 props를 정의하고 내려주는 데이터이름과 속성을 적는다

   ```vue
   name : 'child',
   props : {
   	myMessage : String
   }
   ```

5. {{}}로 자식 컴포넌트의 템플릿에 사용한다



### Emit Events

- Listening to Child Components Events
- $emit(eventName)
  - 현재 인스턴스에서 이벤트를 트리거
  - 추가 인자는 리스너의 콜백 함수로 전달

1. 자식 컴포넌트에서 부모에게 전달할 상황일 때 발생시킬 이벤트 작성

   ```vue
   <input 
         type="text" 
         v-model="childInputData"
         @keyup.enter="childInputChange"
       >
   ```

2. methods에 발생될 이벤트 작성
   template에서 발생시키는 이벤트와 동일한 이름으로 작성

3. this.$emit으로 부모에게 전달해줄 이벤트명과 전달 데이터를 전달

   ```vue
   methods : {
       childInputChange : function(){
           console.log("Enter!", this.childInputData)
           //부모 컴포넌트에게 첫번째 인자는 이벤트 발생, 
   		//2번째인자부터 넘겨주는 데이터지만
           //왠만하면 context처럼 하나의 인자로만 넘겨주자
           this.$emit('child-input-change', this.childInputData)
   	}
   }
   ```

4. 부모 컴포넌트의 template에 작성된 자식 컴포넌트의 태그에 이벤트 받아주기
   받는 이벤트는 자식 컴포넌트의 emit에서 작성한 이벤트 명을 적어주어야함
   그 이벤트가 자식으로부터 들어오면 부모 컴포넌트에서 실행시킬 methods함수를 값으로 넣어준다

   ```vue
   <the-About 
         @child-input-change="parentGetChange">
   </the-About>
   ```

5. 실행된 함수에서 자식이 보내준 데이터 받기

   ```vue
   methods: {
       parentGetChange: function(inputData) {
         console.log('왜불러', inputData)
   	}
   }
   ```

   

## Vue Router

> route에 `컴포넌트`를 매핑한 후, `어떤 주소`에서 렌더링할지 알려줌
>
> SPA상에서 라우팅을 쉽게 개발할 수 있는 기능을 제공

### Vue Router plugin 설치

> 왠만하면 프로젝트 `맨 처음`에 설치하자

```bash
$ vue add router
```

기존 프로젝트를 진행하고 있던 도중에 추가하게 되면 __App.vue를 덮어씀__으로,

프로젝트 내에서 router설치를 실행하기 전에 필요한 경우 파일을 `백업`해놓아야한다.

#### use history mode for router

- 기본값으로 해쉬모드를 제공하지만 히스토리 모드가 더 좋다.
- 히스토리모드는 SSR 방식에서의 url과 같은 형태로 표시해준다.

### router-link

> <router-link>

```vue
<router-link to="/">Home</router-link>
```

- 사용자 네비게이션을 가능하게 하는 컴포넌트
- 목표 경로는 'to' prop으로 지정됨
- a태그이지만, 기본 get요청을 제거하고, router-view에 보여줄 컴포넌트를 교체해준다.
- 보여줄 컴포넌트를 선택할 수 있게 해주는 버튼 같은 역할

#### Named Routes

- 이름을 가지는 라우트

- router/index.js에서 정한 name을 기준으로 가져온다

  ```vue
  <router-link :to="{name : 'home'}"
  ```

#### 프로그래밍 방식 네비게이션

- vue인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근할 수 있음
- 따라서 다른 url로 이동하려면 this.`$router`.push로 호출할 수 있다

```vue
<template>
	<div>
        <button @click="moveToHome"> </button>
    </div>
</template>
<script>
    export default {
        name : '~',
        methods : {
            moveToHome(){
                //this.$router.push('/')
                this.$router.push({name : 'home'})
            }
        }
    }
</script>
```

#### Dynamic Route Matching

> variable routing

- 동적 인자 전달
- 동적인자는 :(콜론)으로 시작
- 해당 dynamic route로 들어온 컴포넌트에서는 
  this.`$route`.params로 동적인자를 사용가능하다

```vue
//index.js
import LottoView from '../views/LottoView.vue'
const routes = [
	{
		path : '/lotto/:lottoNum',
		name : 'lotto',
		component : LottoView,
	}
]
//LottoView.vue
<template>
	<h2>
        {{$route.params.lottoNum}}개 번호 추첨
    </h2>
</template>
<script>
    ~,
    methods: {
        function(){
            const n = this.$route.params.lottoNum
        }
    }
</script>
//App.vue
<template>
	<router-link to="/lotto/:lottoNum">Home</router-link>
	<router-link :to="{name : 'lotto', params:{lottoNum:6}}">lotto</router-link>
</template>
```



### router-view

> <router-view>

```vue
<router-view/>
```

- 주어진 라우터에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
- 실제 component가 DOM에 부착되어 보이는 자리를 의미



### router/index.js

> 장고에서 views.py랑 똑같은 곳
>
> import HomeView from '../views/HomeView.vue'
>
> 임포트를 통해 vue파일 가져와서 주소에 알맞게 보여주는 역할

### views

> 장고에서 templates폴더랑 같은 곳
>
> vue컴포넌트들을 보관하고 있음



## VueX

> 상태(state)를 전역 저장소로 관리할 수 있도록 지원하는 라이브러리

- 상태가 예측 가능한 방식으로만 변경될 수 있도록 보장하는 규칙 설정
- 애플리케이션의 모든 컴포넌트에 대한 중앙 집중식 저장소 역할

- 컴포넌트의 공유된 상태를 추출하고 이를 전역에서 관리하도록 함
- 동일한 state를 공유하는 다른 컴포넌트들도 동기화 됨

### VueX 핵심 컨셉

1. State
   - 모든 어플리케이션 상태를 포함하는 원본 소스(single source of truth)의 역할을 함
2. Mutation
   - 실제로 state를 변경하는 유일한 방법
   - handler(핸들러함수)는 반드시 `동기적`이여야함
   - 첫인자로 항상 state를 받음
   - Actions에서 commit() 메서드에 의해 호출됨
3. Actions
   - state 변경을 제외한 모든 함수를 실행
   - context 객체 인자를 받음
   - dispatch() 메소드를 통해 호출
4. Getters
   - state를 변경하지 않고 `활용`하여 계산을 수행
   - computed 속성과 마찬가지로 getters의 결과는 state 종속성에 따라 캐시(cached)됌

### VueX 사용

#### 설치

```bash
$ vue add vuex
```



### Todo App

```vue
//App.vue
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 바인딩이 되지 않아서 delete와 같이 methods에 함수화 하지 못한다 -->
    <h1>Todo List</h1>
    <h2>All Todos : {{allTodos}}</h2>
    <h2>Completed Todo : {{completedTodos}} </h2>
    <h2>Uncompleted Todo : {{uncompletedTodos}} </h2>
    <todo-form></todo-form>
    <todo-list></todo-list>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList.vue'
import TodoForm from '@/components/TodoForm.vue'
// import {mapGetters} from 'vuex'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm
  },
  //getter를 사용해보자
  //getter를 통해 완료된 todo의 개수를 출력해보자
  //methods를 통해서는 못쓴다
  //computed는 된다
  //getter 자체가 computed와 유사하기 때문에
  computed : {
    completedTodos() {
      return this.$store.getters.completedTodos
    },
    uncompletedTodos() {
      return this.$store.getters.uncompletedTodos
    },
    allTodos() {
      return this.$store.getters.allTodos
    }
    
  },
  //mapGetters를 이용할 수도 있다
  // computed : {
  //   ...mapGetters(['completedTodos'])
  // }
}
</script>

//store/index.js
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 바인딩이 되지 않아서 delete와 같이 methods에 함수화 하지 못한다 -->
    <h1>Todo List</h1>
    <h2>All Todos : {{allTodos}}</h2>
    <h2>Completed Todo : {{completedTodos}} </h2>
    <h2>Uncompleted Todo : {{uncompletedTodos}} </h2>
    <todo-form></todo-form>
    <todo-list></todo-list>
  </div>
</template>

<script>
import TodoList from '@/components/TodoList.vue'
import TodoForm from '@/components/TodoForm.vue'
// import {mapGetters} from 'vuex'

export default {
  name: 'App',
  components: {
    TodoList,
    TodoForm
  },
  //getter를 사용해보자
  //getter를 통해 완료된 todo의 개수를 출력해보자
  //methods를 통해서는 못쓴다
  //computed는 된다
  //getter 자체가 computed와 유사하기 때문에
  computed : {
    completedTodos() {
      return this.$store.getters.completedTodos
    },
    uncompletedTodos() {
      return this.$store.getters.uncompletedTodos
    },
    allTodos() {
      return this.$store.getters.allTodos
    }
    
  },
  //mapGetters를 이용할 수도 있다
  // computed : {
  //   ...mapGetters(['completedTodos'])
  // }
}
</script>

//components/TodoList.vue
<template>
  <div>
      <!-- todos의 각 객체들을 하나하나 todolistitem으로 prop해야하니까 -->
      <!-- 근데 todos는 state에 있으니까 this.$store.state.todos로 불러와야한다 -->
      <!-- prop명은 todo -->
      <!-- 근데 todos 불러오는게 너무 길다고 생각되면 => 컴퓨티드로 -->
      <!-- v-for="todo in $store.state.todos"  -->
      <todo-list-item
        v-for="todo in todos" 
        :key="todo.date"
        :todo="todo"
      ></todo-list-item>
  </div>
</template>

<script>
// todolistitem으로 하나의 todo를 todolistitem으로 관리할 예정이니까
import TodoListItem from './TodoListItem.vue'
export default {
    name : 'TodoList',
    components :{
        TodoListItem,
    },
    //컴퓨티드에서 todos를 불러와서 template에서 줄여주자
    computed : {
        todos() {
            return this.$store.state.todos
        }
    }
}
</script>

//components/TodoForm.vue
<template>
  <div>
      <input type="text" 
        v-model.trim="todoTitle" 
        @keyup.enter="createTodo">
  </div>
</template>

<script>
export default {
    name : 'TodoForm',
    data() {
        return {
            todoTitle : ''
        }
    },
    methods : {
        createTodo() {
            //저장할 model 생성하는 느낌으로
            const newTodo = {
                title : this.todoTitle,
                isCompleted : false,
                data : new Date().getTime()
            }
            //생성했으니 이제 저장할 차례
            //store의 actions함수 불러오려면
            //$store를 부르고, dispatch함수로 actions 목록에 원하는
            //메소드를 첫인자로 가져오고, 전달할 데이터를 두번째 인지로 준다
            this.$store.dispatch('createTodo', newTodo)
            //저장했으니 다음을 위해 초기화해주자
            this.todoTitle = ''
        }
    }
}
</script>

//components/TodoListItem.vue
<template>
  <div>
      <!-- 이제 업데이트:완료한 todo는 중간줄 긋기 해보자 -->
      <!-- isCompleted가 true면 줄긋는 css가져오기 -->
      <span 
        @click="updateTodo(todo)"
        :class="{'is-completed' : todo.isCompleted}"
        >
        {{todo.title}}
      </span>
      <!-- 이제 삭제도 추가해보자 -->
      <!-- mapActions을 쓰면서 데이터를 methods에서 못넘기니까 -->
      <!-- 여기서 바로 넘겨준다 -->
      <!-- 원래는 여기서 함수실행하면 안되지만 -->
      <!-- 이것만 예외상황 -->
      <button @click="deleteTodo(todo)"
      >X</button>
  </div>
</template>

<script>
//바로 index.js의 actions의 메소드를 사용하려면
import {mapActions} from 'vuex'
//import veux를 해주면 되는데
//veux에 mapActions를 사용할 것이다
//그러므로 축약형 사용가능

export default {
    name : 'TodoListItem',
    props :{
        todo : Object,
    },
    // methods : {
    //     deleteTodo() {
    //         //todo 하나의 객체를 표현하기 위한 vue 객체임
    //         //이 객체 todo를 넘겨주면 된다
    //         this.$store.dispatch('deleteTodo', this.todo)
    //     }
    // },
    //mapActions(['deleteTodo']) === {deleteTodo() {}} 똑같다
    //결국 mapActions자체가 methods처럼 메소드집단이므로 그냥 :만 써준다
    //mapActions()의 인자는 배열형태로 들어온다
    //배열에는 여러 메소드들을 적으면 여러개로 가져온다
    //mapActions를 쓰면 데이터를 여기서 못넘겨주니까 => template로 이동
    methods : mapActions(['deleteTodo', 'updateTodo'])
    //만약 mapActions의 메소드 외에 따로 이 컴포넌트의 메소드를 추가 작성하려면
    //methods : {
        //...mapActions(['deleteTodo']),
        //myMethod(){}
    //}
    //이렇게 스프레드로 풀어서 요소 형태로 추가한 다음 작성 가능
}
</script>

<style>
/* 이 컴포넌트의 값들에게만 적용하려면 scoped를 써준다
    <style scoped>
 */
.is-completed {
    text-decoration: line-through;
}
</style>
```



## Local Storage

> client 컴퓨터에 저장

~~session storage : 탭이 켜져있는 동안만 저장~~

### 접근하기

> localStorage.setItem('todos', data)
>
> localStorage.getItem('todos')

- 데이터를 저장할때, 문자열로 변환을 안해주면 입력받은 값의 타입만 저장해준다

### 문자열 변환

> JSON.stringify(todos)

### 문자열을 원래 형태로 변환

> JSON.parse(data)



### VueX-persistedstate

> VueX state를 자동으로 브라우저의 localStorage에 저장해주는 라이브러리 중 하나
>
> 새로고침해도 vuex state를 유지시킴

#### 설치

```bash
$ veu i veux-persistedstate
```

#### 사용

```vue
//index.js
import createPersistedState from 'veux-persistedstate'

export default new Vuex.Store({
	plugins : [
		createPersistedState(),
	],
})
```



### life-cycle

> 컴포넌트의 주기

- beforeCreate() {} : 컴포넌트가 생성되기 전
  - 컴포넌트 데이터 접근 불가능
- created() {} : 컴포넌트가 생성된 직후
  - dom 접근 불가능
  - 데이터 접근 가능
- beforeMount() {} : 상위 컴포넌트에 부착되기 전
  - dom 접근 불가능
- mounted() {} : 부착된 후
  - dom 접근 가능
- beforeUpdate() {} : 업데이트가 실행되지만 갱신자체는 되기 전
- updated() {} : 업데이트 이후
- beforeDestory() {} : mount 상태 해체와 동일, 상위 컴포넌트에서 떨어지기 전
- destroyed() {} : 탈착 후
  - dom 접근 불가능
