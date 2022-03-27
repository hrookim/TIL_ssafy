"""
dfs로 풀어보기!
종료시점: n>12
복잡하지 않은 경우 직접 작성하는 것이 더 좋다. loop가 여러 번 도는 것이 그다지 좋지는 않기 때문에
"""
import sys
sys.stdin = open('input.txt')


def DFS(n, ssum):
    global ans
    if n > 12:
        if ssum < ans:
            ans = ssum
        return
    # 1일권
    DFS(n+1, ssum+lst[n]*day)
    # 1달권
    DFS(n+1, ssum+mon)
    # 3달권
    DFS(n+3, ssum+mon3)
    # 1년권
    DFS(n+12, ssum+year)


T = int(input())
for tc in range(1, T+1):
    day, mon, mon3, year = map(int, input().split())
    lst = [0] + list(map(int, input().split()))
    
    ans = 12345678
    DFS(1, 0)
    print(f'#{tc} {ans}')


    # 두번째 방법 그리디 DP
    D = [0]*13
    for i in range(1, 13):
        mmin = D[i-1] + lst[i]*day
        mmin = min(mmin, D[i-1] + mon)
        if i >= 3:
            mmin = min(mmin, D[i-3] + mon3)
        if i >= 12:
            mmin = min(mmin, D[i-12] + year)
        D[i] = mmin
    
    print(f'#{tc} {D[12]}')