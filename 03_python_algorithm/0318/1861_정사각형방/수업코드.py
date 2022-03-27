import sys
sys.stdin = open('input.txt')


def BFS(si, sj):
    global v
    q = []
    s = []
    
    q.append((si, sj))
    v[si][sj] = 1
    s.append(arr[si][sj])

    while q:
        ci, cj = q.pop(0)
        for di, dj in ((1, 0), (0, 1), (-1, 0), (0, -1)):
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N and v[ni][nj] == 0 and abs(arr[ni][nj]-arr[ci][cj]) == 1:
                q.append((ni, nj))
                v[ni][nj] = 1
                s.append(arr[ni][nj])
    return min(s), len(s)

            
T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    
    num, cnt = N*N, 0
    v = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if v[i][j] == 0:
                # temp n , temp cnt
                tn, tc = BFS(i, j)
                if tc > cnt or tc == cnt and tn < num:
                    cnt = tc
                    num = tn
    print(f'#{t} {num} {cnt}')
                