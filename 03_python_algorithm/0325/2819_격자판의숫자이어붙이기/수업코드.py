"""
격자 전체를 순회하면서, si sj를 기준으로 가능한 모든 경우(6번)를 이동 => 7자리 숫자
경우의수는 set로 중복을 제거해서 구한다.
가능한 모든 경우 -> DFS 사용
* 시간복잡도
n: 숫자 개수 / 총 경우는 4 ** 7 를 탐색하게 된다. (2 ** 50) 이하는 해도 괜찮다.
"""
import sys
sys.stdin = open('input.txt')


def DFS(n, i, j, num):
    if n == 7:
        sset.add(num)
        return
    # 함수 호출 부분 (4방향)
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = i+di, j+dj
        if 0<=ni<4 and 0<=nj<4:
            DFS(n+1, ni, nj, num*10+arr[ni][nj])


T = int(input())
for tc in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    sset = set()
    
    for i in range(4):
        for j in range(4):
            DFS(0, i, j, 0)
    print(f'#{tc} {len(sset)}')