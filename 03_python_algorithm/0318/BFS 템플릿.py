# 그래프 G, 시작점 v
def BFS(G, v, n):
    # 생성
    visited = [0] * (n+1)
    queue = []
    queue.append(v)
    visited[v] = 1
    
    while queue:
        t = queue.pop(0)
        visit(t)
        # 조건에 맞는 경우
        for i in G[t]:
            if not visited[i]:
                queue.append(i)
                # n으로부터 1만큼 이동한 것이다
                visited[i] = visited[n] + 1
    