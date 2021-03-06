## 삽입 정렬

삽입 정렬은 배열의 가장 첫 두 인덱스부터 시작하여 하나하나씩 범위를 증가시켜가며 맞는 자리를 찾아갑니다.

만약 [2, 1, 4 ,3 ] 이라는 배열이 있으면

```python
[3,1] # => [1,3]
```

를 먼저 비교합니다. 1이 더 작으므로 자리를 바꿔줍니다. 그다음 인덱스를 확장합니다.

```python
[1, 3, 4] # => [1, 3, 4]
```

에서 3와 4를 비교합니다. 오름차순으로 정렬이 되어 있으니 그대로 둡니다.

```python
[1, 3, 4, 2] # => [1, 3, 2, 4] => [1, 2, 3, 4]
```

2와 4를 비교합니다. 2가 더 작으므로 자리를 바꿔줍니다. 그리고 그 다음 두 인덱스 3과 2를 비교합니다. 2가 더 작으므로 자리를 또 바꿔줍니다.

그리고 마지막으로 인덱스 0인 1과 인덱스 1인 2는 이미 정렬이 잘 되어 있으므로 그대로 둡니다.

```python
def insert_sort(list):
    for i in range(1, len(list)):
        while i > 0 and list[i] < list[i-1]:
            list[i], list[i-1] = list[i-1], list[i]  # swap
            i = i-1
```

삽입 정렬은 제한된 배열에서 정렬을 하므로 공간 복잡도는 O(1)이고 반복문 두 개를 사용하므로 시간 복잡도는 O(n^2)입니다.
