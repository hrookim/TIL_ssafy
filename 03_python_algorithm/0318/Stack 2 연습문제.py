# N개의 숫자를 원소로 가진 집합 A의 부분집합 중, 워소의 합이 K인 부분집합의 개수 출력(없으면 0)
# N = 4, 원소는 [1, 4, 3, 2] K = 5인 경우 

def DFS(n, ssum):
    global sol
    """ 가지치기는 풀이 후 가장 마지막에 고려! 
     if ssum >= K:
    	return
    """
    if n>=N:
        if ssum == K:
            sol += 1
        return
    DFS(n+1, ssum + lst[n])
    DFS(n+1, ssum)

N, K = 4, 5
lst = [1, 4, 3, 2]
sol = 0
DFS(0, 0)
print(f'#1 {sol}')