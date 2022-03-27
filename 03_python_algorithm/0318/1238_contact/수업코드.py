import sys
sys.stdin = open('input.txt')


def BFS(s):
    q = []
    # visited 방문 표시
    v = [0] * 101
    
    q.append(s)
    v[s] = 1
    sol = s
    
    while q:
        c = q.pop(0)
        # 1-1. 정답인 아이 찾기
        if v[sol] < v[c] or v[c] == v[sol] and sol < c:
            sol = c
        # 1-2. 조건에 맞는 아이를 q에 넣기
        for j in range(1, 101):
            if adj[c][j] and v[j]==0:
                q.append(j)
                v[j] = v[c]+1
    return sol


T = 10

for tc in range(1, T+1):
    N, S = map(int, input().split())
    lst = list(map(int, input().split()))
    
    # 0. 인접행렬 생성
    adj = [[0] * 101 for _ in range(101)]
    for i in range(0, len(lst), 2):
        adj[lst[i]][lst[i+1]] = 1
    
    ans = BFS(S)
    print(f'#{tc} {ans}')