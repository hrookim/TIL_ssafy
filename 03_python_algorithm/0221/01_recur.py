# 재귀로 배열을 복사하는 함수를 만든다면?
# A = [10, 20, 30]
# B = [ ,  ,  ]

A = [10, 20, 30]
B = [0]*3


def f(i, N):
    if i == N:
        return
    else:
        B[i] = A[i]
        f(i+1, N)


f(0, 3)
print(B)