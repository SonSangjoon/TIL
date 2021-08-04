## 자바스크립트 엔진

대부분 자바스크립트는 싱글 쓰레드기반(자바 스크립트의 메인 쓰레드인 이벤트 루프가 싱글 쓰레드이기 때문, 다만 웹브라우저나 NodeJS같은 멀티 쓰레드 환경에서 실행된다)이다. 크롬은 자바스크립트 엔진으로 V8을 사용합니다.

- 엔진의 주요 구성요소
  - Memory Heap: 메모리 할당이 일어나는 곳
  - Call Stack: 코드 실행에 따라 호출 스택이 쌓이는 곳

## 런타임

자바스크립트 런타임은 자바스크립트 엔진, Web API, 콜백 큐, 이벤트 루프, 렌더 큐로 구성됩니다.

- Web API: 자바스크립트 엔진에 정의 되지 않았던, setTimeout, HTTP 요청 메서드, DOM 이벤트 등의 메서드를 지원합니다.

- 콜백 큐: Web API 결과값을 쌓아 두는 큐입니다.

- 이벤트 루프: 이벤트 루프는 콜 스택과 콜백 큐를 관찰하는 역할을 합니다. 콜 스택이 비어있으면 콜백 큐의 첫번째 콜백을 스택에 쌓습니다.

## 자바스크립트 런타임

자바스크립트 엔진 밖에서도 자바스크립트에 관여하는 요소들이 있다. Wep API, Task Queue, Event Loop등이 있습니다. 런타임은 특정 언어로 만든 프로그램들을 실행할 수 있는 환경입니다. Node.js나 크롬등의 브라우저들은 자바스크립트가 구동되는 환경이기 때문에, 이를 자바스크립트 런타임이라고 합니다.

- Web API : Web API는 브라우저에서 제공되는 API이다. 자바스크립트 엔진에서 정의되지 않았던 setTimeout이나 HTTP 요청(ajax) 메소드, DOM 이벤트 등의 메소드를 지원합니다.

- Task Queue : 이벤트 발생 후 호출되어야 할 콜백 함수들이 기다리는 공간. 이벤트 루프가 정한 순서대로 줄을 서 있으므로 콜백 큐(Callback Queue) 라고도 합니다.

- Event Loop : 이벤트 발생 시 호출할 콜백 함수들을 관리하고, 호출된 콜백 함수의 실행 순서를 결정합니다.

### 참고자료

[How JavaScript works: an overview of the engine, the runtime, and the call stack](https://blog.sessionstack.com/how-does-javascript-actually-work-part-1-b0bacc073cf)

[JavaScript 엔진 톺아보기 (1)](https://velog.io/@godori/JavaScript-engine-1)

[javascript 동장 원리와 비동기 처리](https://ingg.dev/js-work/)
