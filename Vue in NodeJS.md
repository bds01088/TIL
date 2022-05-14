# Vue in NodeJS

## 설치

### NPM(Node Package Manager)

> pip와 같은 것

```bash
$ npm install -g @vue/cli
```

- -g는 글로벌에 모두 깐다는 뜻
- 기본적으로 npm은 각각의 가상환경에만 설치하는 걸로 정해져있음



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

### Emit Events



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

### main.js

### App.vue

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

# 5/11일 workshop 참조하기



### State

> state는 곧 data이며 해당 어플리케이션의 핵심이 되는 요소
>
> 중앙에서 관리하는 모든 상태 정보



### VueX-persistedstate

> VueX state를 자동으로 브라우저의 localStorage에 저장해주는 라이브러리 중 하나
>
> 새로고침해도 vuex state를 유지시킴

#### 설치

```bash
$ veu i veux-persistedstate
```

