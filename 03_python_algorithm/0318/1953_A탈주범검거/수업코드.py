import sys
sys.stdin = open('input.txt')

pipe = [
    [0, 0, 0, 0], # 0
    # 상하좌우
    [1, 1, 1, 1], # 1
    [1, 1, 0, 0], # 2
    [0, 0, 1, 1], # 3
    [1, 0, 0, 1], # 4
    [0, 1, 0, 1], # 5
    [0, 1, 1, 0], # 6
    [1, 0, 1, 0]  # 7
]
di, dj = (-1, 1, 0, 0), (0, 0, -1, 1)
opp = [1, 0, 3, 2]


def BFS(N, M, si, sj, L):
    q = []
    v = [[0]*M for _ in range(N)]
    
    q.append((si, sj))
    v[si][sj] = 1
    cnt = 1  # 있을 수 있는 곳 세어보기
    
    while q:
        ci, cj = q.pop(0)
        # 종료 조건
        if v[ci][cj] == L:
            return cnt
        
        for k in range(4):
            ni, nj = ci+di[k], cj+dj[k]
            if 0<=ni<N and 0<=nj<M and v[ni][nj] == 0:
                if pipe[arr[ci][cj]][k] and pipe[arr[ni][nj]][opp[k]]:
                    q.append((ni, nj))
                    v[ni][nj] = v[ci][cj] + 1
                    cnt += 1
    
    return cnt
    
    
T = int(input())
for tc in range(1, T + 1):
    # N M은 매트릭스, R C는 뚜껑위치, L은 소요시간
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = BFS(N, M, R, C, L)
    print(f'#{tc} {ans}')
    
    