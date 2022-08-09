# Socket IO

### Socket io vs webSocket

### Socket io는 webSocket을 주로 사용하는 것이지 webSocket에 포함되어 있는 것이 아니다.

### 설치

```bash
npm i(install) socket.io
import SocketIO from "socket.io"
```

#### wsServer는 httpServer 위에 구성하는게 편하고, 같은 포트를 사용 가능할 수 있다.

```js
# backend
const httpServer = http.createServer(app)
const wsServer = SocketIO(httpServer)
```

Socket io를 설치하고 서버에 사용하는 순간, 

`localhost:3000/socket.io/socket.io.js` 라는 주소로 접속이 가능하고

해당 주소에는 browser에 설치해야하는 socket.io 코드가 들어있다.

#### 왜 browser에 socket io를 설치해야하는가?

위에서 말했다시피 socket io는 websocket`를` 포함하고 있기 때문에 브라우저에서 백엔드에 사용하는 socket.io를 맞춰주기 위해 설치해야만 한다

```html
script(src="/socket.io/socket.io.js")
script(src="public/js/app.js") #따로 분리된 js파일 불러오는 
```

### function io() -> 서버연결

백엔드에 설치되어있는 socket.io를 자동적으로 찾아주는 함수이다.

```js
#frontend
const socket = io()
```

```js
#backend
wsServer.on("connection", socket => {
  console.log(socket)  
})
```

## 채팅방 연결

```js
#frontend
function 방을 들어가는 행동(event){
    event.preventDefault()
    const input = form.querySelector("input")

    #socket.emit(eventname, data, function)
    socket.emit("enter_room", { payload : input.value },  ...args, function())

    #websocket에서 send로 보내는 것을 emit으로 보낼 수 있고,
    #이벤트 이름을 message로만 보내야만 하는 것이 아닌 
    #내가 커스텀한 이벤트명으로 보낼 수 있으며
    #이벤트명 다음, args에 object를 보낼 수 있다.
    #object를 json으로 변환하여 string으로 보내야하는 과정들을 거치지 않고
    #바로 object를 보낸다.
    #뿐만 아니라 모든 형태를 보낼 수 있다.
    #또한 `서버에서 실행 타이밍을 정하고` 싶은 함수를 보낼 수 있다.
    #함수는 항상 맨 마지막에 넣어야함
}
```

```js
#backend
wsServer.on("connection", socket => {
    socket.on("enter_room", (msg, function) => {
        console.log(msg)
        #프론트에서 보낸 함수를 백엔드에서 실행버튼을 가짐
        #프론트에서 보낸 함수이기때문에 실행 자체는 프론트에서 이루어진다.
        function()
    })
})
```

#### 즉, socket.io는 websocket의 제한적인 데이터들만 보내는 것을 개선함

1. back에서 들을 이벤트 이름자체를 커스텀할 수 있다

2. 이벤트를 통해 보내는 msg가 string으로 제한되는 것이 아닌, object, function 등 형태에 제약을 받지않는다.

3. function은 `항상 맨 마지막`에 들어가야한다

4. backend로 넘어간 function은 실행 버튼은 backend에서 누르는 것이기 때문에 실행하기전에 frontend에서 설정된 파라미터가 존재한다면 backend에서 해당 파라미터에 대한 값을 넣어줄 수 있다.

### 실질적인 방 분리

```js
#backend
wsServer.on("connection", socket => {
    socket.on("enter_room", (roomname, function) => {
        console.log(socket.id)
        console.log(socket.rooms)
        socket.join(roomname)
        #socket.join(['room1', 'room2')
        #위처럼 한번에 여러방을 참가할 수 있다.
        console.log(socket.rooms)
    })
})
```

해당 소켓이 어떤 방에 참여하고 있는지 socket.rooms를 통해 목록을 가져올 수 있다.

채팅방에 들어간다면 socket.join을 통해서 해당 방으로 이동 가능하다

socket.rooms는 set 형태를 가지고 있다.

각 socket은 기본적으로 자신의 socket.id로 구성된 방을 초기값으로 가진다.

![](Socket%20IO_assets/2022-07-25-11-21-40-image.png)

#### 방 나가기

```js
socket.leave(roomname)
```

#### 방 전체에 메세지 보내기

```js
socket.to(roomname).emit("event")
```

#### DM 보내기

```js
socket.to(another socket id).emit("event")
```

#### Disconnecting (socket.io가 준 event이름)

브라우저나 방을 나갈 것이지만 방에는 존재하는 상태

lifecycle hook에서 beforeDestroy 같은 느낌임

```js
#backend

socket.on("disconnecting", () => {
    socket.rooms.forEach((room) => socket.to(room).emit("event"))
})
```

```js
#frontend
function addmessage(msg) {
    console.log(msg)
}

socket.on("event", () => {
    addmessage("someone left")
})
```

### 방에서 채팅하기

