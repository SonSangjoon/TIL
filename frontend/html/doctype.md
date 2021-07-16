## DOCTYPE

DTD(Docuemnt Type Definition)는 특정 문서가 어떻게 구성되어야하는지 정의합니다.

Document Type(DOCTYPE)의 약자로, 어떤 버전 HTML이 작성되었는지 미리 선언하여 브라우저가 내용을 올바로 표시할 수 있도록 해줍니다. 선언하지 않았을경우, 호환모드(quirks mode)로 동작하게 됩니다.

HTML5표준에 대한 DOCTYPE 선언은 `<!DOCTYPE html>`입니다.

브라우자마다 문서를 나타내는 방식이 다르기 때문에, 호환모드로 동작할경우 크로스 브라우징 이슈가 훨씬 심해집니다.예를 들어,박스모델에서 폭(width)과 높이(height)의 여백처리는 IE가 W3C의 표준과 달리 처리하기에 다른 결과를 보입니다.

\*\* 웹브라우저 레이아웃 엔진으로 호환모드(quirks mode), 거의 표준모드(almost standats mode), 표준모드(standards mode)의 세가지 방식이 존재합니다.
-> 호환 모드는 기존 방식으로 제작된 웹사이트들을 내비게이터 4(Navigator 4)와 인터넷 익스플로러 5의 비표준 동작들을 에뮬레이션합니다.

### 참고자료

[호환 모드와 표준 모드](https://developer.mozilla.org/ko/docs/Web/HTML/Quirks_Mode_and_Standards_Mode)
