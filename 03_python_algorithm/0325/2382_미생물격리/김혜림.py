#  (상: 1, 하: 2, 좌: 3, 우: 4)
# 41 / 50 맞은 코드...
import sys
sys.stdin = open('input.txt')


def move():
    global time, q, arr
    di, dj = (0, -1, 1, 0, 0), (0, 0, 0, -1, 1)
    opp = [0, 2, 1, 4, 3]

    for t in range(1, M + 1):
        if t > 1:
            q = tmp_q
            arr = tmp_arr
        tmp_q = []
        tmp_arr = [[0] * N for _ in range(N)]
        while q:
            dbck = set()
            ci, cj, k = q.pop(0)
            # 경계선에서 줄고 방향이 전환됨
            if ci in (0, N - 1) or cj in (0, N - 1):
                arr[ci][cj] = arr[ci][cj] // 2
                k = opp[k]
            ni, nj = ci + di[k], cj + dj[k]
            if 0 <= ni < N and 0 <= nj < N:
                # 차있지 않다면 그대로 넣기
                if tmp_arr[ni][nj] == 0:
                    tmp_arr[ni][nj] = arr[ci][cj]
                    tmp_q.append([ni, nj, k])
                else:
                    # 이미 차 있어서, 더 큰 군집의 방향을 따르려 한다면
                    if tmp_arr[ni][nj] < arr[ci][cj]:
                        tmp_arr[ni][nj] += arr[ci][cj]
                        tmp_q.append([ni, nj, k])
                        for i in range(len(tmp_q)):
                            if tmp_q[i][0] == ni and tmp_q[i][1] == nj:
                                ti, tj, td = tmp_q.pop(i)
                                break
                    else:
                        tmp_arr[ni][nj] += arr[ci][cj]

        if t == M:
            for i in (0, N - 1):
                for j in range(N):
                    if tmp_arr[i][j]:
                        tmp_arr[i][j] = tmp_arr[i][j] // 2
            for j in (0, N - 1):
                for i in range(N):
                    if tmp_arr[i][j]:
                        tmp_arr[i][j] = tmp_arr[i][j] // 2
            return tmp_arr


T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    arr = [[0] * N for _ in range(N)]

    time = 0
    q = []
    for _ in range(K):
        i, j, v, d = map(int, input().split())
        arr[i][j] += v
        q.append([i, j, d])

    new_arr = move()

    ssum = 0
    for i in range(N):
        for j in range(N):
            ssum += new_arr[i][j]
    print(f'#{tc} {ssum}')    