```js
#frontend

function handleMessageSubmit(event) {
    event.preventDefault()
    const input = room.querySelector("input")
    socket.emit("new_message", input.value, roomname, () => {
        #이건 채팅 친 사람이 볼 때 you라고 떠야하니까 해당 방의 모든 사람들에게
        #채팅을 보내고 난 다음 아래 함수를 백엔드에서 실행시켜주기 위해 넘기는 
        addMessage(`you : ${input.value}`)
    })
}
socket.on("new_message", (msg) => addMessage(msg))
```

```js
#backend

socket.on("new_message", (msg, room, done) => {
    #해당 룸의 모든 소켓(메세지 보낸 소켓 제외)에게 메세지 전달.
    socket.to(room).emit("new_message", msg)
    #프론트에서 넘겨 있는 함수 실행
    done()
}
```

### 닉네임 설정

닉네임 입력받는 form을 생성하고 입력받으면 닉네임을 추가해주는 이벤트를 서버로 emit한 뒤, socket["nickname"]이라는 새로운 변수자리에 값을 더해주면 된다.

해당 닉네임이 필요할 때 마다 socket.nickname 값을 같이 emit해주면 된다.

### 공지사항 채팅 전달하기

모든 소켓들을 공지사항이라는 채팅방에 기본적으로 입장시켜놓으면 될듯

```js
io === wsServer
#서버에 연결되어있는 모든 소켓들을 announce방에 참가시키기.
io.socketsJoin('announce')

#room1에 있는 소켓들을 room2에 모두 참여시키기.
io.in('room1').socketsJoin('room2')
```

## Adapter

> 모든 클라이언트는 하나의 서버에만 연결되지않는다.
> 
> 여러개의 서버를 사용할 경우, 서버간의 통신을 하려면 server a => adpater a => db => adapter b => server b 로 거쳐가야한다
> 
> 즉, adapter는 어플리케이션과 저장공간(db, memory) 사이의 미들웨어(창) 같은 곳이다.

현재 연결된 소켓이 어떤게 있는지, 해당 공간에 room이 어떤게 있는지 파악가능하다

```js
wsServer === io
console.log(io.sockets.adapter)
```

rooms, sids는 map형태(딕셔너리 형태)로 저장되어있다.

#### 방 개수 또는 열린 방 찾기

소켓은 기본적으로 자신의 소켓id를 방으로 가진다.

이를 이용하여, rooms의 값이 sids에 존재하지 않는다면, 그것은 공개방이라는 뜻이다.

```js
#backend

function publicRooms() {
    const sids = io.sockets.adapter.sids
    const rooms = io.sockets.adapter.rooms
    const publicRooms = []
    rooms.forEach((_, key) => {
        if(sids.get(key) === undefined){
            publicRooms.push(key)
        }
    })
    return publicRooms
}
```

#### 방 목록 갱신

현재에는 방을 들어가면, 존재하던 방이름이 아니라면 새로 생성하고 들어가기 때문에, enter_room이라는 이벤트가 발생할 때마다 방 목록을 갱신해주어야한다.

```js
#backend

socket.on("enter_room", (roomName, done) => {
    socket.join(roomName)
    done()
    socket.to(roomName).emit("welcome", socket.nickname)
    wsServer.sockets.emit("room_change", publicRooms())
}
```

```js
#frontend

socket.on("room_change", (rooms) => {
    const roomList = welcome.querySelector("ul")
    roomList.innerHTML = ""
    if (room.length === 0){
        return
    }
    rooms.forEach(room => {
        const li = document.createElement("li")
        li.innerText = room
        roomList.append("li")
    }) 
} )
```

# Video Call

### 영상화면 가져오기

```js
#frontend

-HTML-
body
    main
        video(class="myFace", autoplay=True, playsinline=True, width="400", height="400")

-Script-
const socket = io()

const myFace = document.getElementById("myFace")

#stream === video + audio
let myStream

async function getMedia() {
    try {
        myStream = await navigator.mediaDevice.getUserMedia({
            audio: true,
            video: true,
        })
        myFace.srcObject = myStream
    } catch (e) {
        console.log(e)
    }
}


getMedia()

function handleMuteClick() {
    myStream.getAudioTracks().forEach(track => track.enabled = !track.enabled)
    if (!muted){
        muteBtn.innerText = "Unmute"
        muted = true
    } else {
        muteBtn.innerText = "Mute"
        muted = false
    }
}
function handleVidoeClick() {
    myStream.getVideoTracks().forEach(track => track.enabled = !track.enabled)
    if (cameraOff){
    } else {
    }
}
```

# WebRTC

> peer to peer 시스템
> 
> socket.io는 서버와 통신하는거임
> 
> WebRTC에서는 서버에 signaling이라는 행동만 하는데, 이는 단순히 해당 브라우저가 어디에 위치해있는지 알리기 위한 것임( ip, port, enviroment 등등)

![](Socket%20IO_assets/2022-07-25-21-16-11-image.png)

P2P 상태가 된다면, 위에 만들어진 video call stream 정보를 서로의 브라우저에 전달함으로써 영상통화가 가능해진다.

### Socket.join을 통한 시그널링하기

이전의 채팅방 들어가는것처럼 socket.join을 통해 하나의 방에 들어가게 된다면, 그때부터 브라우저와 브라우저를 이어주는 P2P 프로세스를 진행하면 된다.

