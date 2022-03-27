import sys
sys.stdin = open('input.txt')


def DFS(n, ssum):
    global B, ans
    # 가지치기
    if ssum >= B+ans:
        return
    
    # 종료조건
    if n == N:
        if ssum >= B and ssum-B < ans:
            ans = ssum-B
        return
    
    # 하부 함수 실행
    DFS(n+1, ssum + lst[n])  # 포함
    DFS(n+1, ssum)           # 안 포함
 
        
T = int(input())
for tc in range(1, T+1):
    N, B = map(int, input().split())
    lst = list(map(int, input().split()))
    ans = 12345678
    DFS(0, 0)
    print(f'#{tc} {ans}')