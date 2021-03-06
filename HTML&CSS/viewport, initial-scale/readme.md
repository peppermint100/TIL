### Viewport

meta viewport 값 width=device-width를 사용하면 기기 독립적 픽셀에서 화면 너비에 맞게 페이지를 맞춥니다. 이렇게 하면 렌더링되는 화면이 작은 휴대폰이든 큰 데스크톱 모니터에든 상관없이, 다양한 화면 크기에 맞게 페이지의 콘텐츠를 재배치할 수 있습니다.

- meta viewport 태그를 사용하여 브라우저 뷰포트의 너비와 배율을 제어합니다.
- 기기 독립적 픽셀에서 화면 너비에 맞추려면 width=device-width를 포함합니다.
- 기기 독립적 픽셀과 CSS 픽셀 간에 1:1 관계를 설정하려면 initial-scale=1을 포함합니다.

### 상대 단위 사용

반응형 디자인의 핵심 개념은 고정 너비 레이아웃과 반대되는 유동성 및 비례성입니다. 측정 시에 상대 단위를 사용하면 레이아웃이 간단해지며, 뷰포트에 비해 너무 큰 구성요소가 실수로 만들어지는 것을 막아줍니다.

예를 들어, 최상위 div에서 너비를 100%로 설정할 경우, 뷰포트의 너비가 뷰포트에 비해 너무 크거나 너무 작지 않도록 조정됩니다. 320px 너비의 iPhone, 342px 너비의 Blackberry Z10 또는 360px 너비의 Nexus 5에 상관없이 div가 맞춰집니다.

또한 상대 단위를 사용하면 브라우저가 사용자 확대/축소 수준에 따라 콘텐츠를 렌더링할 수 있으며, 가로 스크롤 막대를 페이지에 추가할 필요가 없습니다.
