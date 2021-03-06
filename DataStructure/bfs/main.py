g = {
    1 : [ 2,3],
    2 : [ 1,4,5],
    3 : [ 1],
    4 : [ 2],
    5 : [ 2]
}


def bfs(g, start):
    qu = []
    done = set() # 중복을 허용하지 않는 파이썬의 자료형
                 # 방문한 노드인지 확인하기 위한 변수
    qu.append(start)
    done.add(start) 

    while qu:
        p = qu.pop(0)
        print(p)
        for x in g[p]:
            if x not in done:
                qu.append(x)
                done.add(x)


bfs(g, 1)
