n, k = map(int, input().split())
height = list(map(int, input().split()))

def solution():
    dp = [0] * n
    dp[0] = 0

    for i in range(1, n):
        dp[i] = float('inf')

        for j in range(1, k + 1):
            if i - j >= 0:
                cost = dp[i - j] + abs(height[i] - height[i - j])
                dp[i] = min(dp[i], cost)

    return dp[n - 1]

print(solution())
