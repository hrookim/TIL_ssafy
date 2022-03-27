import sys
sys.stdin = open('input.txt')


def find_max_home(i, j, K):
    global M, max_home
    # 방범 받을 수 있는 범위 내에 들어있는 집 수 tmp 찾기
    tmp = 0
    t = 0
    while t <= K - 1:
        if t == 0:
            # j가 0이하로 나오는 경우 인덱싱이 잘못될 수 있다.
            if j - (K - t - 1) <= 0:   
                tmp += sum(matrix[i][0:j + (K - 1) + 1])
            else:  
                tmp += sum(matrix[i][j - (K - 1):j + (K - 1) + 1])
        else:
            # j가 0이하로 나오는 경우 인덱싱이 잘못될 수 있다.
            if j - (K - t - 1) <= 0:
                if 0 <= i - t < N:
                    tmp += sum(matrix[i - t][0:j + (K - t - 1)+1]) 
                if 0 <= i + t < N:
                    tmp += sum(matrix[i + t][0:j + (K - t - 1)+1]) 
            else:
                if 0 <= i - t < N:
                    tmp += sum(matrix[i - t][j - (K - t - 1):j + (K - t - 1)+1]) 
                if 0 <= i + t < N:
                    tmp += sum(matrix[i + t][j - (K - t - 1):j + (K - t - 1)+1]) 
        t += 1
    # 손해보지 않음: 방범가능한 집 * 비용 >= 운영비용
    if tmp*M >= (K**2 + (K-1)**2) and tmp > max_home:
        max_home = tmp
    
    
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    K = 1
    max_home = 0
    while K <= 2*N:
        for i in range(N):
            for j in range(N):
                find_max_home(i, j, K)
        K += 1
    
    print(f'#{tc} {max_home}')