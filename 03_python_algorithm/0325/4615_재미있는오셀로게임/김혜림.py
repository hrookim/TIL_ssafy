# 1 흑돌 / 2 백돌
# N은 보드 한 변의 길이 M은 돌을 놓는 횟수
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T+1):
    N, M = map(int, input().split())
    matrix = [[0] * N for _ in range(N)]
    stones = [(N//2, N//2, 2), (N//2, N//2+1, 1), (N//2+1, N//2, 2), (N//2+1, N//2+1, 1)]
    for _ in range(M):
        x, y, v = map(int, input().split())
        matrix[x][y] = v