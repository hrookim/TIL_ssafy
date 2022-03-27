# 중간에 비어있는 번호 있음, 연락을 받을 수 없는 사람도 있음
# 연락을 이미 받은 사람에게는 연락을 하지 않는다.
import sys
sys.stdin = open('input.txt')


def bfs(n):
    global visited, to_contact
    to_contact[1].append(n)
    for time in range(1, N//2+1):
        while to_contact[time]:
            # current n
            cn = to_contact[time].pop()
            visited[cn] = 1
            
            # new n
            if contacts.get(cn):
                for nn in contacts[cn]:
                    if not visited[nn]:
                        to_contact[time+1].append(nn)
                        contacted[time+1].append(nn)
                

T = 10

for tc in range(1, T+1):
    # 데이터의 길이와 시작점
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    
    # 0. 연락망 구축하기
    contacts = {}
    for i in range(N//2):
        nfrom, nto = numbers[i*2], numbers[i*2+1] 
        # 0-1. 비어있다면
        if not contacts.get(nfrom):
            contacts[nfrom] = []
            contacts[nfrom].append(nto)
        # 0-2. 안 비어있다면
        else:
            contacts[nfrom].append(nto)
    # 0-3. 중복제거
    for key, value in contacts.items():
        contacts[key] = list(set(value))
    
    # 1. 연락돌리기
    visited = [0] * 101
    to_contact = {x: [] for x in range(1, N // 2 + 1)}
    contacted = {x: [] for x in range(1, N // 2 + 1)}
    bfs(S)
    
    results = []
    for y in range(N//2, 0, -1):
        if contacted[y]:
            results = contacted[y]
            break
    
    print(f'#{tc} {max(results)}')