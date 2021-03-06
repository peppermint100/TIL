## 시멘틱 웹

시멘트는 건설업에서 사용하는 단단해지는 물질입니다. 그리고 시멘틱은 어떤 프레임과 프레임을 확실히 나누는 의미에서 시멘틱이라는 말을 사용하기도 합니다.

만약

```html
<div id="header">
  <h1>
    This is Title!
  </h1>
</div>
```

이라는 HTML코드가 있다고 합시다. id를 확인하니 헤더 역할을 하는 HTML 코드입니다. 아마 웹의 가장 상단에 위치하게 생겼죠. 하지만 div라는 굉장히 의미가 다양하게 사용될 수 있는 태그를 사용하고 있고 id를 주지 않는다면 이게 헤더인지 모를뿐 더러 만약 주더라도 개발자가 id를 확인해야만 합니다. 심지어 id를 header-title 이런식으로 준다면 더더욱 헷갈리겠죠

```html
<header>
  <h1>
    This is Title!
  </h1>
</header>
```

하지만 만약 이렇게 준다면 이 코드는 무조건 헤더 역할을 하겠구나! 더더욱 쉽게 알아볼 수 있습니다. 개발자들이 유지보수 하기도 편하고 코드도 깔끔해보입니다. 이러한 태그를 시멘틱 태그라고 하고 심지어 이런 태그는 웹 브라우저가 알아볼 수 있습니다. 시멘틱 태그는

| tag     | Description        |
| ------- | ------------------ |
| header  | 헤더               |
| nav     | 네비게이션         |
| aside   | 사이드             |
| section | 섹션을 나누는 태그 |
| footer  | 푸터(하단)         |

이러한 종류가 있습니다. 이렇게 웹 브라우저가 HTML 태그를 알아볼 수 있다는 것은 검색엔진에 브라우저가 보다 명확한 정보를 줄 수 있음을 의미합니다. 이렇게 웹 컨텐츠 자체에 명확한 의미를 줌으로서 검색엔진 최적화, 크롤링, 인덱싱을 더 효과적으로 할 수 있습니다.