채팅방이라는 곳으로 여러 브라우저들이 어디있는지 확인이 가능해지니, 해당 브라우저들을 이제 p2p로 서로 데이터를 주고 받게 해준다.

### P2P 프로세스

![](Socket%20IO_assets/2022-07-25-21-28-52-image.png)

#### getUserMedia

audio track과 video track을 가져오는 것을 말한다.

video call에서 이미 가져왔다

#### makeConnection

```js
#frontend
let myPeerConnection
let myStream

myStream = await navigator.mediaDevice.getUserMedia({
            audio: true,
            video: true,
        })

function makeConnection(){
    const myPeerConnection= new RTCPeerConnection();
    #peerConnection에 해당 트랙들을 넣어서 데이터 전송해주어야한다.
    myStream.getTracks().forEach(track => 
        myPeerConnection.addTrack(track, myStream))
}
```

#### offer

> 먼저 초대장? 같은걸 보내야하는 사람이 정해져야하는데, 미팅방에 이미 존재하는 사람이 초대장을 금방 들어온 사람에게 보내야하는 것이다.

```js
#frontend

#A브라우저에게 B브라우저가 들어왔다고 이벤트가 알려주는 순간
#아래 코드는 A브라우저에서만 실행된다.
socket.on("welcome", async() => {
    #offer를 생성한다.
    const offer = await myPeerConnection.createOffer()
    #또한 생성된 offer를 통해서 소통해야하므로 저장한다고 함.
    myPeerConnection.setLocalDescription(offer)
    socket.emit("offer", offer, roomName)
}
#A브라우저에 답변 저장.
socket.on("answer", answer => {
    myPeerConnection.setRemoteDescription(answer)
})


#아래코드는 B브라우저에서 실행될 것이다.
socket.on("offer", async (offer) => {
    #B브라우저 기준으로 현재 받은 offer는 외부에서 받아온 description이므로
    #remoteDescription에 저장하는듯하다.
    #에러가 뜬다면, getMedia함수가 너무 빨리 시작되어서이므로 해당 함수에 await를 써주
    myPeerConnection.setRemoteDescription(offer)
    const answer = await myPeerConnection.createAnswer()
    #초대장을 바탕으로 답을 도출해내고, 그 값을 B브라우저의 localDescription에 저장한다. 
    myPeerConnection.setLocalDescription(answer)
    #이제 답을 초대장 보낸 브라우저에 보내주어야한다.
    socket.emit("answer", answer, roomName)
})
```

```js
#backend

wsServer.on("connection", (socket) => {
    ...
    socket.on("offer", (offer, roomName) => {
        socket.to(roomName).emit("offer", offer)    
    })
    socket.on("answer", (answer, roomName) => {
        socket.to(roomName).emit("answer", answer)
    })
})
```

#### IceCandidate

> offer와 answer 모두 가지게 된다면,
> 
> p2p양쪽에서 iceCandidate라는 이벤트를 실행하게 된다.
> 
> internet connectivity establishment(인터넷 연결 생성)

어떤 소통 방법이 가장 좋은지 후보들을 고르고 그 중 하나를 협의해서 정한다는 이벤트

서로서로 iceCandidate를 보내서 자동적으로 협의하게됨

```js
#frontend
function makeConnection(){
    ...
    myPeerConnection.addEventListner("icecandidate", handleIce)
}

function handleIce(data) {
    #얻어진 data는 다른 브라우저에게 보내져야지 서로 협의할 수 있다.
    socket.emit("ice", data.candidate, roomName)
}

socket.on("ice", (ice) => {
    myPeerConnection.addIceCandidate(ice)
})
```

```js
#backend

socket.on("ice", (ice, roomName) => {
    socket.to(roomName).emit("ice", ice)
}
```

#### add stream

```js
#frontend
function makeConnection(){
    ...
    myPeerConnection.addEventListner("icecandidate", handleIce)
    myPeerConnection.addEventListner("addstream", handleAddStream)
}

function handAddStream(data) {
    #html 요소 가져오기.
    const peerFace = document.getElementById("peerFace")
    #연결된 상대방의 스트림(audio, video) 데이터를 가져와서 요소에 넣어주는 
    peerFace.srcObject = data.stream
}
```



## 카메라 전환하기

sender라는 것이 track을 조작하는데 있어서 사용된다.

![](Socket%20IO_assets/2022-07-25-22-32-18-image.png)



## STUN

네트워크상에서 방화벽이 존재하므로

같은 네트워크 상에서는 네트워크를 private하게 매핑할 수 있다.

하지만 다른 네트워크와는 연결이 불가능하므로

public(공용) ip를 알려주는 것이 바로 STUN서버이다.

```js
function makeConnection() {
    myPeerConnection = new RTCPeerConnection({
        iceServer: {
            urls : [
#아래는 구글이 제공하는 무료 STUN서버이다.
                "stun:stun.l.google.com:19302",
                "stun:stun1.l.google.com:19302",
                "stun:stun2.l.google.com:19302",
                "stun:stun3.l.google.com:19302",
                "stun:stun4.l.google.com:19302"
            ],
        },
    }),
}
```
