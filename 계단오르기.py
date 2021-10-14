import collections


def climbStairs(n: int) -> int:
    # 1. 재귀 브루트포스로 풀기(피보나치수열과 유사) => 타임아웃
    if n == 1:
        return n
    elif n == 2:
        return n
    return climbStairs(n - 1) + climbStairs(n - 2)


result = climbStairs(10)
print(result)

dp = collections.defaultdict(int)


def climbStairs2(n: int) -> int:
    # 2. 타블레이션 (상향식 풀이)
    dp[1] = 1  # 초기값 설정
    dp[2] = 2  # 초기값 설정
    for i in range(1, n + 1):
        dp[i + 2] = dp[i] + dp[i + 1]


climbStairs2(10)
print(dp[10])


def climbStairs3(n: int) -> int:
    if n <= 2:
        return n
    if dp[n]:
        return dp[n]
    dp[n] = climbStairs3(n - 1) + climbStairs3(n - 2)
    return dp[n]
