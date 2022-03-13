def fibo_memo(n):
    if n >= 2 and memo[n] == 0:
        memo[n] = fibo_memo(n-1) + fibo_memo(n-2)
    return memo[n]


N = 10
memo = [0] * (N+1)
memo[0] = 0
memo[1] = 1
print(fibo_memo(N))
print(memo)