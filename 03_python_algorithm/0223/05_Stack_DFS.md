# 05_Stack_DFS

비선형구조인 그래프 구조는 그래프로 표현된 모든 자료를 빠짐없이 검색하는 것이 중요하다.

* 두가지 방법:
  * 깊이 우선 탐색(Depth First Search, DFS)
  * 너비 우선 탐색(Breadth First Search, BFS)



## DFS

시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 깊이 탐색해 가다가 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아와서 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하는 순회 방법

> 재귀, 반복으로 구현할 수 있다.

가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 다시 DFS를 반복해야 하므로 후입선출 구조의 **스택**을 사용한다.



### 알고리즘

1. 시작 정점 v를 결정하여 방문한다.
2. 정점 v에 인접한 정점 중에서
   * 방문하지 않은 정점 w가 있다면, 정점v를 스택에 push하고 정점w를 방문한다. 그리고 w를 v로 하여 다시 `2.`를 반복한다.
   * 방문하지 않은 정점이 없으면, 탐색의 방향을 바꾸기 위해서 스택을 pop하여 받은 가장 마지막 방문 정점을 v로 하여 다시 `2.`를 반복한다.
3. 스택이 공백이 될 때까지 `2.`를 반복한다.



#### 반복문을 사용한 DFS

```python
def dfs():
    # 특정 정점(vertex, node)에 방문했는지 체크
    visited = [False for _ in range(V+1)]
    # 앞으로 방문할 정점을 모아 놓은 stack
    to_visit = [S]
    
    # 1. 방문해야할 곳이 있다면,
    while to_visit:
        # 2. 현재 위치를 stack의 top인 아이로 해서
        current = to_visit.pop()
        # 3. 방문하지 않았다면, 방문을 해라
        if not visited[current]:
            visited[current] = True
            # 3-1. 만약 그곳이 goal이라면 거기서 멈춰!
            if current = G:
                return visited[G]
            # 3-2. 그곳이 goal이 아니라면 연결된 곳들을 to_visit에 넣어줘
            to_visit += graph[current]
    
    return visited[G]


V = 5  # vertex의 개수
E = 6  # 간선의 개수
S = 1  # start 지점의 번호
G = 5  # goal 지점의 번호
graph = [[] for _ in range(V+1)]  # 각 정점들을 인덱스로 받아서 연결된 정점의 번호를 갖고있는 2차원 배열
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)

```



#### 재귀를 사용한 DFS

```python
def dfs(v):
    visited[v] = True
    
    # 후입선출 구조의 stack의미를 활용
    for new_v in graph[v][::-1]:
        if not visited[new_v]:
            dfs(new_v)
```

#### delta + 재귀 DFS

```python
def dfs_delta(i, j):
    visited[i][j] = True
    
    # 0. base case
    if matrix[i][j] == 3:  # 목표지점
        return True
    # 1. 이동할 수 있는 곳 찾아서 가보기. 상 우 하 좌 순
    for di, dj in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ni = i + di
        nj = j + dj
        # 2. 갈 수 있는 길이면서
        if 0 <= ni < N and 0 <= nj < N and matrix[ni][nj] != 1:
            # 2. 방문한 적이 없다면 이동
            if not visited[ni][nj]:
                dfs_delta(ni, nj)
```



## 계산기

문자열로 된 계산식이 주어질 때, 스택을 이용해 이 계산식의 값을 계산할 수 있다.

* 문자열 수식 계산의 일반적 방법
  * 중위 표기법의 수식을 후위 표기법으로 변경한다. (스택 이용)
  * 후위 표기법의 수식을 스택을 이용해 계산한다.

> 중위 표기법: 연산자를 피연산자의 가운데 표기하는 방법 `A+B`
>
> 후위 표기법: 연산자를 피연산자 뒤에 표기하는 방법 `AB+`



### 중위표기식의 후위표기식 변환 방법 (1)

1. 수식의 각 연산자에 대해서 우선순위에 따라 괄호를 사용하여 다시 표현한다.
2. 각 연산자를 그에 대응하는 오른쪽 괄호의 뒤로 이동시킨다.
3. 괄호를 제거한다.



### 중위표기식의 후위표기식 변환 방법 (2)

1. 입력 받은 중위표기식에서 토큰을 읽는다. (*수식을 하나 떼어 오는 것이다.*)
2. 토큰이 피연산자이면 토큰을 출력한다.
3. 토큰이 연산자(괄호포함)일 때, 이 토큰이 스택의 top에 저장되어 있는 연산자보다 우선순위가 높으면 스택에 push하고, 그렇지 않다면 스택 top의 연산자의 우선순위가 토큰의 우선순위보다 작을 때까지 스택에서 pop한 후 토큰의 연산자를 push한다. 만약 top에 연산자가 없다면 push한다.