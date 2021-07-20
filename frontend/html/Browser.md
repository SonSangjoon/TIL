## 브라우저 렌더링 



###  렌더링 엔진

브라우저가 화면에 나타나는 요소를 렌더링 할때, 사파리 - 웹킷(Webkit) / 파이어폭스 - (Gecko) / 크롬 - (Webkit -> Blink) 렌더링 엔진(Rendering Engine)을 사용합니다.

각각의 렌더링 엔진들은 별로 규칙에 따라서 지원하는 표준이 다르거나 렌더링 알고리즘과 방식이 차이가 있어, 각 브라우저 별로 자동 테스트를 통해 브라우저의 호환성 문제를 검사해야 합니다.



### 렌더링 과정

1. HTML 파싱 후, DOM(Document Object Model)트리 구축
2. CSS 파싱후, CSSOM(CSS Object Model)트리 구축

> - DOM 및 CSSOM 은 서로 독립적인 데이터 구조입니다.
>
> - Chrome DevTools Timeline을 사용하면 DOM 및 CSSOM의 생성 및 처리 비용을 수집하고 점검할 수 있습니다.
> - 바이트 -> 문자 -> 토큰 -> 노드 -> 객체 모델 
>   - 변환: 바이트를 문자로 변환합니다.
>   - 토큰화: 토큰을 식별합니다.
>   - 렉싱: 방출된 토큰은 해당 속성 및 규칙을 정의하는 객체로 변환합니다.
>   - DOM 생성: HTML 마크업이 여러 태그간의 관계를 정의 하기에 트리 데이터 구조내에 연결합니다.

3. JavaScript 실행

> - HTML 중간에 스크립트가 있다면 HTML 파싱이 중단됩니다.

4. DOM과 CSSOM을 조합하여 렌더트리(Render Tree)구축
5. 뷰포트 기반으로 렌더트리의 각 노드가 가지는 정확한 위치와 크기 계산(Layout/ Reflow 단계)
6. 계산한 위치/크기를 기반으로 화면에 띄움(Paint 단계)







#### 참고자료

[객체 모델 생성](https://developers.google.com/web/fundamentals/performance/critical-rendering-path/constructing-the-object-model?hl=ko)

[브라우저 렌더링 과정 - Reflow Repaint, 그리고 성능 최적화](https://boxfoxs.tistory.com/408)

[브라우저 렌더링 원리](https://github.com/baeharam/Must-Know-About-Frontend/blob/main/Notes/frontend/browser-rendering.md)



