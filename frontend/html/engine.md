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

### 참고자료

[How JavaScript works: an overview of the engine, the runtime, and the call stack](https://blog.sessionstack.com/how-does-javascript-actually-work-part-1-b0bacc073cf)

[JavaScript 엔진 톺아보기 (1)](https://velog.io/@godori/JavaScript-engine-1)
