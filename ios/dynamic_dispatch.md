인프런 앨런님의 강의를 보면 ViewController 앞에 final을 붙이는게 좋다고 언급한 내용이 있다.
강의에서는 상속이 불가능 하도록 알려준다 정도로 언급이 되었는데, 해당 내용에 대해 궁금해 조금 더 
자세히 조사해 보았다.

먼저 제대로 알아보기 이전에 static dispatch와 dynamic dispatch에 대해 알 필요가 있다.

dispatch는 프로그램에서 어떤 메소드나 프로퍼티를 호출할 때 어떤 것을 호출할지
알아내는 과정, 방식을 의미한다.


## 1. Static Disaptch(Direct Call)
---
변수의 명목상 타입에 맞추어 메소드와 프로퍼티를 참조하며 이런 작업이 컴파일
타임에 일어난다. 즉 실제 앱이 실행된 이 후에는 정해진 프로퍼티와 메소드를 맞게 호출한다. Static Dispatch는 이러한 부분에서 성능적인 이점이 있지만 자식 클래스의 요소를 호출하고 싶을 때 명시적인 타입 캐스팅으로 변수를 자식 타입으로
만들어 주어야 한다. 즉 객체지향 프로그래밍의 다형성을 활용하기가 어렵다.

## 2. Dynamic Disaptch
---
변수의 실제 타입에 맞춰서 메소드와 프로퍼티를 참조, 호출한다. 코드에서 이 경우를 명시하지 않으므로 런타임에서 체크할 수 밖에 없다. 즉 Static Dispatch보다 성능상에서 불리하다.

Swift는 Dynamic Dispatch를 채택했으므로 개발자가 직접 프로퍼티의 참조, 호출을 신경써주어야 한다. 그래서 ViewController 앞에 final을 붙이는 것이다.
이렇게 코드를 작성할 때의 장점은 아래와 같다.

## 1. 문법적 의미
---
- final 키워드를 사용하면 어차피 다른 곳에서 상속할 일이 없는 ViewController를
문법적으로 막으므로 다른 곳에서 상속이 불가능해지므로 안정성이 있는 코드가
된다.

- 메소드나 프로퍼티에 final을 붙이면 override가 불가능하므로 의도하지 않은
override를 막을 수 있다.

## 2. 성능적 이점
---
Swift는 클래스마다 vTable이라는 것을 가지고 클래스 내 함수중 어떤 함수를
호출할지 결정한다. vTable은 함수가 오버라이딩 되었는지 확인하고 현재 클래스의
함수를 호출할지 아니면 상속한 부모 클래스의 함수를 호출할지 정한다. swift는
dynamic dispatch 방식을 채택함으로서 이 과정이 런타임에 일어난다.

즉 final을 붙여주면 어떤 함수를 호출할지 미리 정해주므로 Direct Call이 일어나 런타임에서의 성능이 좋아진다. 

이외에도 프로퍼티나 메소드에 private을 붙여서 해당 프로퍼티, 메소드가 해당
클래스에서만 사용되는 것을 표시해서 Direct Call이 일어나게 할 수 도 있다.

[출처](https://itllbegone.tistory.com/m/10)
[출처](https://itllbegone.tistory.com/m/10)
